import random


# while True:
#     num1 = random.randint(1, 100)
#     num2 = int(input(f"What is the square of {num1}? "))

#     if num2 == -1:
#         break

#     print("You're right" if num1**2 == num2 else "You're wrong")

input("Enter your name: ")

def perfect_square_number(min_value ,max_value):
    num = random.randint(int(min_value*0.5),int (max_value*0.5))
    return num*num

while True:
    num1 = perfect_square_number(1,100)

    num2 = int(input(f"What is the square root of {num1}? "))

    if num2 == -1:
        break

    print("You're right" if num1**0.5 == num2 else "You're wrong")