import taichi as ti
import numpy as np
from guang import implot
# import cupy as cp
from pyprobar import probar, bar
import cv2
ti.init(arch=ti.cpu)

theta = np.linspace(0, 2 * np.pi, 2000)
x = theta
y = np.sin(theta)


def get_data_from_func():
    '''
    love
    '''
    n = 650
    t = np.linspace(0, 2 * np.pi, n)
    x = 16 * (np.sin(t))**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    X = x + 1j * y
    return x, y


# y,x = get_data_from_func()

rows, cols = (512, 512)


def imshow(x, y):
    global gui
    gui = ti.GUI("window", (rows, cols))
    background = np.zeros((rows, cols), dtype=np.uint8)
    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()
    scale_x = (cols - 1) / (xmax - xmin)
    scale_y = (rows - 1) / (ymax - ymin)

    pixel_x = np.round((x - xmin) * scale_x).astype(np.int)
    pixel_y = np.round((y - ymin) * scale_y).astype(np.int)

    for col, row in zip(pixel_x, pixel_y):
        background[col, row] = np.uint8(255)  # taichi
        # background[row, col] = np.uint8(255)  # opencv / matplotlib

    # imgplot(background)
    gui.set_image(background)
    gui.show()


imshow(x, y)

# filename = r"C:\Users\beidongjiedeguang\Downloads\Baidu Net Disk Downloads\en\beauty.mp4"
#
# cap = cv2.VideoCapture(filename)
# fps = cap.get(cv2.CAP_PROP_FPS)
# size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # 获取视频尺寸
# TotolFrameNum = int(cap.get(7))
# gui = ti.GUI('Window Title', size)
# for frameNum in range(TotolFrameNum):
#     bar(frameNum, TotolFrameNum, text=f"{frameNum}")
#     cap.set(cv2.CAP_PROP_POS_FRAMES, frameNum)  # 设置要获取的帧号
#     ret, frame = cap.read()
#     gui.set_image(frame.transpose(1,0,2))
#     gui.show()
