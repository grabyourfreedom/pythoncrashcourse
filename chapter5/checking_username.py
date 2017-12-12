# A simple program that performs username validation
current_users = ['admin', 'stranger', 'wanderer', 'visitor', 'owner']
new_users = ['caretaker', 'stranger', 'tenant', 'plumber', 'OWNER']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " is not available. You need to enter a new "
                         "username")
    else:
        print(new_user + " is available. Your registration is accepted")
