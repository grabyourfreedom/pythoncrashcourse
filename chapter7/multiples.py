# Program checks whether user input is multiple of ten

message = input("Enter a number: ")
number = int(message)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10")
else:
    print(str(number) + " is not a multiple of 10")