# Let us read entire contents
with open("learning_python.txt") as file_object:
    contents = file_object.read()
    print(contents)

# Let us print using list
with open("learning_python.txt") as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

# Let us read line by line
with open("learning_python.txt") as file_object:
    for line in file_object:
        print(line)
