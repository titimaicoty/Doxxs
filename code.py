def recursive_factorial(n):
    """Calculate the factorial of a given number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# Example usage
print(recursive_factorial(5))  # Output: 120
