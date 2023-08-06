def get_words(filename):
    with open(filename, encoding="utf-8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("”", "").replace("“", "")
    text = text.replace(":", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def words_into_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def count_words(filename):
    words = get_words(filename)
    count_word = len(words)
    return count_word


def count_unique_words(filename):
    words = get_words(filename)
    words_dict = words_into_dict(words)
    count_unique = len(words_dict)
    return count_unique


def all_words(filename):
    words = get_words(filename)
    words_dict = words_into_dict(words)
    return words_dict
