import csv

def save(feat):
    f = feat.tolist()
    # print(f)
    with open("features.csv", 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['weight', 'weight per sq', 'centerX', 'centerY', 'norm_centerX', 'norm_centerY', 'momentX', 'momentY', 'norm_momentX', 'norm_momentY'])
        for line in f:
            writer.writerow(line)
