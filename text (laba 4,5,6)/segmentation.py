import numpy as np
from croping import white
from timeit import timeit

@timeit
def segment(px):
    coords = []
    columns = white(px, 1)
    # print(columns)
    y = np.shape(px)[0]
    for i in range(1, len(columns)):
        if columns[i] - columns[i-1] > 1:
            coords.append((0, y, columns[i-1] + 1, columns[i]))
    return coords