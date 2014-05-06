import heapq

l = []
with open("1_12.data", "rb") as fh:
    for line in fh:
        l.append(int(line.strip("\n")))
        
heapq.heapify(l)
print(heapq.nsmallest(3, l))