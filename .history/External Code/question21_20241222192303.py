# 21. program for creating function and lambda function 

square_lambda = lambda num : num**2
add_lambda = lambda num1 , num2 : num1 + num2
sub_lambda = lambda num1 , num2 : num1 - num2
div_lambda = lambda num1 , num2 : num1 - num2

print(f"Square of the 5 : {square_lambda(5)}")
print(f"Addition of the 10 and 20 : {add_lambda(10,20)}")
print(f"Subtraction of the 10 and 20 : {sub_lambda(20,10)}")