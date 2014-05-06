import itertools

it = [2,4,8,10,12,14,16,18,19,20,22,24]

def even(i):
    return not i % 2

x = itertools.takewhile(even, it)

for e in x:
    print(e)