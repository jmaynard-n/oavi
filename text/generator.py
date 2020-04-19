from PIL import Image, ImageDraw, ImageFont
from bin import Thresholding_Otsu as otsu
from semi import semitone as gray
from croping import crop
import numpy as np
from timeit import timeit

@timeit
def generator():
    alphabet = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    fnt = ImageFont.truetype("./fonts/A.D. MONO.ttf", 60)
    for s in alphabet:
        img = Image.new('RGB', (30, 50), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((1, -10), s, font = fnt, fill = (0, 0, 0))
        name = s + ".png"
        img = otsu(gray(img))
        img = to_crop(img)
        img.save("./refs/" + name)
    return 0

def str_gen(string, i):
    fnt = ImageFont.truetype("./fonts/A.D. MONO.ttf", 60)
    img = Image.new('RGB', (30 * len(string), 50), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((1, -10), string, font = fnt, fill = (0, 0, 0))
    d = ImageDraw.Draw(img)
    name = "phrase" + i + ".png"
    img = otsu(gray(img))
    img = to_crop(img, [0])
    img.save(name)
    return 0

def to_crop(img, axis = [0, 1]):
    map = np.asarray(img, dtype=np.uint8)
    px = map.reshape((img.height, img.width))
    px = crop(px, axis)
    image = Image.fromarray(px, "L")
    return image
