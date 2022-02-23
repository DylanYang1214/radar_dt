import os
import h5py

# dataset = 'RadarScenes\data'
# root_path = 'E:\datasets'
# dataset_path = os.path.join(root_path, dataset)

data_h5_file = r'E:\datasets\RadarScenes\data\sequence_1\radar_data.h5'

with h5py.File(data_h5_file, "r") as f:
    data = f.create_dataset
    print(' ')