input_file = rC:\Users\Athar\OneDrive\Documents\Python\file2.txt

try:
    with open("file1.txt","r+") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found")

