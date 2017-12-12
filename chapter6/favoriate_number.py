# Prints your favorite number

favorite_numbers = {'guru': 1,
                    'ravi': 2,
                    'krishna': 3,
                    'viswa': 4,
                    'rama': 5}
for key, value in favorite_numbers.items():
    print(key.title() + "'s favorite number is: " + str(value))
    