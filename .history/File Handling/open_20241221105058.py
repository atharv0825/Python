
try:
    with open("file1.txt","r") as file:
        content = file.read
except FileNotFoundError:
    print("File not found")


