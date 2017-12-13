class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name: " + self.restaurant_name)
        print("Cuisine: " + self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is opened")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        if self.flavors:
            print("Flavors in stock:")
            for flavor in self.flavors:
                print("\t" + flavor.title())
        else:
            print("Sold Out")


ice_cream_stand = IceCreamStand("IBaco", "Indian", ['vanila', 'mango', 'jacfruit'])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

