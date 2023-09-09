import time

from joblib import Parallel, delayed
import numpy as np

from util.stopwatch import StopWatch

def func_with_large_input(i, arr):
    # print(arr.flags)
    time.sleep(0.01)
    arr_i = arr[i, :] + 1
    return arr_i

def test_serial(arr):
    sw = StopWatch()
    result = [func_with_large_input(i, arr) for i in range(100)]
    sw.stop()
    print(f'Serial: {sw.getElapsedTime()} ms')

def test_parallel(arr):
    sw = StopWatch()
    tasks = [delayed(func_with_large_input)(i, arr) for i in range(100)]
    result = Parallel(n_jobs=4)(tasks)
    sw.stop()
    print(f'Parallel: {sw.getElapsedTime()} ms')

def test_parallel_batch(arr):
    sw = StopWatch()
    n_jobs = 4
    jobs = 100
    batch_size = max(1, (jobs + n_jobs - 1) // n_jobs)
    # or
    # batch_size = max(1, int(math.ceil(jobs / n_jobs)))
    result = Parallel(n_jobs=n_jobs, batch_size=batch_size)(delayed(func_with_large_input)(i, arr) for i in range(100))
    sw.stop()
    print(f'Parallel with batch: {sw.getElapsedTime()} ms')


if __name__ == '__main__':
    arr = np.random.randint(0,100, size=(100, 50000))
    test_serial(arr)
    test_parallel(arr)
    test_parallel_batch(arr)