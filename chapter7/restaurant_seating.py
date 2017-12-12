# Restaurant Seating App

message = input("How many people are there in your dinner group: ")
count = int(message)

if count > 8:
    print("Please wait for sometime while I find a big table")
else:
    print("Table is available")