# fib.pyx
cimport cython

def fib(long n):
    if n < 2:
        return n
    cdef:
        long a = 0
        long b = 1
        long c, i
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b

cdef cfib(long n):
    if n < 2:
        return n
    cdef:
        long a = 0
        long b = 1
        long c, i
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b

cpdef cpfib(long n):
    if n < 2:
        return n
    cdef:
        long a = 0
        long b = 1
        long c, i
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b

def cfib_test(repeat):
    for _ in range(repeat):
        cfib(100)