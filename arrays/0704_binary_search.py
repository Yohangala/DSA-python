"""
Problem: 704. Binary Search
Link: https://leetcode.com/problems/binary-search/
Difficulty: Easy

Approach:
- Use two pointers (low and high).
- Find middle element.
- If target found → return index.
- If target smaller → search left half.
- If target greater → search right half.

Time Complexity:
O(log n) — search space halves each iteration.

Space Complexity:
O(1) — constant extra space.

Key Insight:
Binary search works only on sorted arrays and reduces
search space by half each step.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()

    print(sol.search([-1,0,3,5,9,12], 9))   # 4
    print(sol.search([-1,0,3,5,9,12], 2))   # -1
    print(sol.search([5], 5))               # 0 (edge case)