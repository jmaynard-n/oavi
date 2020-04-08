from lib import *
from timeit import timeit

@timeit
def roberts(image, filename):
    h = image.height
    w = image.width
    map = np.asarray(image, dtype=np.uint8)
    px = map.reshape((h, w))
    g_x = np.empty((h, w), dtype=np.uint8)
    g_y = np.empty((h, w), dtype=np.uint8)
    # g = np.empty((h, w), dtype=np.uint8)
    v = 1
    mx = np.array([[0, 0, 0], [0, -1, 0], [0, 0, 1]], np.uint8)
    my = np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]], np.uint8)
    it = np.nditer([px, g_x, g_y],
                   flags = ['multi_index'],
                   op_flags=[['readonly'], ['writeonly'], ['writeonly']])
    while not it.finished:
        x = it.multi_index[1]
        y = it.multi_index[0]
        if (x < v or x > w - 1 - v) or (y < v or y >= h - 1 - v):
            it[1] = it[2] = it[0]
            it.iternext()
            continue
        else:
            win = px[y - v: y + v + 1, x - v: x + v + 1]
            it[1] = np.sum(win * mx)
            it[2] = np.sum(win * my)
        it.iternext()

    g_x = g_x * (255 // np.amax(g_x))
    g_y = g_y * (255 // np.amax(g_y))

    # g = np.sqrt(np.absolute(g_x) + np.absolute(g_y))
    g = g_x ** 2 + g_y ** 2
    g = g * (255 // np.amax(g))

    g_x = Image.fromarray(g_x, "L")
    g_y = Image.fromarray(g_y, "L")
    g = Image.fromarray(g, "L")

    g_x.save("./res/outline/x/" + filename)
    g_y.save("./res/outline/y/" + filename)
    g.save("./res/outline/f/" + filename)

    return g
