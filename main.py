from PIL import Image
import numpy as np
# from bin import *

print("Current program can resample given image")
print("Choose want do you want to do:", "1 - upsample", "2 - downsample",
      "3 - resample M/N by two moves", "4 - resample M/N by 1 move",
      "5 - semitone picture","6 - Bradly's binarization",sep='\n')
action = int(input())
file = {1: "./images/desert.bmp", 2: "./images/girl.bmp",
        3: "./images/LAND2.bmp", 4: "./images/MARBLES.bmp", 5: "./images/bin.jpeg"}

print("Choose file:", file, sep ='\n')
name = int(input())

def upsample(image, m):
    w = image.width * m
    h = image.height * m
    map = list(image.getdata())
    map = np.array(map)
    px = map.reshape((image.height, image.width, 3))
    new_image = np.empty((h, w, 3), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            x = i - 1
            y = j - 1
            new_image[x][y] = px[x // m][y // m]
    new_image = Image.fromarray(new_image, "RGB")
    return new_image

# def downsample(image, n):
#     w = image.width // n
#     h = image.height // n
#     new_image = Image.new('RGB', (w, h))
#     px = image.load()
#     for i in range(image.width):
#         for j in range(image.height):
#             x = i // n - 1
#             y = j // n - 1
#             r = px[x * n, y * n][0]
#             g = px[x * n, y * n][1]
#             b = px[x * n, y * n][2]
#             new_image.putpixel((x, y), (r,g,b))
#     return new_image

def downsample(image, n):
    w = image.width // n
    h = image.height // n
    # map = list(image.getdata())
    map = np.asarray(image, dtype=np.uint8)
    px = map.reshape((image.height, image.width, 3))
    new_image = np.empty((h, w, 3), dtype=np.uint8)
    for i in range(image.height):
        for j in range(image.width):
            x = i // n - 1
            y = j // n - 1
            new_image[x][y] = px[x * n][y * n]
    new_image = Image.fromarray(new_image, "RGB")
    return new_image

def resample_two_ways(image, m, n):
    up = upsample(image, m)
    down = downsample(up, n)
    return down


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

def semitone(image):
    w = image.width
    h = image.height
    # map = list(image.getdata())
    map = np.asarray(image, dtype=np.uint8)
    px = map.reshape((image.height, image.width, 3))
    new_image = np.empty((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            new_image[i][j] = np.mean(px[i][j])
    new_image = Image.fromarray(new_image, "L")
    return new_image

# def binar(image):
#     image = semitone(image)
#     w = image.width
#     h = image.height
#     s = w // 8
#     s2 = s // 2
#     t = 0.15
#     sum = 0
#     map = np.asarray(image, dtype=np.uint8)
#     px = map.reshape((h, w))
#     new = np.empty((h, w), dtype=np.uint8)
#     integral = np.empty(w*h, dtype=np.uint8)
#     for i in range(h):
#         sum = 0
#         for j in range(w):
#             index = j * h + i
#             sum += px[i][j]
#             if i == 0:
#                 integral[index] = sum
#             else:
#                 integral[index] = integral[index-1] + sum
#     for i in range(h):
#         for j in range(w):
#             index = j * h + i
#             x1 = i - s2
#             x2 = i + s2
#             y1 = j - s2
#             y2 = j + s2
#             if (x1 < 0):
#                 x1 = 0
#             if (x2 >= w):
#                 x2 = w - 1
#             if (y1 < 0):
#                 y1 = 0
#             if (y2 >= h):
#                 y2 = h - 1
#             count = (x2 - x1) * (y2 - y1)
#             sum = integral[y2 * h + x2] - integral[y1 * h + x2] \
#                     - integral[y2 * h + x1] + integral[y1 * h + x1]
#             if px[i][j] * count < sum * (1 - t):
#                 new[i][j] = 0
#             else:
#                 new[i][j] = 255
#     new = Image.fromarray(new, "L")
#     return new

image = Image.open(file[name], 'r')
image = image.convert("RGB")

if action == 1:
    m = int(input("Enter m: "))
    new = upsample(image, m)
elif action == 2:
    n = int(input("Enter n: "))
    new = downsample(image, n)
elif action == 3:
    m, n = int(input("Enter m: ")), int(input("Enter n : "))
    new = resample_two_ways(image, m ,n)
elif action == 4:
    m, n = int(input("Enter m: ")), int(input("Enter n : "))
    new = resample_one_way(image, m, n)
elif action == 5:
    new = semitone(image)
elif action == 6:
    new = binar(image)

new.show()
# image.show()