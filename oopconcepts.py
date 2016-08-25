class Classroom:

    def __init__(self):
        self._people = []   # by convention, attributes with leading '_' are private attributes

    def add_person(self, person):
        self._people.append(person)

    def remove_person(self, person):
        self._people.remove(person)

    def greet(self):
        for person in self._people:
            person.say_hello()


class Person:

    def __init__(self, name):
        self.name = name     # this way we create attribute and assign value to it
        self.x = 9

    def say_hello(self):
        print("Hello, ", self.name)


p1 = Person("Scott")
p1.say_hello()

p2 = Person("Allen")
p2.say_hello()

p3 = Person("Chris")
p2 = p3
p3.name = "Arnold"
p2.say_hello()
p3.say_hello()

print("id(p1): ", id(p1))
print("id(p2): ", id(p2))
print("id(p3): ", id(p3))


room = Classroom()
room.add_person(Person("Scott"))
room.add_person(Person("Poonam"))
room.add_person(Person("Paul"))
room.greet()
