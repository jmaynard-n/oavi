import numpy as np

from generator import generator as gen
from profile import profiles
from weight import weight
from centre import centre
from save_csv import save
# сгенерировать изображения символов
gen()
# подсчитать признаки

# print(features)
# вес черного и удельный вес
smbl, features = weight('./refs/')
centre(features, smbl)
f = features.tolist()
save(f)
profiles(smbl, path="./prof")
# print(features.tolist())