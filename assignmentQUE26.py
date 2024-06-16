# QUE 26) Write a program in python that checks if a string starts with a given prefix  or ends with a given suffix.

input_string = input("Please enter a string: ")

prefix = input("Please enter the prefix to check: ")
suffix = input("Please enter the suffix to check: ")

starts_with_prefix = input_string.startswith(prefix)
ends_with_suffix = input_string.endswith(suffix)

if starts_with_prefix:
    print("The string starts with the prefix: ",prefix)
else:
    print("The string does not start with the prefix: ",prefix)

if ends_with_suffix:
    print("The string ends with the suffix: ", suffix)
else:
    print("The string does not end with the suffix: ", suffix)
