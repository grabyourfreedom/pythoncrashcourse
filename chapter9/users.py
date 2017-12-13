# Another example class


class User:
    def __init__(self, first_name, last_name, age, city, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print("First Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("City Lives in: " + self.city.title())
        print("Hobby: " + self.hobby.title())
        print("Login Attempts: " + str(self.login_attempts))
        print()

    def greet_user(self):
        print("Hi " + self.first_name.title() + ", Welcome to User App")
        print()

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Lakshmi", "Narayanan", 38, "Chennai", "Coding")
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()
user.reset_login_attempts()
user.describe_user()

