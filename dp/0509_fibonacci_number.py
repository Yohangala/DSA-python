"""
Problem: 509. Fibonacci Number
Link: https://leetcode.com/problems/fibonacci-number/
Difficulty: Easy

Approach:
- Use iterative dynamic programming.
- Maintain two variables representing previous two Fibonacci numbers.
- Update them in each iteration.

Time Complexity:
O(n) — we iterate from 2 to n.

Space Complexity:
O(1) — only two variables used.

Key Insight:
We only need the last two values to compute the next one,
so we can optimize space from O(n) to O(1).
"""

class Solution:
    def fib(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1

        # Compute Fibonacci iteratively
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()

    print(sol.fib(2))  # Expected: 1
    print(sol.fib(5))  # Expected: 5
    print(sol.fib(0))  # Edge case: 0