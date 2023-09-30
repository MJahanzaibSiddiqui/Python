def reverse_string(orignal_str):
    return orignal_str[::-1]

# Calling function
orignal_string = "apple"
reversed_string = reverse_string(orignal_string)
print("Original String:", orignal_string)
print("Reversed String:", reversed_string)



# input_str: This is the input string that we want to reverse.

# [::-1]: This is called string slicing in Python, and it's used to create a reversed copy of the original string.

# The first : is the beginning of the slicing syntax.

# The second : is the end of the slicing syntax.

# -1 indicates the step size. A step size of -1 means we're traversing the string backwards