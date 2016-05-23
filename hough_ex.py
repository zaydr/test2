from skimage.transform import (hough_line, hough_line_peaks,
                               probabilistic_hough_line)
from skimage.feature import canny
from skimage import data
from skimage import io
import numpy as np
import matplotlib.pyplot as plt



edges = io.imread("edges_2.png")
img06_2 = io.imread("img06-2.tif")
h, theta, d = hough_line(edges)

plt.imshow(img06_2, cmap=plt.cm.gray)
rows, cols = edges.shape
for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
    plt.plot((0, cols), (y0, y1), '-r')

plt.show()
