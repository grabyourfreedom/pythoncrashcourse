# Let us read line by line
name = input("Please enter your name: ")
with open("guest.txt", "w") as file_object:
    file_object.write(name)

