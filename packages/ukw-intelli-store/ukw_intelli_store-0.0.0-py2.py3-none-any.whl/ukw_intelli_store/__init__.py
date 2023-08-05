'''
Package to read and process material export data.
To use, initiate an endomaterial object and start exploring!



---------
Examples:

## Init
from ukw_intelli_store import EndoMaterial
em = EndoMaterial(path, path)

## To explore all used materials:
em.mat_info

## To explore specific material id
em.get_mat_info_for_id(material_id)


## To get all logged dgvs keys:
em.get_dgvs_keys()

## To explore a single dgvs key:
em.get_dgvs_key_summary()

'''

__version__ = '0.0.0'
