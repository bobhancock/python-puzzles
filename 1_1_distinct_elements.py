i = 1
for line in open("data/1_1.data", "r"):
    buf = line.strip("\n").split("|")
    if len(set(buf)) == len(buf):
        print(str(i)+" True")
    else:
        print("{} False".format(i))
    i += 1
        
    