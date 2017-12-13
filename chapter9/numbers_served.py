# A simple program to demonstrate how to play with classes and
# objects with more features to our previous program


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant Name: " + self.restaurant_name)
        print("Cuisine: " + self.cuisine_type)
        print("Total served: " + str(self.number_served))

    def open_restaurant(self):
        print("Restaurant is opened")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_server(self, number):
        self.number_served += number

restaurant = Restaurant("Sri Durga Nivas", "Indian")
restaurant.set_number_served(100000)
restaurant.increment_number_server(100)
restaurant.describe_restaurant()
