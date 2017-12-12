# A simple demo of dictionaries in a list

person1 = {'first_name': "lakshmi", "last_name": "narasimhan",
           'age': 38, 'city': "chennai"}
person2 = {'first_name': "john", "last_name": "george",
           'age': 38, 'city': "atlanta"}
person3 = {'first_name': "narayanan", "last_name": "kesavan",
           'age': 38, 'city': "madurai"}

persons = [person1, person2, person3]

for person in persons:
    print("First Name: " + person['first_name'].title())
    print("Last Name: " + person['last_name'].title())
    print("Age: " + str(person['age']))
    print("City: " + person['city'].title())
    print("\n")