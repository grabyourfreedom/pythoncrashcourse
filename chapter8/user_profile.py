# A function that prints user information
def build_profile(first_name, last_name, **info):
    print("First Name: " + first_name.title())
    print("Last Name: " + last_name.title())
    for key, value in info.items():
        print(key.title() + ": " + str(value).title())

    return


build_profile('lakshmi narayanan', 'narasimhan', age=38, passion='coding', city='chennai')
build_profile('rama narayanan', 'govindan', age=70, passion='travel', city='madurai')