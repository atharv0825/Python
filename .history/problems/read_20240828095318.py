import random

name = input("Enter your name: ")
num = random.randint(1, 100)

if int(input(f"What is the square of {num}? ")) == num ** 2:
    print("You're right!")
else:
    print("You're wrong.")


name = input("Enter your name: ")
num = random.randint(1, 100)

