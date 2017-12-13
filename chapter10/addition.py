# Program to demonstrate exceptions

first_number = input("Enter Number 1: ")
second_number = input("Enter Number 2: ")
try:
    first_number = int(first_number)
    second_number = int(second_number)
    addition = first_number + second_number
except ValueError:
    print("Please enter numbers")