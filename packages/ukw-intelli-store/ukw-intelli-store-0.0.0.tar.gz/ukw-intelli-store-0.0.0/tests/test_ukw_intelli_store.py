
from ukw_intelli_store.cli import main
from ukw_intelli_store.endomaterial import EndoMaterial

path_test_imd = "tests/data/imd.xlsx"
path_test_mat = "tests/data/mat.xlsx"

def test_main():
    assert main([]) == 0

def test_init():
    em = EndoMaterial(path_test_imd, path_test_mat)

def test_dgvs_keys():
    em = EndoMaterial(path_test_imd, path_test_mat)
    assert len(em.get_dgvs_keys()) == 3