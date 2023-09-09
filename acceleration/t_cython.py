"""
    @Date: 2023/9/1 19:34
    @Description: test cython
"""
import numpy as np

from acceleration.multiply import elementwise_multiply, elementwise_multiply_faster
from util.stopwatch import StopWatch


def elementwise_multiply_python(A, B):
    nrows, ncols = A.shape
    result = np.zeros((nrows, ncols), dtype=np.float64)

    for i in range(nrows):
        for j in range(ncols):
            result[i, j] = A[i, j] * B[i, j]

    return result


if __name__ == '__main__':

    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)

    repeat = 10
    sw = StopWatch()
    for _ in range(repeat):
        r1 = elementwise_multiply_python(A, B)
    sw.stop()
    print(f'Pure Python: {sw.getElapsedTime()} ms')

    sw.start()
    for _ in range(repeat):
        r3 = A * B
    sw.stop()
    print(f'Numpy: {sw.getElapsedTime()} ms')
    print((r1 == r3).all())

    sw.start()
    for _ in range(repeat):
        r2 = elementwise_multiply(A, B)
    sw.stop()
    print(f'Cython: {sw.getElapsedTime()} ms')
    print((r1 == r2).all())

    sw.start()
    for _ in range(repeat):
        r4 = elementwise_multiply_faster(A, B)
    sw.stop()
    print(f'Cython: {sw.getElapsedTime()} ms')
    print((r1 == r4).all())
