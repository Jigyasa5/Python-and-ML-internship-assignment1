# QUE 12) Write a python program that calculates the sum of the digits of a given number.

def sumOfnum(num):
    sum = 0
    for digit in str(num):  # Convert the number to a string to iterate over each digit
        sum += int(digit)
    return sum

num = int(input("Enter the number: "))  # Prompt the user to enter a number
print("The sum of the digits:", sumOfnum(num))

'''num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)'''