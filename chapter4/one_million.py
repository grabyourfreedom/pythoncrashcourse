million = [value for value in range(0, 1000001)]

print(min(million))
print(max(million))
print(sum(million))

odd = [value for value in range(1, 20, 2)]
print(odd)

multiples = [value for value in range(0, 31, 3)]
for multiple in multiples:
    print(multiple)

for num in range(1, 11):
    print(num ** 3)

cubes = [num ** 3 for num in range(0, 11)]
print(cubes)