rename_mat_cols = {
    "U-beginn Datum": "date",
    "Leistung_DGVS": "key_dgvs",
    "Fachgebiet": "intervention_type",
    "U-Dauer": "duration",
    "Auftragsnummer": "ID",
}


rename_imd_cols = {
    "Laufende Nr. der Materialdokumentation": "id_mat_doc",
    "Status Materialdokumentation": "documentation_status",
    "Verabreichungsdatum": "date",
    "Materialnummer": "id_mat",
    "Materialtext": "name",
    "Name 1": "manufacturer",
    "Materialmenge": "quantity",
    "Mengeneinheit": "unit",
    "Materialpreis": "price",
    "Währung": "currency",
    "Lfd. Nr. Leistung": "ID",
}


drop_values_imd = {
    "documentation_status": [2, 4]
}  # 2 and 4 correspond to invalid documentations

drop_values_material = {
    "intervention_type": [
        "MC_Gastroskopie",
        "MC_Ileokoloskopie",
        "MC_Koloskopie",
        "MENELMGKE",
        "Manometrie Ösophagus",
    ]
}
