import csv
from bin import Thresholding_Otsu as otsu
from semi import semitone
from PIL import Image
import numpy as np
from profile import profiles, prof_axis
from croping import crop
from segmentation import segment
from generator import str_gen
import os
import shutil

def imprt(file):
    img = Image.open(file, 'r')
    img = img.convert("RGB")
    img = otsu(semitone(img))
    return img

def set_dirs(i):
    if os.path.exists("./phrases/" + i):
        shutil.rmtree("./phrases/" + i)
    os.mkdir("./phrases/" + i)
    if os.path.exists("./phrases/" + i + "/smbls"):
        shutil.rmtree("./phrases/" + i + "/smbls")
    os.mkdir("./phrases/" + i + "/smbls")
    if os.path.exists("./phrases/" + i + "/prof_x"):
        shutil.rmtree("./phrases/" + i + "/prof_x")
    os.mkdir("./phrases/" + i + "/prof_x")
    if os.path.exists("./phrases/" + i + "/prof_y"):
        shutil.rmtree("./phrases/" + i + "/prof_y")
    os.mkdir("./phrases/" + i + "/prof_y")

phrases = ["HEY WHERE DO YOU GET IT FROM","ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ALEJANDRO WAS FILLED WITH THE TRANSCENDENCE OF WHAT WAS HAPPENING AND KNEW THE MEANING OF LIFE","BUT VIXEN IS PIQUED", "WHAT GOES UP MUST GO DOWN", "GRAPE JELLY WAS TASTY", "LOVE IS NOT LIKE PIZZA"]

# with open('features.csv') as f:
#     reader = csv.reader(f, delimiter=';')
#     gold = list(reader)
# gold.pop(0)
# alf = {key: val for key, val in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}




for i in range(1, 2):
    str_gen(phrases[i - 1], str(i))
    new = imprt("phrase" + str(i) + ".png")
    set_dirs(str(i))
    new.save("./phrases/" + str(i) + "/" + "phrase" +".bmp")
    map = np.asarray(new, dtype=np.uint8)
    px = map.reshape((new.height, new.width))
    prof_axis(px, str(i * 1000), 0, "./phrases/" + str(i) + "/prof")
    prof_axis(px, str(i * 1000), 1, "./phrases/" + str(i) + "/prof")
    px = crop(px, [0])
    # profiles(None, px, i * 1000, "./phrases/" + str(i) + "/prof")
    pr_x = prof_axis(px, str(i), 0, None)
    coords = segment(pr_x)
    print(coords)
    k = 1;
    for c in coords:
        new = Image.fromarray(px[:, c[2] : c[3]], "L")
        new.save("./phrases/" + str(i) + "/smbls/" + str(k) + ".png")
        profiles(None, px[:, c[2] : c[3]], k, "./phrases/" + str(i) + "/prof")
        k+=1
