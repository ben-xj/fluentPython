from util.stopwatch import StopWatch
from acceleration.fib import fib, cpfib, cfib_test
# from acceleration.fib import cfib

sw = StopWatch()
repeat = 1000000

sw.start()
for _ in range(repeat):
    fib(100)
sw.stop()
print(f'def: {sw.getElapsedTime()} ms')


sw.start()
for _ in range(repeat):
    cpfib(100)
sw.stop()
print(f'cpdef: {sw.getElapsedTime()} ms')

# print(cfib(3))
sw.start()
cfib_test(repeat)
sw.stop()
print(f'cdef: {sw.getElapsedTime()} ms')
