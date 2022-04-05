class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('tim')
p2 = Person('till')

# print(p1.number_of_people)
# print(p2.number_of_people)

# print(Person.number_of_people_())
# static methods

class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def run():
        print("run...")

Math.run()