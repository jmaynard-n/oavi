import numpy as np

def moment(feat, smbl):
    sumx = 0
    sumy = 0
    i = 0
    sq = 20 ** 2 + 50 ** 2
    for px in smbl.values():
        x = feat[i, 2]
        y = feat[i, 3]
        for index, pix in np.ndenumerate(px):
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

def centre(feat, smbl):
    sumx = 0
    sumy = 0
    i = 0
    for px in smbl.values():
        for index, pix in np.ndenumerate(px):
            if pix == 255:
                p = 0
            else:
                p = 1
            sumx += p * index[0]
            sumy += p * index[1]
        # print(sumx, sumy)
        feat[i, 2] = sumx / feat[i, 0]
        feat[i, 3] = sumy / feat[i, 0]
        # print(sumx / feat[i, 0], feat[i, 3])
        feat[i, 4] = feat[i, 2] / np.shape(px)[0]
        feat[i, 5] = feat[i, 3] / np.shape(px)[1]
        i += 1
        sumx = 0
        sumy = 0
    moment(feat, smbl)