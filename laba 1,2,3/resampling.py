from lib import *
from timeit import timeit

@timeit
def upsample(image, m):
    return resample_one_way(image, m, 1)

@timeit
def downsample(image, n):
    return resample_one_way(image, 1, n)

@timeit
def resample_two_ways(image, m, n):
    up = upsample(image, m)
    down = downsample(up, n)
    return down

@timeit
def resample_one_way(image, m, n):
    w = image.width * m // n
    h = image.height * m // n
    map = list(image.getdata())
    map = np.array(map)
    px = map.reshape((image.height, image.width, 3))
    new_image = np.empty((h, w, 3), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            x = i - 1
            y = j - 1
            rx = x * n // m
            ry = y * n // m
            new_image[x][y] = px[rx][ry]
    new_image = Image.fromarray(new_image, "RGB")
    return new_image