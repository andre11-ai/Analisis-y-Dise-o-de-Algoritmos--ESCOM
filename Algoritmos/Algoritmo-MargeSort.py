# Recursive Python Program for merge sort
import random
import time
def merge(left, right):    
    print(f'Merging {left} and {right}')    
    if not len(left) or not len(right):        
        return left or right    
    result = []    
    i, j = 0, 0    
    while (len(result) < len(left) + len(right)):        
        if left[i] < right[j]:            
            result.append(left[i])            
            i += 1        
        else:            
            result.append(right[j])            
            j += 1        
            if i == len(left) or j == len(right):            
                result.extend(left[i:] or right[j:])            
                break    
        print(f'Returning {result}')    
        return result
    def mergesort(list):    
        print(f'Enter in mergesort with {list}')    
        if len(list) < 2:        
            return list    
        
        middle = int(len(list) / 2)    
        left = mergesort(list[:middle])    
        right = mergesort(list[middle:])    
        #print(f'To merge {left} and {right}')    
        return merge(left, right)
        
    #seq = [12, 11, 13, 5, 6, 7]
    seq = list([random.randint(-1000,1000) 
                for x in range(0,10)])
    print("Given array is")
    print(seq)
    print("\n")
    #print("Sorted array is")
    start=time.time()
    sorted_array=mergesort(seq)
    end=time.time()
    print(f'sorted array is {sorted_array}')
    print(f'Sorting executed in {end-start} sec')
    # Code Contributed by Mohit Gupta_OMG