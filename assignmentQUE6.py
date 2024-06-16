# QUE 6) Write a program that reads the content of a text file and prints it to the console.

f = open('mlintern.txt', "r")
print("The content of the file is:")
print(f.read())
f.close()
