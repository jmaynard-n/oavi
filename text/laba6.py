import csv
from weight import weight
from centre import centre
from save_csv import save
from distance import dist

with open('features.csv') as f:
    reader = csv.reader(f, delimiter=';')
    gold = list(reader)
gold.pop(0)

# print(gold)

alf = {key: val for key, val in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

# print(alf)

for i in range(1, 2):
    smbl, features = weight("./phrases/" + str(i) + "/smbls/")
    print(smbl.keys())
    # print(features)
    centre(features, smbl, False)
    # print(features)
    save(features, str(i))
    # print("------------------------------------")
    # print(features)
    string = dist(features, gold, alf, str(i))
    print(string)
