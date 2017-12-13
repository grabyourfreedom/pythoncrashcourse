# A program that prints city name with its country neatly
def city_country(city, country):
    print(city.title() + ", " + country.title())
    return


city_country("chennai", "India")
city_country(country="United states", city="boston")
city_country("karachi", "pakistan")