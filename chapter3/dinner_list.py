friends = ['kuyil', 'abbas', 'bala', 'paneer']

for friend in friends:
    print("Hi " + friend.title() + ", I invite you for dinner")

print(friends[-1].title() + " cannot make to the dinner\n")
del friends[-1]
friends.append("nirmal")

for friend in friends:
    print("Hi " + friend.title() + ", I invite you for dinner")

print("Guys, we got a BIGGER table. Let us party\n")

friends.insert(0, "john")
friends.insert(int(len(friends)/2), "rob")
friends.append("dave")

for friend in friends:
    print("Hi " + friend.title() + ", I invite you for dinner")

print("Sorry guys, it is going to be late for the bigger table to arrive" +
      ". Will let you know once i can accommodate you.")

length = len(friends)
number_removed = length - 2

while number_removed > 0:
    number_removed -= 1
    print(friends.pop(-1).title() + ", Sorry, will buzz you when table is available")

for friend in friends:
    print(friend.title() + ", let's have dinner")

del friends[-1]
del friends[-1]

print(friends)