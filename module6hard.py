from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled: bool = True) -> None:
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def __len__(self) -> int:
        return sum(self.__sides)

    def get_color(self):
        return list(self.__color)

    @staticmethod
    def __is_valid_color(r: int, g: int, b: int) -> bool:
        valid = range(0, 256)
        return r in valid and g in valid and b in valid

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *args) -> bool:
        return all(map(lambda x: isinstance(x, int) and x >= 0, args)) and len(args) == len(self.__sides)

    def get_sides(self) -> list[int]:
        return list(self.__sides)

    def set_sides(self, *new_sides) -> None:
        if len(new_sides) == self.__class__.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list[int], *sides: list[int]) -> None:
        super().__init__(color, *sides)
        self._Figure__sides = self._Figure__sides if len(sides) == self.__class__.sides_count else [1]
        self.__radius = self._Figure__sides[0] / 2 * pi

    def get_square(self) -> float:
        return pi * self.__radius ** 2


class Rectangle(Figure):
    sides_count = 3

    def __init__(self, color: list[int], *sides: list[int]) -> None:
        super().__init__(color, *sides)
        self._Figure__sides = self._Figure__sides if len(sides) == self.__class__.sides_count else [1, 1, 1]

    def get_square(self) -> float:
        p = 1 / 2 * (self.__sides[0] + self.__sides[1] + self.__sides[2])
        return (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides) -> None:
        super().__init__(color, *sides)
        self._Figure__sides = [self._Figure__sides[0] for _ in range(12)] if len(sides) == 1 else [1 for _ in range(12)]

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77)  # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится

print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится

print(cube1.get_sides())

circle1.set_sides(15)  # Изменится

print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())
