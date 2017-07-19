#Addition of numbers in list recursively
def summ(arr, total):
    if len(arr) > 1: #recursive case
        total += arr[0]
        del arr[0]
        total = summ(arr, total)
        return total
    elif len(arr) == 1: #base case
        return arr[0]+total
    else: #base case(2)
        return 0


from random import randint

#Initializing the list by appending to an empty list
#10 Random numbers
numbers = []

for value in range (0, 10):
    numbers.append(randint(1, 10))

print(numbers)
print(sum(numbers)) #to compare with default sum function
print(summ(numbers, 0)) #my recursive addition function