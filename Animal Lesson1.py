class Animal:
    def __init__(self, name: str, food: str, sleep: int):
        self.name = name
        self.food = food
        self.sleep = sleep

    def say(self):
        print(123)

class Cat(Animal):
    def __init__(self, name: str, weasel: str, coarseness: str, food: str, sleep: int, breed: str, grow: int, play: str):
        super().__init__(name, food, sleep)
        self.weasel = weasel
        self.coarseness = coarseness

    def purr(self):
        print("cat purr")

    def scratch(self):
        print("cat scratch")

    def breed(self):
        print("breeding cat")
    def changeAge(self):
        print("the cat's age changes")
    def play(self):
        print("Cat playing")

    # def say(self):
        print(45)

class Dog(Animal):
    def __init__(self, name: str, walk: int, loylaty: str, training, food: str, sleep: str, breed: str, bark: str, play: str):
        self.walk = walk
        self.loylaty = loylaty
        self.trainig = training

    def walking(self):
        print("Walking the dog")

    def service(self):
        print("Dog service")

    def servic(self):
        print("Visit to the dog trainer")

    def breeding(self):
        print("Dog breed")
    def barking(self):
        print("The dog barks")
    def playing(self):
        print("Dog love play")

animal = Animal("Friends",  "jkj",  16)

animal.say()

cat1 = Cat( "Murka", "yes",  16,  "Wiskas", "scold", "британец", 2, "догонялки")
cat1.say()
cat1.purr()
cat1.scratch()
cat1.breed()
cat1.changeAge()
cat1.play()

dog1 = Dog("Nik",  4,  "always",  "regularly",  "Chappi", 16, "Корги", "гав", "ball")
dog1.say()
dog1.walking()
dog1.service()
dog1.servic()
dog1.breeding()
dog1.barking()
dog1.playing()