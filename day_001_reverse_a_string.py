"""
Problem: Reverse a String

Category: String
Difficulty: Easy
Day: 1/100

Problem Description:
Given a string, return a new string with the characters in reverse order.

Example:
Input: "hello"
Output: "olleh"

Input: "Python"
Output: "nohtyP"
"""

def reverse_string_builtin(s: str) -> str:
    """
    Approach 1: Using Python built-in slicing.

    This is the most Pythonic and concise way to reverse a string.
    Python's slicing `[::-1]` creates a reversed copy of the string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

def reverse_string_manual_prepend(s: str) -> str:
    """
    Approach 2: Manual implementation by iterating and prepending characters.

    This approach iterates through each character of the original string
    and prepends it to a new result string. This demonstrates a manual
    way but is less efficient due to string immutability in Python.
    Each `char + reversed_s` operation creates a new string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def reverse_string_optimized_list_swap(s: str) -> str:
    """
    Approach 3: Optimized method using list conversion and two-pointer swap.

    This approach converts the string to a list of characters (since strings
    are immutable in Python). It then uses a two-pointer technique to swap
    characters from the beginning and end of the list until the pointers meet.
    Finally, it joins the list of characters back into a string.
    This demonstrates an efficient algorithmic approach (O(N) time).

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    char_list = list(s)
    left, right = 0, len(char_list) - 1

    while left < right:
        # Swap characters at left and right pointers
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
        
    return "".join(char_list)

# --- Complexity Analysis ---

"""
1.  Approach 1: Using Python built-in slicing (`[::-1]`)
    -   Time Complexity: O(N)
        Creating a slice of a string takes time proportional to the length of the string.
        Python's internal implementation for `[::-1]` is highly optimized, usually in C.
    -   Space Complexity: O(N)
        A new string of length N is created to store the reversed characters.

2.  Approach 2: Manual iteration and prepending characters
    -   Time Complexity: O(N^2)
        In Python, strings are immutable. Each time `reversed_s = char + reversed_s`
        is executed, a new string is created. The length of `reversed_s` grows
        from 1 to N. The cost of concatenation is proportional to the length
        of the strings being concatenated. Summing 1 + 2 + ... + N operations
        results in O(N^2) time complexity.
    -   Space Complexity: O(N^2)
        Due to the repeated creation of new intermediate strings during concatenation,
        which are then discarded, the total space allocated over time can be O(N^2).
        At any single point, the maximum extra space used for the `reversed_s` variable
        is O(N).

3.  Approach 3: Optimized method using list conversion and two-pointer swap
    -   Time Complexity: O(N)
        -   Converting the string to a list of characters: O(N)
        -   Two-pointer swap: The `while` loop runs N/2 times, with constant time operations
            inside (swapping and incrementing/decrementing pointers). This is O(N).
        -   Joining the list back into a string: O(N)
        Overall, the dominant operations are proportional to N, resulting in O(N).
    -   Space Complexity: O(N)
        -   Creating the list of characters: O(N)
        -   The `"".join()` operation might create another new string of length N: O(N)
        Overall, additional space proportional to N is used.
"""

# --- Test Cases ---

if __name__ == "__main__":
    test_cases = [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("", ""), # Empty string
        ("a", "a"), # Single character string
        ("racecar", "racecar"), # Palindrome
        ("madam", "madam"), # Another palindrome
        ("12345", "54321"), # String with numbers
        (" A B C ", " C B A "), # String with spaces
        ("!@#$", "$#@!") # String with special characters
    ]

    print("--- Testing Approach 1: Pythonic Slicing ---")
    for input_str, expected_output in test_cases:
        actual_output = reverse_string_builtin(input_str)
        if actual_output == expected_output:
            print(f"PASS Test Passed for '{input_str}': Expected '{expected_output}', Got '{actual_output}'")
        else:
            print(f"FAIL Test Failed for '{input_str}': Expected '{expected_output}', Got '{actual_output}'")

    print("\n--- Testing Approach 2: Manual Iteration and Prepending ---")
    for input_str, expected_output in test_cases:
        actual_output = reverse_string_manual_prepend(input_str)
        if actual_output == expected_output:
            print(f"PASS Test Passed for '{input_str}': Expected '{expected_output}', Got '{actual_output}'")
        else:
            print(f"FAIL Test Failed for '{input_str}': Expected '{expected_output}', Got '{actual_output}'")

    print("\n--- Testing Approach 3: Two-Pointer Swap (List Conversion) ---")
    for input_str, expected_output in test_cases:
        actual_output = reverse_string_optimized_list_swap(input_str)
        if actual_output == expected_output:
            print(f"PASS Test Passed for '{input_str}': Expected '{expected_output}', Got '{actual_output}'")
        else:
            print(f"FAIL Test Failed for '{input_str}': Expected '{expected_output}', Got '{actual_output}'")