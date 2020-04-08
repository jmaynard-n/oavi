from bin import Thresholding_Otsu as otsu
from semi import semitone
from PIL import Image
import numpy as np
from profile import profiles

def imprt(file):
    img = Image.open(file, 'r')
    img = img.convert("RGB")
    img = otsu(semitone(img))
    return img

for i in range(1, 4):
    new = imprt("phrase" + str(i) + ".png")
    new.save("phrase" + str(i) + ".bmp")
    map = np.asarray(new, dtype=np.uint8)
    px = map.reshape((new.height, new.width))
    profiles(None, px, i)

