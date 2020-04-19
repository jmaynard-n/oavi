from lib import *
from timeit import timeit

@timeit
def semitone(image):
    # print("SEMI START")
    w = image.width
    h = image.height
    # map = list(image.getdata())
    map = np.asarray(image, dtype=np.uint8)
    px = map.reshape((image.height, image.width, 3))
    new_image = np.empty((h, w), dtype=np.uint8)
    # print("IT START")
    for i in range(h):
        for j in range(w):
            new_image[i, j] = np.mean(px[i, j])
    # print("IT END")
    new_image = Image.fromarray(new_image, "L")
    return new_image