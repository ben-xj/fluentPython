"""
Usages of joblib
"""
import time

from joblib import Parallel, delayed


def calculate_square(x):
    # simulate a bunch of things...
    time.sleep(0.1)
    return x * x


def square_list(x: list):
    return [i * i for i in x]


if __name__ == '__main__':
    # parallel processing
    # start = time.time()
    # results = Parallel(n_jobs=4, backend='loky', prefer='threads', batch_size=25)(delayed(calculate_square)(i) for i in range(100))
    # end = time.time()
    # print(results)
    # print('Time taken: {}'.format(end - start))

    arr = list(range(1000))
    start = time.time()
    results = Parallel(n_jobs=4, backend='loky')(delayed(square_list)(arr) for i in range(4000))
    # results = Parallel(n_jobs=4, backend='loky', batch_size=1000)(delayed(square_list)(arr) for i in range(4000))
    end = time.time()
    print('Time taken: {}'.format(end - start))
