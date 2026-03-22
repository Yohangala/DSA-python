"""
Problem: Fibonacci Series (Basic)

Approach:
- Start with first two numbers: 0 and 1.
- Iteratively generate next number as sum of previous two.

Time Complexity:
O(n) — loop runs n times.

Space Complexity:
O(1) — only variables used.
"""

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a)
        a, b = b, a + b


if __name__ == "__main__":
    fibonacci(6)