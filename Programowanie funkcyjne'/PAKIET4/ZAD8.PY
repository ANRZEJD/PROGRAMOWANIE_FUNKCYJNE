from collections import Counter

def most_common_element(lst):
    counts = Counter(lst)
    most_common = counts.most_common(1)
    return most_common[0][0]
