import sys
import random

l = []
for i in xrange(100, 1000002, 1):
    l.append(i)

random.shuffle(l)      

with open("unsorted_ints.data", "wb") as fh:
    for i in l:
        fh.write(str(i)+"\n")
        
print("done")        