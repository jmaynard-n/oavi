import csv
from timeit import timeit

@timeit
def save(f, i='', header = 1):
    # f = feat.tolist()
    # print(f)
    with open("features" + i +".csv", 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        if header:
            writer.writerow(['weight', 'weight per sq', 'centerX', 'centerY', 'norm_centerX', 'norm_centerY', 'momentX', 'momentY', 'norm_momentX', 'norm_momentY'])
        for line in f:
            writer.writerow(line)
