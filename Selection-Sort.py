from random import randint
#Initializing a list of 100 Random numbers
numbers = [randint(-100, 100) for value in range(1,10)]

#Sort itself. It is one of the most simple ones
#Complexity: O(n^2)
    
sorted_numbers = [] #soon-to-be sorted list
maxint = float('-inf')

for turn in range (0, len(numbers)):
    for number in numbers:
        if number > maxint:
            maxint = number
    sorted_numbers.append(maxint)
    numbers.remove(maxint)
    maxint = float('-inf')
    
print("Descending Order:")
print(sorted_numbers) 
sorted_numbers.reverse()
print("\nAscending Order:")
print(sorted_numbers) 
