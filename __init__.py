import json

from collections import defaultdict

from . import hdf5_maker
from . import video_maker
from . import gif_maker
from . import saver
from . import mpl_render

save_hdf5 = hdf5_maker.save_hdf5
HDF5Dataset = hdf5_maker.HDF5Dataset

show_image = video_maker.show

init_video = video_maker.init
add_to_video = video_maker.add

add_to_gif = gif_maker.add
save_gif = gif_maker.save
clear_gif = gif_maker.clear

mpl_to_numpy = mpl_render.to_numpy

dictlist = lambda: defaultdict(list)

log = saver.Experiment()


def load_json(path):
    with open(path, 'r') as f:
        data = json.load(f)

    return data
