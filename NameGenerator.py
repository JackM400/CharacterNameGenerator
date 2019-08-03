import string

print(help(string))
print(string.ascii_letters)
print(string.ascii_lowercase)

import random

print(random.choice('pull a char from here'))
print(random.choice(string.ascii_lowercase + '-'))


def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)
    letter6 = random.choice(string.ascii_lowercase)
    name1 = letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    return(name)


print(generator())
