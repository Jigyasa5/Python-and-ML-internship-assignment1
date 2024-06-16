# QUE 3) Write a python program that calculates the factorial of a given number

def factorial(num):
    if num==0 or num==1 :
        return 1
    else:
        return num*factorial(num-1)

num = int(input("Enter the number: "))
print("The factorial of number: ", factorial(num))
