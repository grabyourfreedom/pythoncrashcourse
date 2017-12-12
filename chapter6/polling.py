# list of people who should respond to poll
respondants = ['jack', 'jill', 'john', 'tom', 'jeo', 'dave', 'chuck', 'edward', 'phil']

# people who have responded to the poll with their response
favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python',
                      }

# A thank you note or an invitation to take part in survey
for respondant in respondants:
    if respondant.lower() in favorite_languages.keys():
        print("Thank you for responding to the poll")
    else:
        print("Invite you to take the poll on your favorite programming language")
