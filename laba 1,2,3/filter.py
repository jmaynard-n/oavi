from lib import *
from timeit import timeit
from resampling import downsample

@timeit
def filter(image):
    # image = image.resize((image.width // 5, image.height // 5))
    # print("resized")
    # image.show()
    h = image.height
    w = image.width
    map = np.asarray(image, dtype=np.uint8)
    px = map.reshape((h, w)).copy()
    new_image = np.empty((h, w), dtype=np.uint8)
    # окно движется по изображению
    v = 1
    it = np.nditer(px, flags = ['multi_index'])
    # print("START")
    while not it.finished:
        # ищем макс и мин в окне
        x = it.multi_index[1]
        y = it.multi_index[0]
        if (x < v  or x > w - 1 - v) or (y < v or y >= h - 1 - v):
            # print("x = ", x,"y = ", y, "cont")
            new_image[y, x] = it[0]
            it.iternext()
            continue
        # elif y == h - 1 - v:
        #     break
        win = px[y - v : y + v + 1, x - v: x + v + 1]
        mx = np.amax(win)
        mn = np.amin(win)
        # print(win, mx, mn, it[0])
        donut = win.copy()
           # смотрим на центральный
           # если макс то ищем другой макс и заменяем на него
        if it[0] == mx:
            donut[v, v] = 0
            new_image[y, x] = np.amax(donut)
            # print("changed to ", np.amax(donut))
        # если мин то аналог макс
        elif it[0] == mn:
            donut[v, v] = mx
            new_image[y, x] = np.amin(donut)
            # print("changed to ", np.amin(donut))
        else:
            new_image[y, x] = it[0]
            # print("not changed")
        it.iternext()
    # xor = np.bitwise_xor(px, new_image)
    # xor = Image.fromarray(new_image, "L").show()
    # image.show()
    sub = px - new_image
    # sub = Image.fromarray(new_image, "L").show()
    new_image = Image.fromarray(new_image, "L")
    # new_image.show()
    return new_image

def mask(image, new):
    h = image.height
    w = image.width
    px = np.asarray(image, dtype=np.uint8).reshape((h, w))
    nx = np.asarray(new, dtype=np.uint8).reshape((h, w))
    mask = np.empty((h, w), dtype=np.uint8)
    it = np.nditer([px, nx, mask], op_flags=[['readonly'], ['readonly'], ['writeonly']])
    while not it.finished:
        # if it[0] != it[1]:
        #     it[2] = 255
        # else:
        #     it[2] = 0
        it[2] = np.abs(it[0] - it[1])
        it.iternext()
    mask = Image.fromarray(mask, "L")
    return mask