
class Dog:

    # construtor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def meow(self):
        return "meow"

    def bark(self):
        print("bark")

    def add_one(self, x):
        return x + 1

d = Dog("Bob", 30)
print(d.get_name())
d.set_age(10)
print(d.get_age())

dog1

