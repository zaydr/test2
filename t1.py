
#do a battleship or computer vision project
import numpy as np
from skimage import io
from skimage import filters
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology
from skimage import feature
import os

test1 = io.imread("Img09-3.tif", 1)
edge_img = io.imread("edges.png",1)
testnp = np.asarray(test1)
testnp = testnp[0:1024,0:1024]

val = filters.threshold_otsu(testnp)
mask = testnp < val

morphology.binary_opening(mask, morphology.diamond(10)).astype(np.uint8)

edges1 = feature.canny(mask)
edges2 = feature.canny(mask, sigma = 3)
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3,figsize =(8,3), sharex = True, sharey = True)

ax1.imshow(mask, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)

ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                    bottom=0.02, left=0.02, right=0.98)
plt.show()
