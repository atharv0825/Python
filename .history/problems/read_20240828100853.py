import random

# while(num2 != -1):
#     name = input("Enter your name: ")
#     num = random.randint(1, 100)

#     if int(input(f"What is the square of {num}? ")) == num ** 2:
#         print("You're right!")
#     else:
#         print("You're wrong.")

name = input("Enter your name: ")

while True:
    num1 = random.randint(1, 100)
    num2 = int(input(f"What is the square of {num1}? "))

    if num2 == -1:
        break

    print("You're right" if num1**2 = num2 else "You're wrong")

