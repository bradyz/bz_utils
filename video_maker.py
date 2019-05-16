from pathlib import Path

import cv2


DEFAULT_DIR = str(Path.home().joinpath('debug'))
DEFAULT_PATH = 'video'


def _create_writer(video_path, height, width, fps=60):
    return cv2.VideoWriter(
            '%s.avi' % video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))


class Dummy(object):
    video = None
    video_path = None

    @classmethod
    def init(cls, save_dir=None, save_path=None):
        if cls.video is not None:
            cls.video.release()

        save_dir = Path(save_dir or DEFAULT_DIR).resolve()
        save_dir.mkdir(exist_ok=True)
        save_path = save_path or DEFAULT_PATH

        cls.video = None
        cls.video_path = str(save_dir.joinpath(save_path))

        cv2.destroyAllWindows()

    @classmethod
    def add(cls, image):
        if cls.video is None:
            cls.video = _create_writer(cls.video_path, image.shape[0], image.shape[1])

        cv2.imshow(cls.video_path, cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        cv2.waitKey(1)

        cls.video.write(image)


init = Dummy.init
add = Dummy.add
