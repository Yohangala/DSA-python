"""
Problem: Find Minimum and Maximum in an Array

Approach:
- Initialize min and max with first element.
- Traverse array and update values.

Time Complexity:
O(n) — single traversal.

Space Complexity:
O(1) — no extra space.
"""

def min_max(arr):
    min_val = arr[0]
    max_val = arr[0]

    for num in arr:
        min_val = min(min_val, num)
        max_val = max(max_val, num)

    return min_val, max_val


if __name__ == "__main__":
    arr = [3, 7, 2, 9, 5]
    print(min_max(arr))  # (2, 9)