def ask_for_digit():
    while True:
        amount = input("How many words to you want (0-10) >>> ")
        if amount.isnumeric() and int(amount) >= 0 and int(amount) <= 10:
            return int(amount)


def ask_for_character():
    while True:
        word = input("Enter a single character >>> ").lower()
        if word.__len__() == 1:
            return word
