import itertools

def it():
    for line in open("/local/src/python_puzzles/data/2_8.data", "r"):
        yield line.strip("\n")
        
iter = it()        
for elem in itertools.islice(iter, 0, None,100101):
    print(elem)