
numbers = [3, 8, 12, 5, 10, 15]


squared_greater_than_10 = [square for num in numbers if (square := num ** 2) > 10]


print(squared_greater_than_10)
