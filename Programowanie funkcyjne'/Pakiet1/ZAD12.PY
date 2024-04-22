from functools import partial
def multiply(x, factor):
    return x * factor
multiply_by_3 = partial(multiply, factor=3)
result = multiply_by_3(4)
print(result)  
