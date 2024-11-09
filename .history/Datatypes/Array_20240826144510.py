import array as arr
a = arr.array('i',[1,2,3])
print("Printing Array : ")
for i in range(0 , 3):
    print(a[i] , end=" ")

#insert()
a.insert(1,4)
print("Printing array in after insert : ")
