from collections import OrderedDict
# A program to demonstrate ordereddict

glossary = OrderedDict()
glossary['if'] = "Keyword that tests a condition and executes the block of code underneath"
glossary['else'] = "Keyword that gets executed when the if condition evaluates to false"
glossary['elif'] = "Keyword that evaluated another condition when an if block fails"
glossary['break'] = 'Keyword used to break or come out of a loop'
glossary['continue'] = 'Keyword used to skip the execution of the current iteration'

for key, value in glossary.items():
    print(key + ":")
    print("\t" + value)
