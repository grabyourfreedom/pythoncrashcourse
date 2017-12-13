# A program to show off how cool the functions are


def describe_city(name, country="india"):
    print(name.title() + " is in " + country.title())
    return


describe_city("chennai")
describe_city("delhi")
describe_city("boston", "united states")
describe_city(country="united states", name="san jose")
