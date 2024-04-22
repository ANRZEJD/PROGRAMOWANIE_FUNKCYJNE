
def square(x):
    return x ** 2


def add_five(x):
    return x + 5


def apply_functions_to_list(numbers, *functions):
    result = []
    for number in numbers:
        for func in functions:
            number = func(number)
        result.append(number)
    return result


numbers = [1, 2, 3, 4, 5]


result = apply_functions_to_list(numbers, square, add_five)

print("Wynik:", result)
