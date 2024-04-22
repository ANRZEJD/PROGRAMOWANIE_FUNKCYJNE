def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            return None
    return wrapper

@safe_function
def divide(a, b):
    return a / b


result = divide(10, 2)
print("Wynik dzielenia:", result)

result = divide(10, 0) 
print("Wynik dzielenia:", result)
