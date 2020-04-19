from PIL import Image
import numpy as np
import os
from timeit import timeit

@timeit
def weight(path):
    i = 0
    smbl = dict()
    list = []
    for j in os.listdir(path):
        list.append(path + j)
    # list.sort()
    feat = np.zeros((len(list), 10), dtype=np.float)
    for s in list:
        img = Image.open(s, 'r')
        map = np.asarray(img, dtype=np.uint8)
        px = map.reshape((img.height, img.width))
        # print(img.height , img.width)
        sq = img.height * img.width
        w = np.count_nonzero(px == 0)
        i = int(s[- s[::-1].find('/') : s.find('.png')]) - 1 ## changed
        feat[i, 0] = w
        feat[i, 1] = w / sq
        # i += 1
        # print(s, s.find(".png"), s[ : s.find('.png')], s[::-1], s[::-1].find('/'))
        smbl.update({ s[- s[::-1].find('/') : s.find('.png')] : px})
    return smbl, feat