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


def generator():
    letter = string.ascii_lowercase
    vowels = 'aeiou'
    consonants =  'bcdfghjklmnpqrstvwyxz'

    # user input
    letter_input1 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')
    letter_input2 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')
    letter_input3 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')
    letter_input4 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')
    letter_input5 = input('Choose a letter \n\t"v" for vowels,\n\t"c" for constants ,\n\t"l" for any other letter\n')

    # conditional logic
    # user choice:

    # letter 1
    # user choice:vowel
    if letter_input1 == 'v':
        letter1 = random.choice(vowels)
        # user choice:consonant
    elif letter_input1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input1 == 'l':
        # user choice:letter
        letter1 = random.choice(letter)
    else:
        # user choice: user specified
        letter1 = letter_input1
    # letter 2
    if letter_input2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input2 == 'l':
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input2

    # letter 3
    if letter_input3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_input3 == 'l':
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input3
    # letter 4
    if letter_input4 == 'v':
        letter4 = random.choice(vowels)
    elif letter_input4 == 'c':
        letter4 = random.choice(consonants)
    elif letter_input4 == 'l':
        letter4 = random.choice(letter)
    else:
        letter4 = letter_input4
    # letter 5
    if letter_input5 == 'v':
        letter5 = random.choice(vowels)
    elif letter_input5 == 'c':
        letter5 = random.choice(consonants)
    elif letter_input5 == 'l':
        letter5 = random.choice(letter)
    else:
        letter5 = letter_input4

    name = letter1 + letter2 +letter3 + letter4 + letter5
    return(name)

print(generator())
