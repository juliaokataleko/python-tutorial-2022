class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Iam {self.name} and iam {self.age} years old")

    def speak(self):
        print("I don't know what to say...")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"Iam {self.name}, iam {self.age} years old and iam {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 29)
p.speak()

c = Cat("Bill", 34, "Blue")
c.show();

d = Dog("Jill", 25)
d.show()

f = Fish("Fish", 10)
f.speak()