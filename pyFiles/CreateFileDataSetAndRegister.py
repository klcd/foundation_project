#!/usr/bin/env python
# coding: utf-8



import azureml.core
from azureml.core import Workspace

# Load the workspace from the saved config file
ws = Workspace.from_config()




# Get the default datastore
default_ds = ws.get_default_datastore()
default_ds.name




from azureml.core import Dataset]




#Create a file dataset from the path on the datastore (this may take a short while)
file_data_set = Dataset.File.from_files(path=(default_ds, './data/id_00/**/*.wav'))

# Get the files in the dataset
for file_path in file_data_set.to_path():
    print(file_path)




file_data_set = file_data_set.register(workspace=ws,
                                            name='pump_00',
                                            description='Pump sound files for normal and abnormal cases',
                                            tags = {'format':'WAV'},
                                            create_new_version=True)






