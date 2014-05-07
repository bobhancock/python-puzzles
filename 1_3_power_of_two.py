#def is_power_of_2(x):
   #while x > 1 and (x % 2 == 0):
      #x = x//2
   #return (x == 1)

import math
def is_power_of_2(x):
   return not (math.log(x, 2) % 1) 

def power2(x):
   """ Get the binary repr of the number as a string
   0b1001 for example.
   Take the slice that represents the number, and if
   the most significant digit is one and the rest are zero, it
   is a power of two.
   """
   s = bin(x)[2:]  # binary repr as a string
   return s[0] == "1" and s[1:] == "0"*len(s[1:])
   

def is_pow_of_2(n):
    return n & (n - 1)  == 0
   
i = 1
for line in open("data/1_3.data"):
   n = int(line.strip("\n"))
   print("{} {}".format(i, is_power_of_2(n)))
   i += 1
   
