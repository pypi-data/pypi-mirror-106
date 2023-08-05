import numpy as np
import imageio
from guang import path
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
import cv2
from guang import implot, auto_canny
from skimage import measure
from skimage import filters


def circle_detect(image, rangeR=(200, 250), total_num_peaks=1):
    """
    :param rangeR: detected circles' Radius range
    :param total_num_peaks: detect circles number
    return (accums, cx, cy, radii)"""
    # image = cv2.bilateralFilter(image, 21, 75, 75)
    image = cv2.medianBlur(image, 15)
    edges = canny(image, low_threshold=3, high_threshold=10)  # sigma=3,
    # plt.imshow(edges)
    # plt.show()
    hough_radii = np.arange(rangeR[0], rangeR[1], 2)
    hough_res = hough_circle(edges, hough_radii)

    accums, cx, cy, radii = hough_circle_peaks(hough_res,
                                               hough_radii,
                                               total_num_peaks=total_num_peaks)
    return accums, cx, cy, radii


def edge_detect(image, mode="roberts"):
    """
    :param image: 2d gray image array
    :param mode: options -- "roberts", "sobel", "threshold"
    :return:
    """
    if mode.lower() == "roberts":
        edge = filters.roberts(image)
    elif mode.lower() == "sobel":
        edge = filters.sobel(image)
    elif mode.lower() == "threshold":
        pass
    else:
        raise ValueError("mode error")

    return edge


def test():

    image = cv2.imread(path("../data/pikaqiu.jpg"), 0)
    edge_roberts = filters.roberts(image)
    edge_sobel = filters.sobel(image)
    implot(edge_sobel)
    implot(edge_roberts)


# test()


def test_edge():
    # image = imageio.imread(path("../data/pikaqiu.jpg"))
    import matplotlib.pyplot as plt
    image = cv2.imread(path("../data/pikaqiu.jpg"), 0)
    implot(image)
    # image = filters.sobel(image)
    # implot(image,channel='gray')
    # image = 255*image
    # image = image.astype("uint8")
    # ret2, img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # print(ret2)
    img = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 5, 5)
    # img = cv2.medianBlur(img, 5)
    implot(img)
    img = 255 - img
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
    gray_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # 形态学
    implot(gray_img)
    gray_img = cv2.medianBlur(img, 3)
    implot(auto_canny(gray_img, 100))
    implot(image)
    contours = measure.find_contours(gray_img, 120)
    plt.figure()
    for n, contour in enumerate(contours):
        plt.plot(contour[:, 1], contour[:, 0], linewidth=2)
    plt.axis("equal")


# test_edge()


def test_circle_detect():
    from guang.cv.video import getFrame
    import matplotlib.pyplot as plt
    from skimage.draw import circle_perimeter
    from skimage import color

    # dst = cv2.pyrMeanShiftFiltering(image, 10, 100)   #边缘保留滤波EPF
    fps, size_17, img = getFrame(
        filename=r'C:\Users\beidongjiedeguang\Desktop\实验\62.avi',
        frameNum=723,
    )
    image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    accums, cx, cy, radii = circle_detect(image,
                                          rangeR=[100, 250],
                                          total_num_peaks=1)
    image = color.gray2rgb(image)
    for center_y, center_x, radius in zip(cy, cx, radii):
        circy, circx = circle_perimeter(center_y, center_x, radius)
        image[circy, circx] = (220, 20, 20)

    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(20, 10))
    ax.imshow(image, cmap=plt.cm.gray)
    plt.show()


if __name__ == "__main__":
    pass
