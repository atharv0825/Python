# 3. Find factorial of a number using recursion in python.
num = int(input("Enter Number : "))
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    

printf("Factorial of {num} is {factorial(num)}")    
