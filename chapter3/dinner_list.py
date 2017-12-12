# List of friends that i would like to invite for a dinner
friends = ['kuyil', 'abbas', 'bala', 'paneer']

# Here goes the invitation
for friend in friends:
    print("Hi " + friend.title() + ", I invite you for dinner")

# One of them cannot make to the dinner
print(friends[-1].title() + " cannot make to the dinner\n")
del friends[-1]
# Let us invite another friend
friends.append("nirmal")

# Let us invite them all
for friend in friends:
    print("Hi " + friend.title() + ", I invite you for dinner")

# We have got a BIG table, time to add more friends.
print("Guys, we got a BIGGER table. Let us party\n")

# Add three folks
friends.insert(0, "john")
friends.insert(int(len(friends)/2), "rob")
friends.append("dave")

# Send invitation all over again, so that no one is missed
for friend in friends:
    print("Hi " + friend.title() + ", I invite you for dinner")

# Hotel says BIG table is not yet available
print("Sorry guys, it is going to be late for the bigger table to arrive" +
      ". Will let you know once i can accommodate you.")

# Remove all but two friends with whom i will have dinner, Sorry guys
length = len(friends)
number_removed = length - 2

# Send them a note
while number_removed > 0:
    number_removed -= 1
    print(friends.pop(-1).title() + ", Sorry, will buzz you when table is available")

# Dinner with two the friends
for friend in friends:
    print(friend.title() + ", let's have dinner")

# Remove them from the list as they had dinner
del friends[-1]
del friends[-1]

# Print the list (which should be empty now)
print(friends)
