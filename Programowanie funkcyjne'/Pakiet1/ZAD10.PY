even_numbers_generator = (x for x in range(0, 2**31, 2))
for _ in range(10):
    print(next(even_numbers_generator))
