import numpy as np
from PIL import Image
from croping import crop
from timeit import timeit

@timeit
def prof_axis(px, k, ax, path):
    x = np.sort(px, axis=ax)
    if ax == 0:
        x = np.flip(x, axis=ax)
    img = Image.fromarray(x, "L")
    if ax == 0 and path is not None:
        img.save(path + "_x/" + k + "_x.png")
    elif path is not None:
        img.save(path + "_y/" + k + "_y.png")
    return x

def main_part(px, k, path):
    px = crop(px, [0, 1])
    prof_axis(px, k, 0, path)
    prof_axis(px, k, 1, path)

@timeit
def profiles(smbl, arr=None, key=0, path="./"):
    if arr is not None:
        main_part(arr, str(key), path)
    else:
        for k in smbl.keys():
            px = smbl.get(k)
            main_part(px, k, path)
