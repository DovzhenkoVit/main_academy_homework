class Animal:
    def __init__(self, size, breed, weight):
        self.size = size
        self.breed = breed
        self.weight = weight

    def breeding(self, other):
        if not isinstance(other, self.__class__):
            raise RuntimeError("Species should be similar!")

        size = (self.size + other.size) / 2

        if self.size >= other.size:
            breed = self.breed
        else:
            breed = other.breed

        weight = (self.weight + other.weight) / 2

        animal3 = self.__class__(size, breed, weight)
        return animal3

    def show_param(self):
        result = f"Size: {self.size}, " \
                 f"Breed: {self.breed}, " \
                 f"Weight: {self.weight} "
        return result

    @staticmethod
    def action(value):
        return print(value)

    @staticmethod
    def voice(value):
        return print(value)

    def eat(self, food_type):
        if food_type.lower() == "fish":
            self.weight += 0.2
        elif food_type.lower() == "meat":
            self.weight += 0.3


class FlyMixin:
    @staticmethod
    def takeoff():
        return print("Take off")

    @staticmethod
    def fly():
        return "Fly"

    @staticmethod
    def landing():
        return "Landing"


class DigMixin:
    @staticmethod
    def dig():
        return "Dig"


class Birds(Animal, FlyMixin):
    @staticmethod
    def kung_fu():
        return "I know kung fu"


class Crane(Birds):
    pass


class Stork(Birds):
    pass


class Mosquito(Animal, FlyMixin):
    pass


class TheFly(Animal, FlyMixin):
    pass


class Mole(Animal, DigMixin):
    pass


class Cat(Animal):
    def eat(self, food_type):
        if food_type.lower() == "fish":
            self.weight += 0.3
        super().eat(food_type)


class Dog(Animal):
    def eat(self, food_type):
        if food_type.lower() == "meat":
            self.weight += 0.2
        super().eat(food_type)


if __name__ == '__main__':
    Stork1 = Stork(3, "Crane1", 5)
    Stork2 = Stork(4, "Crane2", 4)
    Stork3 = Stork1.breeding(Stork2)
    print(Stork1.fly())
    print(Stork3.landing())
    print(Stork3.show_param())
