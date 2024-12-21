input_file = r"C:\Users\Athar\OneDrive\Documents\Python\file2.txt"

try:
    with open("file1.txt","w+") as file:
        content = file.read()
        file.write("ATHARV PRAVIN BABAR")
        print(content)

except FileNotFoundError:
    print("File not found")


