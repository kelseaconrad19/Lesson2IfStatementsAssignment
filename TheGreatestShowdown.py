# Task 1: Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
num_3 = int(input("Please enter another number: "))

# Assume num_1 is both the largest and smallest initially
largest = num_1

# Find the largest number
if num_2 > largest:
    largest = num_2
if num_3 > largest:
    largest = num_3
print(largest)

# Task 2: Extend your program from Task 1 to also determine the smallest number among the three and print it out.
smallest = num_1
# Find the smallest number
if num_2 < smallest:
    smallest = num_2
if num_3 < smallest:
    smallest = num_3
print(smallest)

# Task 3: Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".
if num_1 == num_2 and num_1 == num_3:
    print("All numbers are equal.")
if num_1 == num_2 or num_1 == num_3:
    print(f"The smallest number is {smallest}. The Largest number is {largest}. There are two numbers equal to each other.")
