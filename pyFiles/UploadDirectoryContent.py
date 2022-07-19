#!/usr/bin/env python
# coding: utf-8


from azureml.data.datapath import DataPath
from azureml.core import Dataset
import azureml.core
from azureml.core import Workspace

# Load the workspace from the saved config file
ws = Workspace.from_config()
print('Ready to use Azure ML {} to work with {}'.format(
    azureml.core.VERSION, ws.name))


# Get the default datastore
default_ds = ws.get_default_datastore()

# Enumerate all datastores, indicating which is the default
for ds_name in ws.datastores:
    print(ds_name, "- Default =", ds_name == default_ds.name)


Dataset.File.upload_directory(src_dir='./data/id_00/abnormal/',
                              target=DataPath(
                                  default_ds, './data/id_00/abnormal/')
                              )


Dataset.File.upload_directory(src_dir='./data/id_00/normal/',
                              target=DataPath(
                                  default_ds, './data/id_00/normal/')
                              )
