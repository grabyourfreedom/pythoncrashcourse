# Program to demonstrate JSON

from json import dump
from json import load

msg = input("Enter your favorite number: ")
number = int(msg)
with open("number.json", "w") as json_file:
    dump(number, json_file)

with open("number.json") as json_file:
    number = load(json_file)
    print(str(number))
