"""
Problem: Reverse a Number

Approach:
- Extract digits using modulus (% 10).
- Build reversed number by multiplying previous result by 10.

Time Complexity:
O(d) — where d is number of digits.

Space Complexity:
O(1) — constant space.
"""

def reverse_number(n):
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return reversed_num


if __name__ == "__main__":
    print(reverse_number(1234))  # 4321