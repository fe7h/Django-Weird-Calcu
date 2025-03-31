from functools import partial
import os

from .calculate import *
from .img_gen import img_gen as _img_gen


_img_path = os.path.join(os.path.dirname(__file__), 'img/meme.png')
img_gen = partial(_img_gen, path=_img_path)

__all__ = ['calculate', 'img_gen']
