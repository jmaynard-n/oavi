import numpy as np

from generator import generator as gen
from profile import profiles
from weight import weight
from centre import centre
from save_csv import save
# сгенерировать изображения символов
# gen()
# подсчитать признаки
features = np.zeros((26, 10), dtype=np.float)
# print(features)
# вес черного и удельный вес
smbl = weight(features)
centre(features, smbl)
save(features)
profiles(smbl)
# print(features.tolist())