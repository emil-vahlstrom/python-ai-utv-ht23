from util import find_all
from service import fetch_words
from word import Word


def ask_for_digit():
    while True:
        amount = input("How many words to you want (1-10) >>> ")
        if amount.isnumeric() and int(amount) >= 1 and int(amount) <= 10:
            return int(amount)


def ask_for_character(prompt: str):
    while True:
        word = input(prompt).lower()
        if word.__len__() == 1:
            return word


number_of_words = ask_for_digit()

# Fetch words from API
words = [Word(word_from_api) for word_from_api in fetch_words(number_of_words)]

retries_left = 8
unfinished_words = len(words)

already_used = set()
while retries_left > 0 and unfinished_words > 0:
    print(f"\nWords to solve({retries_left} retries left): ")
    for word in words:
        print("-", word.hidden_word)

    # Ask for input
    while True:
        already_used_formatted = f"(already_used: {', '.join(already_used)})" if len(already_used) > 0 else '' 
        prompt = f"Enter a single character{already_used_formatted} >>> "
        char = ask_for_character(prompt)
        if char in already_used:
            print("Letter already exists")
        elif char not in already_used:
            already_used.add(char)
            break

    letter_was_found = False

    # Check the words if there's a match and if so unmask the hidden letter
    for word in words:
        if word.hidden_word.find("*") == -1:
            continue
        result = find_all(word.public_word, char)

        if (len(result) > 0):
            letter_was_found = True

        hidden_word_list = list(word.hidden_word)

        for index in result:
            hidden_word_list[index] = word.public_word[index]
        word.hidden_word = "".join(hidden_word_list)
        
        if word.hidden_word.find("*") == -1:
            unfinished_words -= 1
    if letter_was_found != True:
        retries_left -= 1

the_words_are = {", ".join([word.public_word for word in words])}
print(f'\n{"YOU WIN!" if retries_left > 0 else "YOU LOSE!"} The words are: {the_words_are}')
