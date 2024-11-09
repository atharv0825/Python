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

    if num1*num1 == num2 :
        print("Your right ")
    else: 
        print("Your wrong")


