# Find the count of given word in a sentence

try:
    with open("text.txt") as text_object:
        lines = text_object.readlines()
except FileNotFoundError:
    print("File not found")
else:
    count = 0
    for line in lines:
        count += line.lower().count("the")

print(str(count))
