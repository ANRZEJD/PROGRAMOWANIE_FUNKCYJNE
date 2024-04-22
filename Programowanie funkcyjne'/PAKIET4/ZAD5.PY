def split_list(lst, max_length):
    return [lst[i:i+max_length] for i in range(0, len(lst), max_length)]
