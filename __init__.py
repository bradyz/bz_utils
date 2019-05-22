from collections import defaultdict

from . import hdf5_maker
from . import video_maker
from . import gif_maker

save_hdf5 = hdf5_maker.save_hdf5

show_image = video_maker.show
init_video = video_maker.init
add_to_video = video_maker.add

add_to_gif = gif_maker.add
save_gif = gif_maker.save
clear_gif = gif_maker.clear

dictlist = lambda: defaultdict(list)
