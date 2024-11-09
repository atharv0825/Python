str2 = str(input("Enter the name : "))
import random
num = random.randint(1 ,100)

print("what is square of  ",num)
num2 = int(input("Enter answer : "))
if num*num == num2 :
    print("Your right ")
else: 
    print("Your wrong")     
    
import random

name = input("Enter your name: ")
num = random.randint(1, 100)

if int(input(f"What is the square of {num}? ")) == num ** 2:
    print("You're right!")
else:
    print("You're wrong.")
 