import numpy as np
from timeit import timeit

@timeit
def moment(feat, smbl, iter=True):
    sumx = 0
    sumy = 0
    i = 0
    for px in smbl.keys():
        if not iter:
            i = int(px) - 1
        x = feat[i, 2]
        y = feat[i, 3]
        sq = np.shape(smbl[px])[0] ** 2 + np.shape(smbl[px])[1] ** 2
        for index, pix in np.ndenumerate(smbl[px]):
            if pix == 255:
                p = 0
            else:
                p = 1
            sumx += p * (x - index[0]) ** 2
            sumy += p * (y - index[1]) ** 2
        feat[i, 6] = sumx
        feat[i, 7] = sumy
        feat[i, 8] = sumx / sq
        feat[i, 9] = sumy / sq
        i += 1
        sumx = 0
        sumy = 0

@timeit
def centre(feat, smbl, iter=True):
    sumx = 0
    sumy = 0
    i = 0
    for px in smbl.keys():
        for index, pix in np.ndenumerate(smbl[px]):
            if pix == 255:
                p = 0
            else:
                p = 1
            sumx += p * index[0]
            sumy += p * index[1]
        # print(sumx, sumy)
        if not iter:
            i = int(px) - 1
            # print(i)
        feat[i, 2] = sumx / feat[i, 0]
        feat[i, 3] = sumy / feat[i, 0]
        # print(sumx / feat[i, 0], feat[i, 3])
        feat[i, 4] = feat[i, 2] / np.shape(smbl[px])[0]
        feat[i, 5] = feat[i, 3] / np.shape(smbl[px])[1]
        i += 1
        sumx = 0
        sumy = 0
    moment(feat, smbl, iter)