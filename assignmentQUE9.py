# QUE 9) Write a python program that checks if a substring is present in a given string.
string = input("Enter the string: ")
substring = input("Enter the substring to check: ")

if substring in string:
    print("The substring is present in string.")
else:
    print("The substring is not present in string.")
