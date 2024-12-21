
class animal :
    def speak() :
        print("Animal can make sound")

class dog(animal):
    def speak():
        print("Dog can bark")        

class cat(animal):
    def speak():
        print("Cat can meow")

print("Orginal Method  : " , animal.speak())
print("Method overriding 1: " + dog.speak())
print("Method overriding 2: " + cat.speak())

