# Let us implement a guest book
with open("guest_book.txt", "w") as file_object:
    can_quit = False
    while not can_quit:
        msg = input("Enter your name or type quit to exit: ")
        if msg == 'quit':
            can_quit = True
            break
        file_object.write(msg + "\n")
