from json import dump
from json import load
from json.decoder import JSONDecodeError

is_number_available = False
try:
    with open("number.json") as json_file:
        number = load(json_file)
        is_number_available = True
except FileNotFoundError:
    print("File not found")
except JSONDecodeError:
    print("Value not format error")

if is_number_available:
    print("your favorite number is: " + str(number))
else:
    msg = input("Enter your favorite number: ")
    number = int(msg)
    with open("number.json", "w") as json_file:
        dump(number, json_file)
