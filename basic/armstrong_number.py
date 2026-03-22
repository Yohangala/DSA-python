"""
Problem: Armstrong Number

Approach:
- Count number of digits.
- Extract each digit.
- Raise digit to the power of total digits.
- Sum all values and compare with original number.

Time Complexity:
O(d) — where d is number of digits.

Space Complexity:
O(1) — constant space.
"""

def is_armstrong(num):
    original = num
    total = 0
    power = len(str(num))

    while num > 0:
        digit = num % 10
        total += digit ** power
        num //= 10

    return total == original


if __name__ == "__main__":
    print(is_armstrong(153))  # True