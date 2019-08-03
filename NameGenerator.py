import string

print(help(string))
# print(string.ascii_letters)
# print(string.ascii_lowercase)

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
    name = letter1 + letter2 + letter3 + letter4 + letter5 + letter6
    return (name)


print(generator())
letter = string.ascii_lowercase
vowels = 'aeiou'
consonants = string.ascii_lowercase - vowels

# user input
letter_input1 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')
letter_input2 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')
letter_input3 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')
letter_input4 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')
letter_input5 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')

# conditional logic

