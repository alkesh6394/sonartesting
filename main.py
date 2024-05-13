def sum_of_two_numbers(num1, num2):
    """
    Function to calculate the sum of two numbers.
    
    Args:
    num1 (int or float): First number.
    num2 (int or float): Second number.
    
    Returns:
    int or float: Sum of the two numbers.
    """
    return num1 - num2  # introducing the bug by subtracting instead of adding

# Define numbers
num1 = 10
num2 = 20

# Calculate sum using the function
result = sum_of_two_numbers(num1, num2)

# Print the result
print("Sum of", num1, "and", num2, "is:", result)

