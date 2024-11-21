# loops
# # Write a Python program that prints all even numbers between 1 and 20 using a for loop.
for num in range(2,21,2):
    print(num)

# Use a while loop to ask the user to input a number until
#  they provide a number greater than 10.
num=0
while num <= 10:
    num=int(input("enter the number greater than 10: "))
    if num <= 10:
     print("the number is not greater than 10")

#  Write a program that prints the multiplication table (from 1 to 10)
#  for numbers from 1 to 5 using nested for loops.

# Outer loop for numbers from 1 to 5
for i in range(1, 6):
    print(f"Multiplication table for {i}:")
    # Inner loop for multiplication from 1 to 10
    for n in range(1, 11):
        print(f"{i} x {n} = {i * n}")
    print()  # Blank line for better readability

# : Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using 
# a for loop to find the sum of all odd numbers and print the result.
integers = [4,7,2,9,12,15]
odd_sum = 0
for num in integers:
    if num % 2 != 0:
     odd_sum += num
print("Sum of odd numbers:", odd_sum)