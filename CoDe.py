class FactorialCalculator:
    """A class to calculate factorials."""

    @staticmethod
    def calculate(n):
        """Calculate the factorial of a given number."""
        if n < 0:
            return "Factorial is not defined for negative numbers."
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

# Example usage
calculator = FactorialCalculator()
print(calculator.calculate(5))  # Output: 120
