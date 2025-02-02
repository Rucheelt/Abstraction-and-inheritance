from abc import ABC, abstractmethod

class animal(ABC):
    def sound(self):
        pass

class human(animal):
    print("Humans communicate")
class bird(animal):
    print("Birds chirp")
class dog(animal):
    print("Dogs bark")
class cat(animal):
    print("Cats meow")

h=human()
h.sound()
b=bird()
b.sound()
d=dog()
d.sound()
c=cat()
c.sound()
