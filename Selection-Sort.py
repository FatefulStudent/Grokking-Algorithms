from random import randint
#Initializing the list by appending to an empty list
#100 Random numbers
numbers = []
for value in range (0, 100):
    numbers.append(randint(1, 1000))

#Sort itself. It is one of the most simple ones
#Complexity: O(n^2)
    
sorted_numbers = [] #soon-to-be sorted list
maxint = 0 

for turn in range (0, len(numbers)):
    for number in numbers:
        if number > maxint:
            maxint = number
    sorted_numbers.append(maxint)
    numbers.remove(maxint)
    maxint = 0
    
print("Descending Order:")
print(sorted_numbers) 
sorted_numbers.reverse()
print("\nAscending Order:")
print(sorted_numbers) 