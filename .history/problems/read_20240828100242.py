import random

# while(num2 != -1):
#     name = input("Enter your name: ")
#     num = random.randint(1, 100)

#     if int(input(f"What is the square of {num}? ")) == num ** 2:
#         print("You're right!")
#     else:
#         print("You're wrong.")


while True:
    name = input("Enter your name: ")
    num1 = random.randint(1, 100)

    if num1*num1 == int(input(f"What is the square of {num1}? ")) :
        print("Your right ")
    else: 
        print("Your wrong")


