import numpy as np
from timeit import timeit

# @timeit
def white(img, axis):
    h = np.shape(img)[axis]
    # print(img.shape, h)
    rows = []
    for i in range(0, h):
        if axis == 0:
            # print(i, img[i, :], )
            wh = (img[i, :] != 255).sum()
        else:
            wh = (img[:, i] != 255).sum()
        if wh == 0:
            rows.append(i)
    return rows

@timeit
def crop(img, ax):
    for i in ax:
        img = np.delete(img, white(img, i), axis=i)
    return img