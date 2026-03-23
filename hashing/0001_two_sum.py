"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Approach:
- Use a hashmap to store numbers and their indices.
- For each element, calculate the required complement.
- If complement exists in hashmap, return indices.

Time Complexity:
O(n) — single pass through array.

Space Complexity:
O(n) — hashmap stores up to n elements.

Key Insight:
Instead of checking all pairs, store previously seen numbers
to find complement in constant time.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in d:
                return [d[needed], i]

            d[num] = i

        return []


# ✅ Test Cases
if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum([2,7,11,15], 9))   # [0,1]
    print(sol.twoSum([3,2,4], 6))       # [1,2]
    print(sol.twoSum([3,3], 6))         # [0,1] (edge case)