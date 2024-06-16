# QUE 5) Write a program that takes a string input from the user and writes it to a text file.

user_string = input("Eter the string: ")

f=open('mlintern.txt', 'w')
f.write(user_string)
f.close()
print("The input has been written to mlintern.txt.")