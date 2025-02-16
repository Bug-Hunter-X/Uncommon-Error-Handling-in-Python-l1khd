def function_with_uncommon_error(x):
    try:
        result = 1 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

# Uncommon error case: Input is a complex number
result = function_with_uncommon_error(2+3j)
print(result) # Output: (0.2-0.3j) # Correct handling

result = function_with_uncommon_error("hello")
print(result) # Output: Invalid input type # Correct handling

result = function_with_uncommon_error(0)
print(result) # Output: Division by zero # Correct handling

# Uncommon error handling for floating point exceptions
# Example showing that it's not enough to check for NaN only
import math

def function_with_uncommon_error2(x):
    try:
        result = math.sqrt(-1.0)
    except ValueError:
        return "Invalid input for square root (negative number)"
    except OverflowError:
        return "Overflow error"
    return result

result = function_with_uncommon_error2(-1.0)
print(result)  # Output: Invalid input for square root (negative number)

# Example: A more robust solution to handle potential errors
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

result = handle_complex_numbers(2+3j)
print(result) # Output: (0.2-0.3j) 
result = handle_complex_numbers(0)
print(result) # Output: Division by zero
result = handle_complex_numbers("hello")
print(result) # Output: Invalid input type