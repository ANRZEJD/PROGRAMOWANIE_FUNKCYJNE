def process_tuple(data):
   
    length = len(data)
    total_sum = sum(data)
    return length, total_sum

tuple_data = (1, 2, 3, 4, 5)
result_length, result_sum = process_tuple(tuple_data)

print("Długość krotki:", result_length)
print("Suma elementów krotki:", result_sum)
