global_variable = 10

def function_with_global_variable(local_variable):
    global global_variable
    global_variable += local_variable
    return global_variable

result = function_with_global_variable(5)
print("Wynik:", result) 

