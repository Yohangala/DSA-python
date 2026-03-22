"""
Problem: Factorial of a Number

Approach:
- Multiply numbers from n to 1 using a loop.

Time Complexity:
O(n) — loop runs n times.

Space Complexity:
O(1) — constant space used.
"""

def factorial(n):
    total = 1

    while n > 0:
        total *= n
        n -= 1

    return total


if __name__ == "__main__":
    print(factorial(5))  # 120