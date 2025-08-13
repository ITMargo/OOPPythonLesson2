from time import sleep


class Animal:
    def __init__(self, name: str, food: str, sleep: int):
        self.name = name
        self.food = food
        self.sleep = sleep

    def say(self):
        print(123)

class Cat(Animal):
    def __init__(self, name: str, weasel: str, coarseness: str, food: str, sleep: int):
        super().__init__(name, food, sleep)
        self.weasel = weasel
        self.coarseness = coarseness

    def purr(self):
        print("cat purr")

    def scratch(self):
        print("cat scratch")

    def say(self):
        print(45)

class Dog(Animal):
    def __init__(self, name: str, walk: int, loylaty: str, training, food: str, sleep: str):
        self.walk = walk
        self.loylaty = loylaty
        self.trainig = training

    def walking(self):
        print("Walking the dog")

    def service(self):
        print("Dog service")

    def servic(self):
        print("Visit to the dog trainer")

animal = Animal("Friends",  "jkj",  16)

animal.say()

cat1 = Cat( "Murka", "yes",  16,  "Wiskas", "scold")
cat1.say()
cat1.purr()
cat1.scratch()

dog1 = Dog("Nik",  4,  "always",  "regularly",  "Chappi", 16)
dog1.say()
dog1.walking()
dog1.service()
dog1.servic()