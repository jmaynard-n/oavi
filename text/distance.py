from save_csv import save
from timeit import timeit

def euclid(curr, gold):
    val = 0
    for (c, g) in zip(curr, gold):
        val += (float(g) - c) ** 2
    val = val ** 0.5
    return val

@timeit
def dist(curr, gold, alf, k):
    curr = curr.tolist()
    string = ''
    result = []
    for c in curr:
        probability = []
        # i = 0
        for i, g in enumerate(gold):
            p = euclid(c, g)
            probability.append((alf[i], p))

        probability.sort(key=(lambda x: x[1]))
        string += (probability[0])[0]
        result.append(probability)
    # result = np.array(result, dtype=np.float)
    # result.sort(axis=1)
    save(result, "_result_" + k, 0)
    return string