from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed: int) -> None:
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz) -> None:
        if self._cords[2] + dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self) -> None:
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self) -> None:
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self) -> None:
        print(self.sound)


class Bird(Animal):
    beak = True

    def __init__(self, speed: int) -> None:
        super().__init__(speed)

    def lay_eggs(self) -> None:
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed: int) -> None:
        super().__init__(speed)

    def dive_in(self, dz) -> None:
        self.speed //= 2
        self._cords[2] -= abs(dz) * self.speed


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed: int) -> None:
        super().__init__(speed)


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

    def __init__(self, speed: int) -> None:
        super().__init__(speed)


db = Duckbill(10)

print(db.live)

print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()
