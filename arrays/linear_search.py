"""
Problem: Linear Search
Difficulty: Easy

Approach:
- Traverse the array from start to end.
- Compare each element with target.
- If found, return index.
- If not found, return -1.

Time Complexity:
O(n) — worst case we check all elements.

Space Complexity:
O(1) — no extra space used.

Key Insight:
Linear search is best for unsorted arrays.
"""

def linearSearch(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


# ✅ Test Cases
if __name__ == "__main__":
    print(linearSearch([3, 7, 2, 9, 5], 9))  # 3
    print(linearSearch([1, 2, 3, 4], 5))     # -1
    print(linearSearch([], 10))              # -1 (edge case)