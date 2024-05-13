def sum_of_two_numbers(num1):
    """
    Function to calculate the sum of two numbers.
    
    Args:
    num1 (int or float): First number.
    
    Returns:
    int or float: Sum of the two numbers.
    """
    return num1 + num2  # Intentional bug: num2 is not defined in this function

# Define numbers
num1 = 10
num2 = 20

# Calculate sum using the function
result = sum_of_two_numbers(num1)

# Print the result
print("Sum of", num1, "and", num2, "is:", result)

