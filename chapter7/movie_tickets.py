# Ticket fee calculator

msg = input("Enter your age: ")
age = int(msg)

if age < 3:
    print("No fee")
elif age <= 12:
    print("$10")
elif age > 12:
    print("$15")