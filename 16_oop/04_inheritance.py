class Animal:
    location = "Australia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now....")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")


d = Dog("Bruno")
d.speak()
