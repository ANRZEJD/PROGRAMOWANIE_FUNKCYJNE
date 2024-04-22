def filter_even_values(dictionary):
    return {key: value for key, value in dictionary.items() if isinstance(value, int) and value % 2 == 0}
