def add(x):
  
    def add_second_argument(y):
      
        return x + y
    return add_second_argument

add_to_5 = add(5)
result = add_to_5(3)
print(result) 
