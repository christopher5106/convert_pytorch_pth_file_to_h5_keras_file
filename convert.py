import torch
filename = '/sharedfiles/XLM/mlm_tlm_xnli15_1024.pth'
reloaded = torch.load(filename)

print(reloaded['model'])

# ['model_weights', 'optimizer_weights']
# list(f1["model_weights"])
#
# #!/usr/bin/env python
# import h5py
#
# # Create random data
# import numpy as np
# data_matrix = np.random.uniform(-1, 1, size=(10, 3))
#
# # Write data to HDF5
# data_file = h5py.File('file.hdf5', 'w')
# data_file.create_dataset('model_weights', data=data_matrix)
# data_file.create_dataset('optimizer_weights', data=data_matrix)
#
# data_file.close()
