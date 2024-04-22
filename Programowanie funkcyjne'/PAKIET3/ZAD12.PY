def rotate_list(lst, steps):
    if not lst:
        return lst
    steps = steps % len(lst)
    return lst[-steps:] + lst[:-steps]
