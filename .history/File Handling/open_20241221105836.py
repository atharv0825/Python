input_file = r"C:\Users\Athar\OneDrive\Documents\Python\file2.txt"

try:
    with open("file1.txt","r+") as file:
        content = file.read()
        file.w
        print(content)

except FileNotFoundError:
    print("File not found")

