# Some more conditions with lists

first = "Hello"
second = "hello"
hello = "Hello"

print(first == hello)
print(second == hello)
print(first.lower() == second.lower())

# Let us play with numbers
print("Numerical tests")
print(2 > 3)
print(2 < 3)
print(2 <= 3)
print(3 >= 2)

# Clubbing conditions with and & or
print(first.lower() == second and 2 < 3)
print(first.lower() == second or 5 < 3)

# List of numbers and some condition tests on list.
numbers = [1, 2, 3, 4, 5, 6]

print(10 in numbers)
print(1 in numbers)
print(10 not in numbers)
print(1 not in numbers)
