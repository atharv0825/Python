# 20. program for demonstrating any 5 functions of set 
set1 = {10,20,30,40,50}
set2 = {10,20,70,80,90}


print("original function : ",set1)
# 1.Add function 
set1.add(60)
print("Add function : ",set1)

# 2.remove function 
set1.remove(60)
print("Remove function : ",set1)

# 3.union funtion 
union_set = set1.union(set2)
print("Union function : ",union_set)

# 4.intersection function 
intersection_set = set1.intersection(set2)
print("Intersection Function : ",intersection_set)

# 5.difference function
differnce_set = set1.difference(set2)
print("Difference Function : ",differnce_set)

# 6.symmetric function 
symmetric_diff = set1.symmetric_difference(set2)
