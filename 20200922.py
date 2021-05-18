from attr import attrs, attrib


@attrs
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Chris', 32)
p2 = Person('chris', 32)

print(p1 == p2)