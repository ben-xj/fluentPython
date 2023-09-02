import numpy as np
cimport numpy as cnp

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
