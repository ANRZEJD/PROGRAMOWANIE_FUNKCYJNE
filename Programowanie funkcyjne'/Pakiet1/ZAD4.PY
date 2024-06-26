import time
def timeit(func):
     def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania {func.__name__}: {execution_time} sekund")
        return result
    