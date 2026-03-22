"""
Problem: Check Prime Number

Approach:
- Numbers <= 1 are not prime.
- Check divisibility from 2 to sqrt(n).
- If divisible, not prime.

Time Complexity:
O(sqrt(n)) — optimized loop.

Space Complexity:
O(1) — constant space.
"""

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_prime(7))  # True