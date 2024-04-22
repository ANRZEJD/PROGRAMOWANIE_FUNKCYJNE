from itertools import combinations

def generate_combinations(elements):

    all_combinations = list(combinations(elements, 2))
    return all_combinations

elements_list = [1, 2, 3, 4]


result = generate_combinations(elements_list)


print(result)
