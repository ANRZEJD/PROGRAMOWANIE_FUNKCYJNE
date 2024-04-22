words = ["A", "AB", "ABC", "ABCD", "ABCDE", "ABCDEF"]
filtered_words = list(filter(lambda word: len(word) > 5, words))
print(filtered_words)  # Wydrukuje ['banana', 'orange', 'strawberry', 'pineapple']
