
words = ["apple", "banana", "orange", "apricot", "kiwi", "avocado"]
filtered_words = list(filter(lambda x: x.startswith('a'), words))
print("Słowa zaczynające się na literę 'a':", filtered_words)


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Kwadraty liczb:", squared_numbers)
