# 4. program to read the contents from a file and display on console

file = open(r'C:\Users\Athar\OneDrive\Documents\Python\file1.txt')
print(file.read())

# 5. program to read the contents from a one file and write into another file 
input_location =r'C:\Users\Athar\OneDrive\Documents\Python\file1.txt'
with open(input_location,'r') as input_file:
    data = input_file.read()

output_location = r'C:\Users\Athar\OneDrive\Documents\Python\file2.txt'
with open(output_location,'w') as output_file:
     output_file.write(data)

# 6. program to display file available in current directory 
