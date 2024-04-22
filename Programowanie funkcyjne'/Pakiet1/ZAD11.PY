def sort_strings_by_length(strings):
    return sorted(strings, key=lambda x: len(x))

words = ["FA", "GAB", "QABC", "WABCD", "XABCDE", "ZABCDEF"]
sorted_words = sort_strings_by_length(words)
print(sorted_words) 
