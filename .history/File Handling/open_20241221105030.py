
try:
    with open("file1.txt","r") as file:
        contet
except FileNotFoundError:
    print("File not found")


