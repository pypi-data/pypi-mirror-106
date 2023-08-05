'''
This is a universal function library.
'''
from . import utils

__version__, __name__ = utils.version_config(update=False)
__version__ = '0.' + __version__
print('guang.__version__=:', __version__)  # '0.0.7.2.7'
__author__ = 'K.y <beidongjiedeguang@gmail.com>'
__license__ = 'GPL-v3'
__copyright = 'Copyright 2020 K.y'

from .Utils.toolsFunc import path, broadcast, dict_dotable, Cons, rm, sort_count, d_time, index_char, yaml_load, yaml_dump
from .guang import ppath
from .cv.utils import implot, auto_canny
# __all__ = ["ML","Utils","DL", "Voice", "wechat", "ML", "interesting", "app", "cv",]
