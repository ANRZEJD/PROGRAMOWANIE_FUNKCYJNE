
def generate_even_numbers():
    n = 0
    while True:
        yield n
        n += 2

even_numbers = generate_even_numbers()


for _ in range(5):
    print(next(even_numbers))
