from PIL import Image
# from timeit import timeit
from resampling import upsample, downsample, resample_one_way, resample_two_ways
from semi import semitone
from filter import filter, mask
from bin import Thresholding_Otsu, Niblack
from roberts import roberts

def imprt(file):
    image = Image.open(file, 'r')
    image = image.convert("RGB")
    return image

def apply_filter(filename):
    im = imprt("./images/noise/" + filename)
# tmp = Thresholding_Otsu(semitone(im))
    tmp = semitone(im)
    tmp.save("./res/noise/sem/" + filename)
    i = 10
    new = filter(tmp)
    while i:
        new = filter(new)
        i-=1
    new.save("./res/noise/filter/" + filename)
    maska = mask(tmp, new)
    maska.save("./res/noise/mask/" + filename)

# apply_filter("k1.bmp")
# apply_filter("k2.bmp")
# apply_filter("k3.bmp")
# apply_filter("k4.bmp")
# apply_filter("k5.bmp")
# apply_filter("k6.bmp")
# apply_filter("k7.bmp")
# apply_filter("k8.bmp")

def find_outline(filename):
    im = imprt("./images/outline/" + filename)
    tmp = semitone(im)
    tmp.save("./res/outline/sem/" + filename)
    grad = roberts(tmp, filename)

    i = 100
    new = filter(grad)
    while i:
        print(i)
        new = filter(new)
        i -= 1

    new = Thresholding_Otsu(new)
    new.save("./res/outline/fin/" + filename)


hun = imprt("./images/101.jpg")
ten = imprt("./images/11.jpg")
hun = semitone(hun)
ten = semitone(ten)
maska = mask(ten, hun)
maska.save("./res/noise/mask/" + "maskkk.jpg")
# for i in range(1, 13):
#     find_outline(str(i) + ".jpg")

# find_outline("2.jpg")
# find_outline("k8.bmp")

# print("DOWNSAMPLING")
# im = imprt("./images/down/LAND2.bmp")
# new = downsample(im, 3)
# new.save("./res/down/down_land3.png")
#
# im = imprt("./images/down/MARBLES.bmp")
# new = downsample(im, 5)
# new.save("./res/down/down_marb5.png")
#
# print("UPSAMPLING")
# im = imprt("./images/up/desert.bmp")
# new = upsample(im, 3)
# new.save("./res/up/desert3.png")
#
# im = imprt("./images/up/girl.bmp")
# new = upsample(im, 5)
# new.save("./res/up/girl5.png")
#
# print("RESAMPLING 2")
# im = imprt("./images/down/LAND2.bmp")
# new = resample_two_ways(im, 4, 9)
# new.save("./res/two ways/land49.png")
#
# im = imprt("./images/up/girl.bmp")
# new = resample_two_ways(im, 7, 3)
# new.save("./res/two ways/girl73.png")
#
# print("RESAMPLING 1")
# im = imprt("./images/down/LAND2.bmp")
# new = resample_one_way(im, 4, 9)
# new.save("./res/one way/land49.png")
#
# im = imprt("./images/up/girl.bmp")
# new = resample_one_way(im, 7, 3)
# new.save("./res/one way/girl73.png")
#
# print("SEMITONE")
# im = imprt("./images/down/LAND2.bmp")
# new = semitone(im)
# new.save("./res/semi/land.png")
#
# im = imprt("./images/up/girl.bmp")
# new = semitone(im)
# new.save("./res/semi/girl.png")
#
# print("THRESHOLDING")
# im = imprt("./images/bin/bin.bmp")
# new = Niblack(semitone(im))
# new.save("./res/bin/bin.png")

# im = imprt("./images/bin/blue_house_small.bmp")
# new = Niblack(semitone(im))
# new.save("./res/bin/blue_house.png")
#
# im = imprt("./images/bin/how_small.bmp")
# new = Thresholding_Otsu(semitone(im))
# new.save("./res/bin/small.png")
#
# im = imprt("./images/bin/old.bmp")
# new = Thresholding_Otsu(semitone(im))
# new.save("./res/bin/old.png")
#
# im = imprt("./images/bin/angle.jpg")
# new = Thresholding_Otsu(semitone(im))
# new.save("./res/bin/angle.png")
#
# im = imprt("./images/bin/blur.jpg")
# new = Thresholding_Otsu(semitone(im))
# new.save("./res/bin/blur.png")