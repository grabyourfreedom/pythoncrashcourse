# These are the places i want to visit in a list
places = ['kashi', 'rameshwaram', 'prayag', 'ahobilam', 'mathura', 'madurai']

# Printing them
print(places)

# Let's get a list that is sorted, print both the lists to show you they
# are different
print("\n")
print(sorted(places))
print(places)
print("\n")

# This time in the reverse order
print("\n")
print(sorted(places, reverse=True))
print(places)
print("\n")

# Let's reverse the list, printing them before and after
places = ['kashi', 'rameshwaram', 'prayag', 'ahobilam', 'mathura', 'madurai']
print(places)
places.reverse()
print(places)

# Reverse another time so that it becomes in original order
places.reverse()
print(places)

# Now, let us sort
places.sort()
print(places)

# Let's us sort in reverse order too
places.sort(reverse=True)
print(places)
