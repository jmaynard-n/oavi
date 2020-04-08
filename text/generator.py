from PIL import Image, ImageDraw, ImageFont
from bin import Thresholding_Otsu as otsu
from semi import semitone as gray

def generator():
    alphabet = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    fnt = ImageFont.truetype("./fonts/A.D. MONO.ttf", 60)
    for s in alphabet:
        img = Image.new('RGB', (20, 50), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((1, -10), s, font = fnt, fill = (0, 0, 0))
        name = s + ".png"
        img = otsu(gray(img))
        img.save("./refs/" + name)
    return 0


