import sys

def isprime(n):
   for x in xrange(2,int(n ** 0.5) + 1):
      if not n % x:
         return False
   return True    


def largest_prime_factor(n):
   if isprime(n):
      return n
   
   for x in reversed(xrange(2,int(n ** 0.5 + 1))):
      if not n % x:
         return max(largest_prime_factor(n/x), largest_prime_factor(x))

 
if  __name__ == "__main__":
   print largest_prime_factor(sys.maxint/10000)