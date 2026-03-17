"""
Problem: Count vowels in a string

Given a string, return the count of vowels (a, e, i, o, u) present in it.
The comparison should be case-insensitive.

Example:
count_vowels("Hello World") == 3 (e, o, o)
count_vowels("Python") == 1 (o)
count_vowels("AEIOU") == 5
count_vowels("Bcdfg") == 0
"""

import re

# Define the set of vowels for consistent use across methods
VOWELS = {'a', 'e', 'i', 'o', 'u'}

def count_vowels_builtin(s: str) -> int:
    """
    Approach 1: Using Python built-in functions (set and sum with generator).

    This method converts the input string to lowercase and then iterates
    through each character. For each character, it checks if it exists
    in a predefined set of lowercase vowels. The `sum()` function
    efficiently counts `True` values (which are treated as 1).
    """
    s_lower = s.lower()
    return sum(1 for char in s_lower if char in VOWELS)

def count_vowels_manual(s: str) -> int:
    """
    Approach 2: Manual loop implementation.

    This method converts the input string to lowercase and initializes a
    counter. It then iterates through each character of the string,
    manually checking if the character is one of the vowels. If it is,
    the counter is incremented.
    """
    s_lower = s.lower()
    count = 0
    for char in s_lower:
        if char in VOWELS:
            count += 1
    return count

def count_vowels_regex(s: str) -> int:
    """
    Approach 3: Optimized method using Regular Expressions.

    This method leverages the `re` module to find all occurrences of vowels
    in the string. The regex `[aeiou]` matches any of the specified lowercase
    vowels. The `re.IGNORECASE` flag ensures that both uppercase and lowercase
    vowels are matched. `re.findall()` returns a list of all non-overlapping
    matches, and the length of this list is the count of vowels.
    """
    # Pattern to match any vowel (a, e, i, o, u) case-insensitively
    return len(re.findall(r'[aeiou]', s, re.IGNORECASE))


"""
Complexity Analysis:

1. Approach 1: Using Python built-in functions (set and sum with generator)
   - Time Complexity: O(N), where N is the length of the string.
     - `s.lower()` takes O(N) to create a new lowercase string.
     - Iterating through the string using a generator expression takes O(N).
     - Checking `char in VOWELS` (set lookup) is O(1) on average.
     - `sum()` takes O(N) to process the generator.
     - Overall: O(N) + O(N) * O(1) = O(N).
   - Space Complexity: O(N) in the worst case (if `s.lower()` creates a new string).
     - The `VOWELS` set is constant O(1).
     - The generator expression itself uses O(1) extra space (it doesn't store the whole intermediate list).
     - However, `s.lower()` creates a new string, which takes O(N) space.

2. Approach 2: Manual loop implementation
   - Time Complexity: O(N), where N is the length of the string.
     - `s.lower()` takes O(N).
     - The `for` loop iterates N times.
     - `char in VOWELS` is O(1) on average.
     - Overall: O(N) + O(N) * O(1) = O(N).
   - Space Complexity: O(N) in the worst case (for `s.lower()`).
     - `count` variable is O(1).

3. Approach 3: Optimized method using Regular Expressions
   - Time Complexity: O(N), where N is the length of the string.
     - Regular expression engines typically process the string in linear time relative to its length (N).
     - `re.findall()` needs to scan the entire string once.
   - Space Complexity: O(K), where K is the number of vowels found.
     - `re.findall()` creates a list of all matched vowels. In the worst case, K can be N (e.g., "aeiouaeiou...").
     - So, it could be O(N) in the worst case.

Summary:
All three approaches have a time complexity of O(N), which is optimal as every character in the string must be examined at least once.
Space complexity varies slightly; the `re.findall` approach can use O(N) space to store the list of matches, while the other two use O(N) for the `s.lower()` copy but O(1) otherwise for additional variables/intermediate structures. For very long strings where memory is extremely tight, the manual loop (if `s.lower()` could be avoided by checking char by char for upper/lower case) would be slightly more space-efficient, but in typical Python usage, `s.lower()` is standard.
"""

if __name__ == "__main__":
    test_cases = [
        ("Hello World", 3),
        ("Python", 1),
        ("AEIOU", 5),
        ("aeiou", 5),
        ("rhythm", 0),
        ("", 0),
        ("Bcdfg", 0),
        ("12345!@#$", 0),
        ("AeiOu", 5),
        ("Programming is fun!", 5), # o, a, i, i, u
        ("Education", 5), # E, u, a, i, o
        ("MissIssippI", 4), # i, i, i, i
        ("aaaaaaaaaa", 10),
        ("xyz", 0),
        ("y", 0) # 'y' is not a vowel
    ]

    print("Running test cases for 'Count vowels in a string':")

    methods = {
        "Built-in method": count_vowels_builtin,
        "Manual loop method": count_vowels_manual,
        "Regex method": count_vowels_regex,
    }

    for name, func in methods.items():
        print(f"\n--- Testing {name} ---")
        for i, (input_string, expected_output) in enumerate(test_cases):
            actual_output = func(input_string)
            if actual_output == expected_output:
                print(f"Test {i+1} ('{input_string}'): PASS Expected {expected_output}, Got {actual_output}")
            else:
                print(f"Test {i+1} ('{input_string}'): FAIL Expected {expected_output}, Got {actual_output}")