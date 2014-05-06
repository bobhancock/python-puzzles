# Give an unsorted iterable of integers, if there are two unique elements of the 
# iterable, a and b, that sum to m then return True, else False.
def is_sum(m, iter):
    iter.sort() # O(n log n)
    i = 0
    j = len(iter) - 1
    
    # limits
    if m < iter[0] or m > iter[-1] + iter[-2]:
        return False

    while i < j:
        if iter[i] + iter[j] == m:
            break
        
        if m < iter[i] + iter[j]:
            j -= 1
        else:
            i += 1
                       
    return i != j    
        
l =  [1,2,3,5,7,10, 19, 23, 30]  
r = is_sum(60, l)
print(r)
    
    
    