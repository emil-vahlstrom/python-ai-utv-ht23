from util import find_all
from input import ask_for_digit, ask_for_character
from service import fetch_words;

# # Documentation: https://random-word-api.herokuapp.com/home
# apiEndpoint = "https://random-word-api.herokuapp.com/word?number=10"


# print(f'Connecting this following endpoint: {apiEndpoint}')

# r = requests.get(apiEndpoint)
# print(f'status code: {r.status_code}')

# val = r.json()

# print(val)
# print(type(val))

# for entry in val:
#    print(f'entry: {entry}')

# name = input('Write your name >>> ')
# print(f'Hello {name}!')

# test = "AbcA"
# test_char = "A"

# print(test.find('A'))
# print(test.find('A', 4))

# retval = find_all(test, test_char)
# print(f'retval: {retval}')


# Hang men, how many words do you want?
# Error: not a number

# The words are:
# *******
# ****
# ***
# The letters you have already guessed: []
#
# Guess a letter:
#
# No match
# There's a match
# You have already chosen this letter, chose another one


# End game:
# out of 10 hangmen, 8 survived
# Try again? y/n
# go to: 36

# amount = input("How many words to you want? >>> ")

# print(amount)
# print(f'is number: {amount.isnumeric()}' )




#number=ask_for_digit()
#print(f'digit: {digit}')

# Documentation: https://random-word-api.herokuapp.com/home
apiEndpoint = "https://random-word-api.herokuapp.com/word?number=10"
number_of_words = 1
#words=fetch_words(number_of_words)

class Word:
    def __init__(self, public_word: str):
        self.public_word = public_word
        self.hidden_word = ("*" * len(public_word))
    
    def __repr__(self):
        return f'Word(public_word={self.public_word}, hidden_word={self.hidden_word})'

    def __str__(self):
        return self.hidden_word

#wordstr = words[0]
#word = Word(wordstr)

#print(f'word: {word}')
#print(f'repr(word): {repr(word)}')

visible_word = "blindfolding"
hidden_word = "************"
result=find_all(visible_word, "i")
#print(result)
#print(type(result))

# hidden_word_list=list(hidden_word)

#print(hidden_word_list)

# for index in result:
#     hidden_word_list[index] = visible_word[index]

# hidden_word = "".join(hidden_word_list)
#print(hidden_word)

#already_used = {'a'}
#print('a' in already_used)
#print('b' in already_used)
#already_used.add('b')
#print('b' in already_used)

retries_left=15

already_used=set()
while retries_left>0:
    print(f'hidden_word: {hidden_word}')
    print(f'retries left: {retries_left}')
    print(f'already_used: {already_used}')

    # Ask for input
    while True:
        char=ask_for_character()
        if char in already_used:
            print("Letter already exists")
        elif char not in already_used:
            already_used.add(char)
            break
    
    result=find_all(visible_word, char)
    print(result)
    if (len(result) == 0):
        retries_left-=1

    hidden_word_list=list(hidden_word)

    for index in result:
        hidden_word_list[index] = visible_word[index]
    hidden_word = "".join(hidden_word_list)
    if (hidden_word.find("*")==-1):
        break

if (retries_left > 0):
    print(f'YOU WIN! The word is {visible_word}')
else:
    print("YOU LOSE!")