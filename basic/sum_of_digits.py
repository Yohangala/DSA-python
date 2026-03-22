"""
Problem: Sum of Digits

Approach:
- Extract digits using modulus (% 10).
- Add each digit to total.
- Remove last digit using integer division (// 10).

Time Complexity:
O(d) — where d is number of digits.

Space Complexity:
O(1) — no extra space used.
"""

def sum_of_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    return total


if __name__ == "__main__":
    print(sum_of_digits(1234))  # 10