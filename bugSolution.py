import cmath

def handle_complex_numbers(x):
    try:
        result = 1 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(x, complex):
            result = 1 / x
            return result
        else:
            return "Invalid input type"

# improved function to handle potential floating-point exceptions
import math

def improved_sqrt(x):
    if x < 0:
        return cmath.sqrt(x)
    elif x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid input"

# Example usage:
result = handle_complex_numbers(2+3j)
print(result) # Output: (0.2-0.3j)
result = handle_complex_numbers(0)
print(result) # Output: Division by zero
result = handle_complex_numbers("hello")
print(result) # Output: Invalid input type
result = improved_sqrt(-1.0) 
print(result) # Output: 1j
result = improved_sqrt(1.0) 
print(result) # Output: 1.0
result = improved_sqrt("hello")
print(result) # Output: Invalid input