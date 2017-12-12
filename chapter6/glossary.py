# Program that uses dictionary and implements a simple glossary

glossary = {'if': "Keyword that tests a condition and executes the block of code underneath",
            'else': "Keyword that gets executed when the if condition evaluates to false",
            'elif': "Keyword that evaluated another condition when an if block fails",
            'break': 'Keyword used to break or come out of a loop',
            'continue': 'Keyword used to skip the execution of the current iteration'}

for key, value in glossary.items():
    print(key + ":")
    print("\t" + value)