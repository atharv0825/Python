students = ["Atharv","Alfaj","Piyush"]
print(students)

#The append() method appends an element to the end of the list.
print("\nAppend : ")
students.append("Kunal");
print(students)

# clear() Removes all the elements from the list
# print("\nClear : ")
# students.clear()
# print(students)

#copy() Returns a copy of the list
print("\nCopy : ")
seniors = students.copy()
print(seniors)

#count() Returns the number of elements with the specified value
print("\nCount : ")
no = students.count("Kunal")
print("NO students : " , no)

#extend() Add the elements of a list (or any iterable), to the end of the current list
print("\nextend : ")
roll=[1,2,3,4]
students.extend(roll)
print(students)

#index() Returns the index of the first element with the specified value
print("\nindex : ")
print("Kunal's index : " , students.index("Kunal"))

# insert()	Adds an element at the specified position
print()