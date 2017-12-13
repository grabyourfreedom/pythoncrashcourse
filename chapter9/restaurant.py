# A simple program to demonstrate how to play with classes and objects


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name: " + self.restaurant_name)
        print("Cuisine: " + self.cuisine_type)
        print()

    def open_restaurant(self):
        print("Restaurant is opened")
        print()


# restaurant = Restaurant("Sri Durga Nivas", "Indian")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant = Restaurant("Ananda", "South Indian")
# restaurant.describe_restaurant()

# restaurant = Restaurant("Wangs", "Chinese")
# restaurant.describe_restaurant()

# restaurant = Restaurant("Data Udupi", "Karnataka")
# restaurant.describe_restaurant()