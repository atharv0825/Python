import array as arr

numbers = arr.array('i',[10,20,30,40,50])
print("Original Array : ",numbers)

# 1.Append function 
numbers.append(60)
print("Append Function : ",numbers)

# 2.Insert function
numbers.insert(6,70)
print("Insert Function : ",numbers)

# 3.count function
x = numbers.count(70)
print("Count function : ",x)

# 4.copy function
c = numbers.__copy__()
print("Copy function : ",c)

# 5.extend function
numbers2 = arr.array('i',[80,90,100])
numbers.extend(numbers2)
print("Extend Function : ",numbers)

# 6.reverse function
numbers.reverse()
print("Reverse Funtion :",numbers)