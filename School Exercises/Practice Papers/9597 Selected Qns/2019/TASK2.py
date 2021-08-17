# Task 2.1
from string import ascii_uppercase, ascii_lowercase


def rot13(string: str, shift: int = 13):
    """
    Shifts every alphabet in a string a specified number of characters forward

    Args:
        string: A string to encode
        shift: The number of characters to shift by (default 13)
    Returns:
        Encoded string
    """
    res = ""
    for char in string:
        if char in ascii_uppercase:
            # Wrap around for large numbers
            new_index = (ascii_uppercase.index(char) + shift) % 26
            res += ascii_uppercase[new_index]
        elif char in ascii_lowercase:
            # Wrap around for large numbers
            new_index = (ascii_lowercase.index(char) + shift) % 26
            res += ascii_lowercase[new_index]
        else:
            res += char
    return res


print(rot13("This is a word."))
print(rot13("ALL &&&& CAPITALS"))
print(rot13("UpperCamelCase12()"))

# Task 2.2
test_string = "Hello world."
encoded_string = rot13(test_string)
double_encoded_string = rot13(encoded_string)

print(f"Original: {test_string}")
print(f"Encoded once: {encoded_string}")
print(f"Encoded twice: {double_encoded_string}")
