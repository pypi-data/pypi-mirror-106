from __future__ import division
import os
from guang.sci.nt_toolbox.general import *
from guang.sci.nt_toolbox.signal import *
from guang.Utils.toolsFunc import path
from guang.cv import implot
import imageio, cv2

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

x0 = imageio.imread(ppath("../data/pikaqiu.jpg"))
imgplot(x0 / 255)

# print(ppath("../data/picaqiu.jpg"))
