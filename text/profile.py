import numpy as np
from PIL import Image

def main_part(px, k):
    x = np.sort(px, axis=0)
    y = np.sort(px, axis=1)
    # print(x)
    x = np.flip(x, axis=0)
    x = Image.fromarray(x, "L")
    y = Image.fromarray(y, "L")
    nameX = k + "_x.png"
    nameY = k + "_y.png"
    x.save("./prof_x/" + nameX)
    y.save("./prof_y/" + nameY)

def profiles(smbl, arr=None, key=0):
    if arr is not None:
        main_part(arr, str(key))
    else:
        for k in smbl.keys():
            px = smbl.get(k)
            main_part(px, k)
