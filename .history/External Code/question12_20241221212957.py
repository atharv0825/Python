
class animal :
    def speak() :
        print("Animal can make sound")

class dog(animal):
    def speak():
        print("Dog can bark")        

class cat(animal):
    def speak():
        print("Cat can meow")

print(animal.speak())
print(dog.speak())
print("Method overriding 2: " , cat.speak())

