from util.stopwatch import StopWatch

# literal
alist = [1,2,3,4]
atuple = (1,2,3,4)
adict = {'a':1, 'b':2, 'c':3, 'd':4}
aset = {1,2,3,4}

# 列表推导式
a_new_list_ugly = []
for i in alist:
    a_new_list_ugly.append(i**2)

print(f'a_new_list_ugly: {a_new_list_ugly}')

a_new_list = [i**2 for i in alist]
print(f'a_new_list: {a_new_list}')

# 元组推导式
a_new_tuple = tuple(i**2 for i in atuple)
print(f'a_new_tuple: {a_new_tuple}')

# 生成器
a_generator = (i**2 for i in atuple)
print(f'a_generator: {a_generator}')

# 字典推导式
a_new_dict = {k:v**2 for k,v in adict.items()}
print(f'a_new_dict: {a_new_dict}')

# 集合推导式
def f(x):
    return x**2 + 2*x + 1

a_new_set = {f(i) for i in aset}
print(f'a_new_set: {a_new_set}')


# benchmark
alist = list(range(100))
stopwatch = StopWatch()
for i in range(100_000):
    a_new_list_ugly = []
    for i in alist:
        a_new_list_ugly.append(i**2)
stopwatch.stop()
print(f'a_new_list_ugly: {stopwatch.getElapsedTime()} ms')

stopwatch.start()
for i in range(100_000):
    a_new_list = [i**2 for i in alist]
stopwatch.stop()
print(f'a_new_list: {stopwatch.getElapsedTime()} ms')