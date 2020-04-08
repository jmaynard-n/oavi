from collections import Counter
from PIL import Image
import numpy as np
# from timeit import timeit

# @timeit
def Thresholding_Otsu(img):
    nbins = 256
    map = np.asarray(img, dtype=np.uint8)
    pixel_counts = Counter(map.ravel())
    counts = np.array([0 for x in range(256)])
    for c in sorted(pixel_counts):
        counts[c] = pixel_counts[c]
    p = counts / sum(counts)
    sigma_b = np.zeros((256, 1))
    for t in range(nbins):
        q_L = sum(p[:t])
        q_H = sum(p[t:])
        if q_L == 0 or q_H == 0:
            continue

        miu_L = sum(np.dot(p[:t], np.transpose(np.matrix([i for i in range(t)])))) / q_L
        miu_H = sum(np.dot(p[t:], np.transpose(np.matrix([i for i in range(t, 256)])))) / q_H
        sigma_b[t] = q_L * q_H * (miu_L - miu_H) ** 2

    t = np.argmax(sigma_b)

    map = np.asarray(img, dtype=np.uint8)
    px = map.reshape((img.height, img.width, 1))
    new_image = np.empty((img.height, img.width), dtype=np.uint8)
    for index, pix in np.ndenumerate(px):
        i = index[0]
        j = index[1]
        if pix < t:
            new_image[i][j] = 0
        else:
            new_image[i][j] = 255
    new_image = Image.fromarray(new_image, "L")
    return new_image

def Niblack(image):
    map = np.asarray(image, dtype=np.uint8)
    px = map.reshape((image.height, image.width))
    new_image = px.copy()
    h = image.height
    w = image.width
    mx = np.amax(px)
    mn = np.amin(px)

    aver = px.copy()
    stdev = px.copy()
    v = 15
    it = np.nditer([px, aver, stdev], flags=['multi_index'],
                   op_flags=[['readonly'], ['writeonly'], ['writeonly']])
    while not it.finished:
        x = it.multi_index[1]
        y = it.multi_index[0]
        if (x < v or x > w - 1 - v) or (y < v or y > h - 1 - v):
            if np.abs(mx - it[0]) < np.abs(mn - it[0]):
                it[1] = mx // (h * w)
                it[2] = mx ** 2 // (h * w) - it[1]
            else:
                it[1] = mn // (h * w)
                it[2] = mn ** 2 // (h * w) - it[1]
            it.iternext()
            continue
        win = px[y - v: y + v + 1, x - v: x + v + 1]
        # mx = np.amax(win)
        # mn = np.amin(win)
        it[1] = np.sum(win) // (v * 2 + 1)
        it[2] = np.sum(win ** 2) // (v * 2 + 1) - it[1]
        it.iternext()

    it = np.nditer([px, new_image, aver, stdev],
                   op_flags=[['readonly'], ['writeonly'], ['readonly'], ['readonly']])
    while not it.finished:
        t = it[2] - it[3] * 0.2
        if it[0] < t:
            it[1] = 0
        else:
            it[1] = 255
        it.iternext()
    new_image = Image.fromarray(new_image, "L")
    return new_image