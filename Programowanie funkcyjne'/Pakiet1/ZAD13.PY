def calculate_factorial(n):
  
    if n == 0 or n == 1:
        return 1
 
    else:
        return n * calculate_factorial(n - 1)
    
number = 5
result = calculate_factorial(number)
print(result) 
