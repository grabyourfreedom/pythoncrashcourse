# A list that holds the numbers between zero and one million
million = [value for value in range(0, 1000001)]

# Some short cut math
print(min(million))
print(max(million))
print(sum(million))

# List of all odd numbers between 1 and 20
odd = [value for value in range(1, 20, 2)]
print(odd)

# Multiples of 3 between 0 and 31
multiples = [value for value in range(0, 31, 3)]
for multiple in multiples:
    print(multiple)

# Printing cubes of numbers between 1 and 11
for num in range(1, 11):
    print(num ** 3)

# A list that holds the cubes of numbers from 0 to 10
cubes = [num ** 3 for num in range(0, 11)]
print(cubes)
