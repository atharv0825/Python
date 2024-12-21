input_file = r"C:\Users\Athar\OneDrive\Documents\Python\file2.txt"

try:
    with open("file1.txt","a+") as file:
        content = file.read()
        file.write("VIRAJ PRAVIN BABAR")
        file.seek()
        print(content)

except FileNotFoundError:
    print("File not found")