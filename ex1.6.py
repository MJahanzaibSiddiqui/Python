# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. For example, "radar" and "madam" are palindromes because if you reverse the order of their characters, they still spell the same thing.

def palindrome(input_str):
    # Base case: if the string is empty or has only one character
    if len(input_str) <= 1:
        return True
    elif input_str[0] == input_str[-1]:  # Check if first and last characters match
        # Recur for the substring without the first and last characters
        return palindrome(input_str[1:-1])
    else:
        return False

str1 = "madam"
str2 = "hello"

print(f"'{str1}' is a palindrome: {palindrome(str1)}")
print(f"'{str2}' is a palindrome: {palindrome(str2)}")


# Specifically, input_str[1:-1] does the following:

# 1 is the start index, meaning we start from the second character of the string (Python uses zero-based indexing, so 1 is the second character).
# -1 is the end index, meaning we go up to the second-to-last character of the string (excluding the last character).
# input_str[start:end] = input_str[1:-1]

# The f in print(f"...") is called an f-string or a formatted string literal in Python. It's used for string formatting and allows you to embed expressions inside a string by using curly braces {}.

# For example, you might want to include a variable's value in a string to print a meaningful message. Instead of concatenating strings and variables using +, you can use f-strings for a cleaner and more readable approach.