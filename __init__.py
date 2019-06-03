import json

from collections import defaultdict

from . import hdf5_maker
from . import video_maker
from . import gif_maker
from . import saver

save_hdf5 = hdf5_maker.save_hdf5
HDF5Dataset = hdf5_maker.HDF5Dataset

show_image = video_maker.show
init_video = video_maker.init
add_to_video = video_maker.add

add_to_gif = gif_maker.add
save_gif = gif_maker.save
clear_gif = gif_maker.clear

dictlist = lambda: defaultdict(list)

log = saver.Experiment()


def load_json(path):
    def _cast(x):
        try:
            return float(x)
        except:
            return str(x)


    with open(path, 'r') as f:
        data = json.load(f)

    for key in data:
        data[key] = _cast(data[key])

    return data
