# 17. program for demonstrating any 5 functions of dictionary 
dict = {
    "Name" : "Atharv",
    "Age" : 20,
    "Roll no" : 10,    
}
# 1. Update function
dict.update({"Address" : "Vita"})
print("Update Function : ",dict)

# 2. Pop function
dict.pop("Age")
print("pop function : ",dict)

# 3. Popitem function 
dict.popitem()
print("popitem function : ",dict)

# 4. keys function
dict.keys