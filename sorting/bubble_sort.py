"""
Problem: Bubble Sort (Sorting Algorithm)
Difficulty: Easy (Conceptual)

Approach:
- Repeatedly compare adjacent elements.
- Swap if they are in wrong order.
- After each pass, largest element moves to the end.
- Use a flag to detect if array is already sorted.

Time Complexity:
Worst Case: O(n²)
Best Case: O(n) — when array is already sorted (optimized version)

Space Complexity:
O(1) — in-place sorting.

Key Insight:
Each iteration places the next largest element at its correct position.
"""

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps, array is sorted
        if not swapped:
            break

    return arr


# ✅ Test Cases
if __name__ == "__main__":
    print(bubbleSort([5, 3, 2, 4]))   # [2, 3, 4, 5]
    print(bubbleSort([1, 2, 3, 4]))   # [1, 2, 3, 4] (best case)
    print(bubbleSort([1]))            # [1] (edge case)