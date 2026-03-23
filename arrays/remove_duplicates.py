"""
Problem: Remove Duplicates from Array

Approach:
- Use a set to track seen elements.
- Traverse array and add elements only if not seen.
- Maintain order using result list.

Time Complexity:
O(n) — each lookup in set is O(1).

Space Complexity:
O(n) — extra space for set and result list.
"""

def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4]
    print(remove_duplicates(arr))  # [1, 2, 3, 4]