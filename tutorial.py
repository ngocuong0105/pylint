'''
Pylint tutorial.
'''
import string

SHIFT = 3
choice = input("would you like to encode or decode?")
word = input("Please enter text")
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if choice == "encode":
    for letter in word:
        if letter == ' ':
            ENCODED = ENCODED + ' '
        else:
            X = LETTERS.index(letter) + SHIFT
            ENCODED = ENCODED + LETTERS[X]
if choice == "decode":
    for letter in word:
        if letter == ' ':
            ENCODED = ENCODED + ' '
        else:
            X = LETTERS.index(letter) - SHIFT
            ENCODED = ENCODED + LETTERS[X]

print(ENCODED)

# Pylint is telling me that those variables appear to be constants and should be all UPPERCASE.
