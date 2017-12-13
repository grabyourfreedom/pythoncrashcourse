# A program to build a car with special features


def build_car(manufacturer, model, **features):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in features.items():
        car[key] = str(value).title()
    return car


car = build_car("Fiat", "Linea", gears=5, assistance="Road Side Assistance")
print(car)

car = build_car("Maruti", "Swift", gears=5, insurance="Free bumper to bumper")
print(car)