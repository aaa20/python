class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.country = "USA"

person_1 = Person("Bob", "Male")
person_2 = Person("Kate", "Female")

print(person_1.name)
print(person_1.gender)
print(person_1.country)

print(person_2.name)
print(person_2.gender)
print(person_2.country)

