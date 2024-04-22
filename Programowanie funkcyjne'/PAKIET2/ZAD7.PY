from itertools import groupby


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_even(n):
    return n % 2 == 0


grouped_numbers = groupby(numbers, key=is_even)

for key, group in grouped_numbers:
    group_list = list(group)
    print("Parzysta:" if key else "Nieparzysta:", group_list)
