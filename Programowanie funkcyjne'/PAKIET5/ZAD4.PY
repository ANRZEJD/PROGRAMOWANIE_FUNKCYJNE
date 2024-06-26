def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

result_addition = apply_operation(add, 5, 3)
result_subtraction = apply_operation(subtract, 5, 3)

print("Wynik dodawania:", result_addition)  
print("Wynik odejmowania:", result_subtraction)  
