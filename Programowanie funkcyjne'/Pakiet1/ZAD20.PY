def analyze_data(data):
   
    if isinstance(data, list):
        print("To jest lista.")
        print("Długość listy:", len(data))
        print("Pierwszy element listy:", data[0] if data else None)
    elif isinstance(data, tuple):
        print("To jest krotka.")
        print("Długość krotki:", len(data))
        print("Pierwszy element krotki:", data[0] if data else None)
    else:
        print("Nieznany typ danych.")


list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)
dict_data = {'a': 1, 'b': 2, 'c': 3}

analyze_data(list_data)
analyze_data(tuple_data)
analyze_data(dict_data)
