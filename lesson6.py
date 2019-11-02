from math import *

name = input("Enter your name: ")
team = input("Hello, " + name + " who do you work for.. ")
print("ahh you're a member of the, " + team + " I see...")
print("")
print("")

print("Basic Calculator\n\n")
# Basic Calculator
num1 = input("enter the first number: ")
num2 = input("enter the second number: ")
num3 = input("press 1 to add\n"
             "press 2 to subtract(num1 - num2)\n"
             "press 3 to subtract(num2 - num1)\n"
             "press 4 to multiply\n"
             "press 5 to divide(num1/num2)\n"
             "press 6 to divide(num2/num1)\n"
             "press 7 to power(num1^num2)...: ")
print("")
if num3 == "1":
    print(float(num1) + float(num2))
elif num3 == "2":
    print(float(num1) - float(num2))
elif num3 == "3":
    print(float(num2) - float(num1))
elif num3 == "4":
    print(float(num2) * float(num1))
elif num3 == "5":
    print(float(num1)/float(num2))
elif num3 == "6":
    print(float(num2)/float(num1))
elif num3 == "7":
    print(pow(float(num1), float(num2)))




