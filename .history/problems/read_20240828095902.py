import random

    name = input("Enter your name: ")
    num = random.randint(1, 100)

    if int(input(f"What is the square of {num}? ")) == num ** 2:
        print("You're right!")
    else:
        print("You're wrong.")

num2 = 0

while(num2 != -1):
    name = input("Enter your name: ")
    num1 = random.randint(1, 100)

    int(input("Enter your Answer (-1 to exit)"))

    if num1*num1 == num2 :
        print("Your right ")
    else: 
        print("Your wrong")


