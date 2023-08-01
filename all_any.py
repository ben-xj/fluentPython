# %%
a = [1,2,3,4,5]

# %%
# all
def all_greater_than_2(arr):
    for i in arr:
        if i <= 2:
            return False
    return True

print(all_greater_than_2(a))

def all_greater_than_2_simple(arr):
    return all(i > 2 for i in arr)

print(all_greater_than_2(a))

# %%
# any
def any_greater_than_2(arr):
    for i in arr:
        if i > 2:
            return True
    return False

print(any_greater_than_2(a))

def any_greater_than_2_simple(arr):
    return any(i > 2 for i in arr)

print(any_greater_than_2_simple(a))

# %%
# benchmark
from stopwatch import StopWatch
import random

arr = [random.randint(1,10) for _ in range(100_000)]
repeat = 1000_000
sw = StopWatch()

# %%
# all comparison

sw.start()
for i in range(repeat):
    all_greater_than_2_simple(arr)
sw.stop()
print("`all` keyword time:", sw.getElapsedTime())

sw.start()
for i in range(repeat):
    all_greater_than_2(arr)
sw.stop()
print("for-loop time:", sw.getElapsedTime())

# %%
# any comparison

sw.start()
for i in range(repeat):
    any_greater_than_2_simple(arr)
sw.stop()
print("`any` keyword time:", sw.getElapsedTime())

sw.start()
for i in range(repeat):
    any_greater_than_2(arr)
sw.stop()
print("for-loop time:", sw.getElapsedTime())

# %%
print('########  new comparison  ##########')

# %%
# new all comparison
arr = [True, True, True, True, True, True, False, True, True, True]
sw.start()
for i in range(repeat):
    all(arr)
sw.stop()
print("`all` keyword time:", sw.getElapsedTime())

sw.start()
for i in range(repeat):
    for i in arr:
        if not i:
            break
sw.stop()
print("for-loop time:", sw.getElapsedTime())

# %%
# new any comparison
arr = [False, False, False, False, False, False, False, False, False, True]
sw.start()
for i in range(repeat):
    any(arr)
sw.stop()
print("`any` keyword time:", sw.getElapsedTime())

sw.start()
for i in range(repeat):
    for i in arr:
        if i:
            break
sw.stop()
print("for-loop time:", sw.getElapsedTime())
# %%
