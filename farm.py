class Animal(object):

    def __init__(self, breed, quantity):
        self.quantity = quantity
        self.breed = breed

    def description(self):
        return "The farm has {} of {} quantity".format(self.breed, self.quantity)


class Sheep(Animal):

    def speak(self, sound):
        return "The {} sounds {}".format(self.breed,sound)


class Cow(Animal):

    def provides(self, item):
        return "The {} provides {}".format(self.breed,item)


jonny = Sheep("Germen Sheperd",30)
print(jonny.description())
print(jonny.speak("meeh meeh"))

althiya = Cow("Foreign",20)
print(althiya.description())
print(althiya.provides("milk"))
