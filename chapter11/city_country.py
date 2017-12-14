def display_city(city, country, population=0):
    city = city.strip()
    country = country.strip()
    formatted_string = city.title() + ", " + country.title()

    if population > 0:
        formatted_string += " - population=" + str(population)

    return formatted_string
