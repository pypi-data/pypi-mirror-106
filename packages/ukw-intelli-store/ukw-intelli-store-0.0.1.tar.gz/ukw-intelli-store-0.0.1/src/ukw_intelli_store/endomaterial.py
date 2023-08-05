import pandas as pd
import numpy as np
from typing import List, Union
from datetime import date
from datetime import datetime as dt

from .config import (drop_values_imd, drop_values_material, rename_imd_cols, rename_mat_cols)
from .utils import filter_time

# 
expected_mat_cols = list(rename_mat_cols.keys())
expected_imd_cols = list(rename_imd_cols.keys())

class EndoMaterial:
    """Class for handling endo storage data.

    path_imd (str): Points to a xlsx file with columns:
        Verabreichungszeit
        Geändert am
        Uhrzeit
        Status
        Materialdokumentation
        Materialnummer
        Materialtext
        Name 1
        Materialmenge
        Mengeneinheit
        Materialpreis
        Währung
        Anford. OE fachlich
        Lfd. Nr.
        Leistung

    path_mat (str): Points to a xlsx file with columns:
        Auftragsnummer
        U-beginn Datum
        U-Ende Datum
        U-Dauer
        Fachgebiet
        Leistung_DGVS
        Untersucher
        Untersucher 2

    ----------
    Attributes:

    self.imd: df
    self.mat: df
    self.n_rows: dict describing number of rows in dataframe when reading from source and after preprocessing
    self.summary: dict

    --------
    Methods:

    preprocess_data
    preprocess_imd
    preprocess_mat
    validate_data
    clean_gdvs_keys
    get_mat_info_for_id
    get_mat_info
    make_features
    drop_tows_by_col_value
    generate_summary
    get_description
    get_dgvs_keys
    get_professions
    get_profession_summary
    get_dgvs_key_summary
    get_most_common_material
    get_highest_cost_material
    get_case_info
    """

    def __init__(self, path_imd, path_mat_doc):
        # Read DFs
        self.imd = pd.read_excel(path_imd)
        self.mat = pd.read_excel(path_mat_doc)
        self.n_rows = {"imd_init": len(self.imd), "mat_init": len(self.mat)}

        self.preprocess_data()

        # Generate Mat info dict ({mat_id: {"price": XX, "name": X, "manufacturer":XX}})
        self.get_mat_info()

        self.make_features()
        self.summary = self.generate_summary()
        # self.time_series_df = self.get_time_series_summary(self.mat)

    def preprocess_data(self):
        """Preprocessing pipeline for imd and mat dataframes.
        Asserts that input format is correct.
        Renames columns
        Drops columns we wont need
        Drops rows with invalid data
        """
        self.drop_values_imd = drop_values_imd
        self.drop_values_material = drop_values_material
        self.expected_imd_cols = expected_imd_cols
        self.expected_mat_cols = expected_mat_cols

        self.preprocess_imd()
        self.preprocess_mat()
        self.validate_data()
        self.not_mat_cols = self.mat.columns.tolist()
        self.not_mat_cols.append("price_total")

        print(self.n_rows)

    def preprocess_imd(self):
        """
        Inplace Preprocessing of self.imd.
        Drops all cols not mentioned in rename_imd_cols.
        Drops all rows with values mentioned in drop_values_imd
        Changes "date" col from datetime to date
        filters out dates before 1.1.2020
        drops all rows with na values
        """
        _ = self.imd.columns.to_list()
        print("IMD Cols:", _)
        for col in self.expected_imd_cols:
            assert col in _

        # drop_cols
        self.imd.drop(
            self.imd.columns.difference(list(rename_imd_cols.keys())),
            axis=1,
            inplace=True,
        )
        self.imd.rename(columns=rename_imd_cols, inplace=True)

        # drop rows with specified values we want to filter out
        for column, values in self.drop_values_imd.items():
            self.imd = self.drop_rows_by_col_value(self.imd, column, values)

        # set dt objects to date
        self.imd["date"] = self.imd["date"].dt.date
        # drop values with date before 1.1.2020 (default of function)
        self.imd = self.imd[filter_time(self.imd["date"])]

        # Drop Remaining NA
        self.imd.dropna(axis=0, how="any", inplace=True)
        self.n_rows["imd_after_processing"] = len(self.imd)

    def preprocess_mat(self):
        """
        Inplace Preprocessing of self.mat.
        Drops all cols not mentioned in rename_mat_cols.
        Drops all rows with values mentioned in drop_values_mat
        Changes "date" col from datetime to date
        filters out dates before 1.1.2020
        drops all rows with na values
        """
        _ = self.mat.columns.to_list()
        print("MAT Cols: ", _)
        for col in self.expected_mat_cols:
            assert col in _

        # drop_cols
        self.mat.drop(
            self.mat.columns.difference(list(rename_mat_cols.keys())),
            axis=1,
            inplace=True,
        )
        # rename
        self.mat.rename(columns=rename_mat_cols, inplace=True)

        # drop rows with specified values we want to filter out
        for column, values in self.drop_values_material.items():
            self.mat = self.drop_rows_by_col_value(self.mat, column, values)

        # set dt objects to date
        self.mat["date"] = self.mat["date"].dt.date
        # drop values with date before 1.1.2020 (default of function)
        self.mat = self.mat[filter_time(self.mat.date)]

        self.mat.set_index("ID", inplace=True)
        self.mat[self.mat["duration"] < 0]["duration"] = np.nan

        # Drop Remaining NA
        self.mat.dropna(axis=0, how="any", inplace=True)
        self.mat["key_dgvs"] = self.clean_dgvs_keys()

        self.n_rows["mat_after_processing"] = len(self.mat)

    def validate_data(self):
        """
        Removes IDs which have no matches in other df (mat vs imd)
        """
        mat_ids = self.mat.index.unique()
        imd_ids = self.imd["ID"].unique()
        mat_dates = self.mat["date"].sort_values(ascending=True).to_list()
        imd_dates = self.imd["date"].sort_values(ascending=True).to_list()

        self.validation_report = {
            "n_ids_mat": len(mat_ids),
            "n_ids_imd": len(imd_ids),
            "mat_ids_without_match": [_ for _ in mat_ids if _ not in imd_ids],
            "imd_ids_without_match": [_ for _ in imd_ids if _ not in mat_ids],
            "mat_date_range": [mat_dates[0], mat_dates[-1]],
            "imd_date_range": [imd_dates[0], imd_dates[-1]],
        }

        id_list = self.validation_report["mat_ids_without_match"]
        if len(id_list) > 0:
            print(
                f"mat data contains {len(self.validation_report['mat_ids_without_match'])} ids which are not found in imd data, removing them"
            )
            self.mat.drop(id_list, axis=0, inplace=True)
        id_list = self.validation_report["imd_ids_without_match"]
        if len(id_list) > 0:
            print(
                f"imd data contains {len(self.validation_report['imd_ids_without_match'])} ids which are not found in imd data, removing them"
            )
            self.imd = self.drop_rows_by_col_value(self.imd, "ID", id_list)

    def clean_dgvs_keys(self):
        """Looks for values with '#' in self.mat["key_dgvs"], and changes them so the entry with the highest number replaces the earlier valie

        Example: ÖDG040#ÖGD060 -> ÖGD060

        Returns:
            list or pd series: same length as self.mat, containing cleaned keys
        """
        replace = []
        keys = self.mat["key_dgvs"].to_list()
        for i, key in enumerate(keys):
            if "#" in key:
                elements = key.split("#")
                element_values = [
                    [digit for digit in element if digit.isdigit()]
                    for element in elements
                ]
                element_values = [int("".join(digits)) for digits in element_values]
                index = element_values.index(
                    max(element_values)
                )  # if multiple numbers with same value exist, first is chosen
                replace.append((i, elements[index]))

        for replacement in replace:
            keys[replacement[0]] = replacement[1]

        return keys

    def get_mat_info_for_id(self, mat_id):
        """Expects mat_id. Queries self.imd for entry with this id which was used with  successfull documentation. Returns dictionary with keys "price", "name", manufacturer.

        Args:
            mat_id (int|float): ID of the material

        Returns:
            dict: dictionary with keys "price", "name", and "manufacturer"
        """
        try:
            select = (
                np.array(self.imd["id_mat"] == mat_id)
                * np.array(self.imd["documentation_status"] == 3)
            )
            entry = self.imd.loc[select, ["price", "name", "manufacturer", "quantity"]].copy()
            entry["price"] = entry["price"] / entry["quantity"]
            entry = entry.iloc[0, :].drop(columns = ["quantity"])
            return entry
        except:
            print(f"Failed to get info for id {mat_id}")
            return {
                "price": 0,
                "name": "NOT FOUND",
                "manufacturer": "NOT FOUND",
            }

    def get_mat_info(self):
        """Generates dictionary containing info for each material ID. Info is generated via self.get_mat_info_for_id function.
        Assigns result to self.mat_info
        """
        self.mat_info = {
            _: {"price": 0, "name": "", "manufacturer": ""}
            for _ in self.imd["id_mat"].unique()
        }
        for key in self.mat_info.keys():
            _info = self.get_mat_info_for_id(key)
            self.mat_info[key]["price"] = _info["price"]
            self.mat_info[key]["manufacturer"] = _info["manufacturer"]
            self.mat_info[key]["name"] = _info["name"]

    def make_features(self):
        """
        Merges imd data into material dataframe: For each material ID a column is added. Additionally the price_total column is added.
        """
        mat_ids = list(self.mat_info.keys())
        self.mat.loc[:, "price_total"] = 0
        self.mat.loc[:, mat_ids] = 0
        for _id in self.mat.index:
            _rows = self.imd[self.imd["ID"] == _id]
            for index, row in _rows.iterrows():
                amount = row["quantity"]
                _mat_id = row["id_mat"]
                if amount > 0 and _mat_id in mat_ids:
                    self.mat.loc[_id, _mat_id] = +amount
                    self.mat.loc[_id, "price_total"] = +row["price"]

    def drop_rows_by_col_value(self, df, colname, value_list):
        """Expects dataframe, colname and list of values to remove. All rows containing one of the specified values in the specified column are removed. Returns new dataframe.

        Args:
            df (pd.DataFrame): target df
            colname (str|int): colname
            value_list (List): list of value

        Returns:
            pd.DataFrame: dataframe with removed entries
        """
        df = df.copy()
        n_dropped = 0
        for value in value_list:
            select = df[colname] == value
            n_dropped = +select.sum()
            df.drop(df[select].index, axis=0, inplace=True)

        print(f"Dropped {n_dropped} rows at '{colname}'")
        return df

    def generate_summary(
        self, start_date: date = date(2020, 1, 1), end_date: date = dt.now().date()
    ) -> dict:
        """Summarizes all data between given dates.

        Args:
            start_date (date, optional): Defaults to date(2020, 1, 1).
            end_date (date, optional): Defaults to dt.now().date().

        Returns:
            dict: contains summary keys "key_dgvs" and "intervention_types".
        """
        select = filter_time(self.mat["date"], start_date, end_date)
        df = self.mat[select]

        professions = self.get_professions(df)
        dgvs_keys = self.get_dgvs_keys(df)

        _summary = {
            "key_dgvs": {
                key: self.get_dgvs_key_summary(self.mat, key) for key in dgvs_keys
            },
            "intervention_types": {
                profession: self.get_profession_summary(self.mat, profession)
                for profession in professions
            },
        }

        return _summary

    def get_description(self):
        tmp = self.mat.loc[:, ["duration", "price_total", "intervention_type"]]
        tmp = tmp.groupby(["intervention_type"])
        _ = tmp.describe()
        return _

    def get_dgvs_keys(self, df:pd.DataFrame=None):
        if df is None:
            df = self.mat.copy()
        _ = list(df["key_dgvs"].unique())
        _.sort()
        return _

    def get_professions(self, df:pd.DataFrame=None):
        """Returns all unique values in the intervention type column

        Returns:
            list: list of unique intervention_type values of the mat dataframe
        """
        if df is None:
            df = self.mat.copy()
        _ = list(df["intervention_type"].unique())
        _.sort()
        return _

    def get_profession_summary(
        self, _mat: pd.DataFrame=pd.DataFrame(), profession: str = None, round_precision: int = 2
    ) -> dict:
        """Expects mat df and profession string. Returns summary (n_performed, mean_cost, mean_duration, top 5 used materials, top 5 most expensive materials)

        Args:
            _mat (pd.DataFrame): [description]
            profession (str): [description]
            round_precision (int, optional): [description]. Defaults to 2.

        Returns:
            dict: [description]
        """
        if _mat.empty:
            _mat = self.mat.copy()
        select = _mat["intervention_type"] == profession
        _mat_filtered = _mat[select]
        _summary = {
            "n_performed": select.sum(),
            "mean_cost": round(_mat_filtered["price_total"].mean(), round_precision),
            "mean_duration": round(_mat_filtered["duration"].mean(), round_precision),
            "top_most_used_mat_ids": self.get_most_common_material(_mat_filtered),
            "top_highest_cost": self.get_highest_cost_material(_mat_filtered),
        }
        return _summary

    def get_dgvs_key_summary(
        self, _mat: pd.DataFrame = pd.DataFrame(), key: str = None, round_precision: int = 2
    ) -> dict:
        if _mat.empty:
            _mat = self.mat.copy()
        select = _mat["key_dgvs"] == key
        _mat_filtered = _mat[select]
        _summary = {
            "n_performed": select.sum(),
            "mean_cost": round(_mat_filtered["price_total"].mean(), round_precision),
            "median_cost": round(_mat_filtered["price_total"].median(), round_precision),
            "cost_standard_deviation": round(_mat_filtered["price_total"].std(), round_precision),
            "mean_duration": round(_mat_filtered["duration"].mean(), round_precision),
            "top_most_used_mat_ids": self.get_most_common_material(_mat_filtered),
            "top_highest_cost": self.get_highest_cost_material(_mat_filtered),
        }
        return _summary

    def get_case_info(self, df: pd.DataFrame, case_id: Union[int, float]) -> dict:
        """Function expects mat-like dataframe and case_id (index of mat_like dataframes). Returns dictionary containing relevant case information.

        Args:
            df (pd.DataFrame): dataframe like EndoMaterial.mat
            case_id (Union[int, float]): case_id, index to select row in df

        Returns:
            dict: Dictionary summarizing the selected case. keys: date, duration, intervention_type, key_dgvs, price_total, {each mat_id which was used at least once in this case}
        """
        case_row = df.loc[case_id]
        case_row = case_row[case_row != 0]
        case_dict = case_row.to_dict()
        mat_ids = case_row.index.difference(self.not_mat_cols).to_list()
        for _id in mat_ids:
            _info = self.get_mat_info_for_id(_id).to_dict()
            _info["number_used"] = case_dict[_id]
            case_dict[_id] = _info
        return case_dict

    def get_most_common_material(self, df: pd.DataFrame, n: int = 5) -> List:
        """expects self.mat like dataframe. Drops all non material columns. Then sums the value of all remaining cols, returns list of index, value tuples of n highest values.

        Args:
            df (pd.DataFrame): self.mat like dataframe
            n (int, optional): number of values to return. Defaults to 5.

        Returns:
            List: List of tuples. [(mat_id, used amount)]
        """
        df = df.drop(columns=self.not_mat_cols)
        if n > 0:
            count = df.sum().sort_values(ascending=False)[:n]
        else:
            count = df.sum().sort_values(ascending=False)
        count = [_ for _ in count.items()]
        count = [
            (
                _id,
                _quantity,
                round(_quantity * self.mat_info[_id]["price"], 2),
                self.mat_info[_id]["name"],
            )
            for _id, _quantity in count
        ]
        return count

    def get_highest_cost_material(self, df: pd.DataFrame, n: int = 5) -> List:
        count = self.get_most_common_material(df, -1)
        count = sorted(count, key=lambda x: x[2], reverse=True)
        count = count[:n]

        return count
