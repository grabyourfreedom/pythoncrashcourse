# Prints your favorite number

favorite_numbers = {'guru': [1, 3, 5],
                    'ravi': [2, 4, 6],
                    'krishna': [3, 6, 9],
                    'viswa': [4, 8, 12],
                    'rama': [5, 10, 15, 20]
                    }

for key, value in favorite_numbers.items():
    print(key.title() + "'s favorite number is: ")
    for number in value:
        print("\t" + str(number))
