from random import randint #for choosing pivot

def quick_sort(arr): #classic quick sort, Complexity: O(n * log(n))
    if len(arr) > 1:
        pivot = arr[randint(0,len(arr)-1)]
        
        #array with values <= pivot :
        less = [i for i in arr[:] if i <= pivot] 
        less.remove(pivot)#removing pivot from the lesser array        
        
        #array with values > pivot :
        greater = [i for i in arr[:] if i > pivot]
        
        #sorting in ascending order :
        return quick_sort(less) + [pivot] + quick_sort(greater)        
    else:
        return(arr)
    
print(quick_sort([randint(-100, 100) for value in range(1,10)]))