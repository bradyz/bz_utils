"""
Turns a list of dicts into an hdf5 file, like Pandas to_csv().
All items must be numpy ndarrays.
"""
import h5py


def save_hdf5(dataset_path, data_list, dtypes):
    data = {key: list() for key in dtypes.keys()}

    for row in data_list:
        for key in data:
            data[key].append(row[key])

    with h5py.File(dataset_path, mode='w') as h:
        for key, val in data.items():
            h.create_dataset(key, data=val, dtype=dtypes[key])
