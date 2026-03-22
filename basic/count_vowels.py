"""
Problem: Count Vowels in a String

Approach:
- Convert string to lowercase.
- Traverse each character.
- Check if character is a vowel (a, e, i, o, u).
- Count occurrences.

Time Complexity:
O(n) — iterate through all characters.

Space Complexity:
O(1) — no extra space used.
"""

def count_vowels(s):
    s = s.lower()
    count = 0

    for ch in s:
        if ch in 'aeiou':
            count += 1

    return count


if __name__ == "__main__":
    print(count_vowels("Hello"))  # 2