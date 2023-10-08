def find_all(word, sub):
    """
    Finds all occurences of a subsequence in a word

    Parameters:
        word (string): The word to search in
        sub (string): The subsequence to look for in {word}

    Returns:
        list: A list of indexes matching the subsequence
    """
    list = []
    index = 0
    while index != -1:
        index = word.find(sub, index)
        if (index > -1):
            list.append(index)
            index+=1
        else:
            break
    return list

def trace(msg):
    print(msg)