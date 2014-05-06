import random

with open("/local/src/python_puzzles/data/2_8.data", "wb") as fh:
    for i in xrange(1000000):
        fh.write( str(random.random()) + "\n")
    
    
    