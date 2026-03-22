# ╔══════════════════════════════════════════════════════════╗
# ║  Problem   : 344. Reverse String                         ║
# ║  Link      : https://leetcode.com/problems/reverse-string/
# ║  Difficulty: Easy          Platform: LeetCode            ║
# ╠══════════════════════════════════════════════════════════╣
# ║  Approach  : Two Pointers                                ║
# ║  Time      : O(n) — n/2 swaps, traverse half array      ║
# ║  Space     : O(1) — in-place, no extra memory used      ║
# ╠══════════════════════════════════════════════════════════╣
# ║  Key Insight:                                            ║
# ║  Two-pointer technique works when elements need to be   ║
# ║  processed from both ends simultaneously.               ║
# ╚══════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]  # swap
            left += 1
            right -= 1

# ── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    arr1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(arr1)
    print(arr1)  # Expected: ["o", "l", "l", "e", "h"]

    arr2 = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(arr2)
    print(arr2)  # Expected: ["h", "a", "n", "n", "a", "H"]

    arr3 = ["a"]          # edge case: single element
    sol.reverseString(arr3)
    print(arr3)  # Expected: ["a"]