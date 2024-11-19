"""Debug testing"""

def titlize(sentence):
    """Capitalize words in a sentence that are longer than 2 characters."""
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
            new_words.append(word)
        else:
            new_words.append(word)

    return ' '.join(new_words)

TITLE = 'hello world of programming'
print(titlize(TITLE))
