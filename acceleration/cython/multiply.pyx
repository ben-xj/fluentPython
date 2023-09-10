import numpy as np
cimport numpy as cnp
from cython import boundscheck, wraparound

cpdef cnp.ndarray[double, ndim=2] elementwise_multiply(
        cnp.ndarray[double, ndim=2] A,
        cnp.ndarray[double, ndim=2] B):
    cdef int nrows = A.shape[0]
    cdef int ncols = A.shape[1]
    cdef cnp.ndarray[double, ndim=2] result = np.zeros((nrows, ncols), dtype=np.float64)

    cdef int i, j
    for i in range(nrows):
        for j in range(ncols):
            result[i, j] = A[i, j] * B[i, j]

    return result

@boundscheck(False)
@wraparound(False)
def elementwise_multiply_faster(
        cnp.ndarray[double, ndim=2] A,
        cnp.ndarray[double, ndim=2] B):
    cdef:
        int nrows = A.shape[0]
        int ncols = A.shape[1]
        cnp.ndarray[double, ndim=2] result = np.zeros((nrows, ncols), dtype=np.float64)
        int i, j
    for i in range(nrows):
        for j in range(ncols):
            result[i, j] = A[i, j] * B[i, j]

    return result



@boundscheck(False)
@wraparound(False)
def elementwise_multiply_even_faster(
        double[:, :] A,
        double[:, :] B):
    cdef:
        int nrows = A.shape[0]
        int ncols = A.shape[1]
        cnp.ndarray[double, ndim=2] result = np.zeros((nrows, ncols), dtype=np.float64)
        int i, j
    for i in range(nrows):
        for j in range(ncols):
            result[i, j] = A[i, j] * B[i, j]

    return result
