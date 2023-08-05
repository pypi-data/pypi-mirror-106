from imageio_ffmpeg import read_frames  # limited functionality
import av  # pip install av   # fast
from guang.cv.video import getFrame  # I'm the best
from guang.Utils.toolsFunc import path

reader = read_frames(path(r"F:\硬盘\高阶V\888"))
meta = reader.__next__()
"""
>>> meta
{'ffmpeg_version': '4.2.2 built with gcc 9.2.1 (GCC) 20200122',
 'codec': 'h264',
 'pix_fmt': 'yuv420p(tv',
 'fps': 29.97,
 'source_size': (720, 396),
 'size': (720, 396),
 'duration': 6971.0}
"""
