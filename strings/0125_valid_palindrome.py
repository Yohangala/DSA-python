"""
Problem: 125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy

Approach:
- Use two pointers (left and right).
- Skip non-alphanumeric characters.
- Compare characters in lowercase.
- If mismatch occurs, return False.
- Continue until pointers meet.

Time Complexity:
O(n) — each character is visited at most once.

Space Complexity:
O(1) — no extra space used.

Key Insight:
Avoid creating a new string. Instead, process characters
in-place using two pointers for optimal performance.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip invalid characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()

    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))                      # False
    print(sol.isPalindrome(" "))                               # True (edge case)