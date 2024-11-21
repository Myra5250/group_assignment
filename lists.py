 # lists
# #Create a list of 5 fruits and print each fruit on a new line using a for loop.
fruits = ["apple", "banana", "peach", "orange", "pear"]
for f in fruits:
   print(f)

# Write a function that takes a list of numbers and returns a new list with each number
#  squared. Example: [1, 2, 3] should become [1, 4, 9].
def squared_numbers(numbers):
   return [n ** 2 for n in numbers]
numbers = [1,2,3]
square_numbers = squared_numbers(numbers)
print(square_numbers)

# Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6],
#  and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find 
# and print the two largest numbers in the list without using the max() function.
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort(reverse= True)
largest = numbers[0]
second_largest = numbers[1]
print(numbers)
print("The largest number is",largest)
print("The second largest number is",second_largest)