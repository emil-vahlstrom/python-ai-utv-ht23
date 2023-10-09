class Word:
    """
    A word, public or masked
    """

    def __init__(self, public_word: str):
        self.public_word = public_word
        self.hidden_word = ("*" * len(public_word))

    def __repr__(self):
        return f'Word(public_word={self.public_word}, hidden_word={self.hidden_word})'

    def __str__(self):
        return self.hidden_word
