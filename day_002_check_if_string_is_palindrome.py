"""
Problem: Check if string is palindrome

A palindrome is a word, phrase, number, or other sequence of characters
which reads the same forward and backward.
This problem asks us to determine if a given string is a palindrome.

For a basic definition, we typically consider case-sensitivity and all characters.
However, common variations (especially in interviews) include ignoring
non-alphanumeric characters and case. Our "optimized" approach will cover this.
"""

def is_palindrome_builtin(s: str) -> bool:
    """
    Approach 1: Using Python built-ins (string slicing).

    This approach leverages Python's powerful string slicing capabilities
    to reverse the string and then directly compares it with the original.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

def is_palindrome_manual(s: str) -> bool:
    """
    Approach 2: Manual implementation using two pointers.

    This method uses two pointers, one starting from the beginning (left)
    and one from the end (right) of the string. It iteratively compares
    characters at these pointers, moving inwards. If any characters do not match,
    the string is not a palindrome.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_optimized(s: str) -> bool:
    """
    Approach 3: Optimized method (handles case-insensitivity and non-alphanumeric characters).

    This approach is often what's expected in a real-world scenario or interview
    where "palindrome" refers to phrases like "A man, a plan, a canal: Panama".
    It uses a two-pointer technique but first sanitizes characters by skipping
    non-alphanumeric ones and converting characters to lowercase for comparison.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome (ignoring case and non-alphanumeric chars),
              False otherwise.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Move left pointer past non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer past non-alphanumeric characters
        while left < right and not s[right].isalnum():
            right -= 1

        # If characters at valid positions don't match (case-insensitively), it's not a palindrome
        if left < right and s[left].lower() != s[right].lower():
            return False

        # Move pointers inwards
        left += 1
        right -= 1

    return True

"""
Complexity Analysis:

1. Approach 1: Using Python builtins (is_palindrome_builtin)
   - Time Complexity: O(N)
     Creating a slice s[::-1] takes O(N) time as it copies the entire string.
     Comparing two strings of length N takes O(N) time in the worst case.
     Therefore, the total time complexity is O(N).
   - Space Complexity: O(N)
     Creating the reversed string slice s[::-1] requires O(N) additional space
     to store the new string.

2. Approach 2: Manual implementation (is_palindrome_manual)
   - Time Complexity: O(N)
     The two pointers traverse at most half of the string. In the worst case,
     they make N/2 comparisons. This is O(N).
   - Space Complexity: O(1)
     Only a few variables (pointers) are used, which consume constant extra space.

3. Approach 3: Optimized method (is_palindrome_optimized)
   - Time Complexity: O(N)
     The two pointers traverse the string at most once. In the worst case,
     each pointer might iterate through the entire string (e.g., if the string
     is all non-alphanumeric or requires many skips). Character checking
     (.isalnum(), .lower()) is typically O(1).
     Therefore, the total time complexity is O(N).
   - Space Complexity: O(1)
     Only a few variables (pointers) are used, consuming constant extra space.

Summary:
The manual and optimized two-pointer methods are generally preferred for
their O(1) space complexity, especially for very long strings where
creating a full copy might be an issue. The optimized method is robust for
real-world palindrome definitions.
"""

if __name__ == "__main__":
    test_cases = [
        # Basic Palindromes
        ("madam", True, "Basic odd length palindrome"),
        ("racecar", True, "Basic odd length palindrome"),
        ("level", True, "Basic odd length palindrome"),
        ("anna", True, "Basic even length palindrome"),
        ("noon", True, "Basic even length palindrome"),

        # Non-Palindromes
        ("hello", False, "Basic non-palindrome"),
        ("world", False, "Basic non-palindrome"),
        ("python", False, "Basic non-palindrome"),
        ("abcda", False, "Non-palindrome"),

        # Edge Cases
        ("", True, "Empty string"),
        ("a", True, "Single character string"),
        ("  ", True, "String with only spaces (for basic approaches)"),
        (" % ", True, "String with only non-alphanumeric (for basic approaches)"),

        # Cases for Optimized Approach (ignoring case & non-alphanumeric)
        ("A man, a plan, a canal: Panama", True, "Classic phrase palindrome"),
        ("No lemon, no melon", True, "Another classic phrase palindrome"),
        ("Was it a car or a cat I saw?", True, "Phrase with punctuation and spaces"),
        ("Madam", True, "Case-insensitive palindrome"),
        ("RaceCar", True, "Case-insensitive palindrome"),
        ("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.", True, "Long complex palindrome"),
        ("0P", False, "Simple non-palindrome with mixed chars"),
        (" ", True, "Single space string (optimized)"),
        (".,", True, "Only punctuation (optimized)"),
        ("ab_a", True, "With underscore (optimized)"),
        ("!@#$A", True, "Only one alphanumeric (optimized)"),
        ("A_B", False, "Non-palindrome with underscore"),
        ("ab@ba", True, "Palindrome with special chars in middle"),
    ]

    print("--- Testing is_palindrome_builtin ---")
    for s, expected, desc in test_cases:
        # For builtin and manual, " " is a palindrome, "A man..." is not due to spaces/punctuation/case.
        # Adjust expected value for optimized-specific cases for the first two approaches
        if "Classic phrase palindrome" in desc or "Phrase with punctuation" in desc or "Case-insensitive" in desc or "Long complex palindrome" in desc or "With underscore" in desc or "special chars in middle" in desc or "alphanumeric (optimized)" in desc:
            adjusted_expected = False
        elif s.strip() == "" and len(s) > 0: # handle strings like "  ", " % "
            adjusted_expected = True
        else:
            adjusted_expected = expected

        result = is_palindrome_builtin(s)
        status = "PASS" if result == adjusted_expected else "FAIL"
        print(f"'{s}': Expected {adjusted_expected}, Got {result} {status} ({desc})")

    print("\n--- Testing is_palindrome_manual ---")
    for s, expected, desc in test_cases:
        # Same adjustment as for builtin
        if "Classic phrase palindrome" in desc or "Phrase with punctuation" in desc or "Case-insensitive" in desc or "Long complex palindrome" in desc or "With underscore" in desc or "special chars in middle" in desc or "alphanumeric (optimized)" in desc:
            adjusted_expected = False
        elif s.strip() == "" and len(s) > 0:
            adjusted_expected = True
        else:
            adjusted_expected = expected

        result = is_palindrome_manual(s)
        status = "PASS" if result == adjusted_expected else "FAIL"
        print(f"'{s}': Expected {adjusted_expected}, Got {result} {status} ({desc})")

    print("\n--- Testing is_palindrome_optimized ---")
    for s, expected, desc in test_cases:
        result = is_palindrome_optimized(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"'{s}': Expected {expected}, Got {result} {status} ({desc})")