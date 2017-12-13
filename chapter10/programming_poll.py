# Let us implement a programming poll
with open("programming_polls.txt", "w") as file_object:
    can_quit = False
    while not can_quit:
        msg = input("Why do you like programming: ")
        if msg == 'quit':
            can_quit = True
            break
        file_object.write(msg + "\n")
