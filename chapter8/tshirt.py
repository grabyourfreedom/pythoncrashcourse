# Given the size and message to be printed, this function prints
# the T-Shirt


def make_shirt(size="L", message="i love python"):
    print("Size : " + str(size).upper())
    print("Message: " + message.title())
    return


make_shirt("XL", "Go kiss the world")
make_shirt("XXL", "live life king size")
make_shirt(message="less is more", size="xxxl")

# T-Shirt with large and default message
make_shirt()

# T-Shirt with medium and default message
make_shirt(size="m")

# T-Shirt with large and default message
make_shirt("XL", "python is sexy")