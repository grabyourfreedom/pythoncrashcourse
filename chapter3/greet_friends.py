# A list, a greeting and a message
friends = ["john", "steve", "shiv", "krishna", "kesava", "rishi", "akshara"]
msg_hello = "Hello "
msg_greet = ", Welcome to the world of Python!!!"

# Let us do some processing when looping through a list
for friend in friends:
    greetings = msg_hello + friend.title() + msg_greet
    print(greetings)
