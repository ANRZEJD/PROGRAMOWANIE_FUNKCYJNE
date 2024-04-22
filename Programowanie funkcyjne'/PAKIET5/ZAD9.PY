from functools import reduce

numbers = [12, 45, 23, 67, 89, 34, 56]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Największa liczba:", max_number)


def calculate_average(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers)

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("Średnia:", average)
