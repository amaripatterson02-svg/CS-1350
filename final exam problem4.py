def is_palindrome_recursive(s):
    """
    Check if a string is a palindrome using recursion.
    Ignore spaces and case.
    """
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Base case: empty or one character → palindrome
    if len(s) <= 1:
        return True

    # If first and last characters don't match → not palindrome
    if s[0] != s[-1]:
        return False

    # Recursive call on the string without first and last char
    return is_palindrome_recursive(s[1:-1])


# Test your function:
print(is_palindrome_recursive("racecar"))  # True
print(is_palindrome_recursive("hello"))  # False
print(is_palindrome_recursive("A man a plan a canal Panama"))  # True
print(is_palindrome_recursive(""))  # True
