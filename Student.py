class Student:

    all_students = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.all_students.append(self)

    def __repr__(self):
        return '{name: ' + self.name + ', age: ' + str(self.age) + '}'

    # def __str__(self):
    #     return 'Person(name=' + self.name + ', age=' + str(self.age) + ')'





