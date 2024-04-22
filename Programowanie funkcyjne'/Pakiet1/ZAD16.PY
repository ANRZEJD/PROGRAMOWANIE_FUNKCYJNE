def compose(f, g):

    def composed_function(x):
        return f(g(x))
    return composed_function


def square(x):
    return x ** 2

def add_one(x):
    return x + 1

composed_function = compose(square, add_one)


result = composed_function(3)  
print(result)  