from PIL import Image
import numpy as np
import os

def weight(feat):
    sq = 20 * 50
    i = 0
    smbl = dict()
    list = []
    for j in os.listdir('./refs'):
        list.append("./refs/" + j)
    for s in list:
        img = Image.open(s, 'r')
        map = np.asarray(img, dtype=np.uint8)
        px = map.reshape((img.height, img.width))
        w = np.count_nonzero(px == 0)
        feat[i, 0] = w
        feat[i, 1] = w / sq
        i += 1
        smbl.update({s[-5]: px})
    return smbl