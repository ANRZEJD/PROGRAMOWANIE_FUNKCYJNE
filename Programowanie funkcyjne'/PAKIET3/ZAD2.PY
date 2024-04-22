def filter_long_words(words):
    average_length = sum(len(word) for word in words) / len(words)
    return [word for word in words if len(word) > average_length]
