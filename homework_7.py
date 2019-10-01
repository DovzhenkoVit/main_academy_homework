class Animal:
    def __init__(self, size, breed, weight, tail_length):
        self.size = size
        self.breed = breed
        self.weight = weight
        self.tail_length = tail_length
        self.leap_length = (self.weight * 10) / self.tail_length

    def leap(self, leap_param):
        if leap_param <= self.leap_length:
            return print(f"Successful jump on {leap_param}m.")
        else:
            return print(f"Max jump length is {self.leap_length}m")

    def breeding(self, other):
        if not isinstance(other, self.__class__):
            raise RuntimeError("Species should be similar!")

        size = (self.size + other.size) / 2

        breed = self.breed
        if self.breed != other.breed:
            breed = self.breed[0:2] + other.breed[2:]

        weight = (self.weight + other.weight) / 2

        tail_length = (self.tail_length + other.tail_length) / 2

        animal3 = self.__class__(size, breed, weight, tail_length)
        return animal3

    def show_param(self):
        result = f"Size: {self.size}, " \
                 f"Breed: {self.breed}, " \
                 f"Weight: {self.weight}, "\
                 f"Tail length: {self.tail_length}"
        return print(result)

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
    Kuzya = Cat(30, "bombay", 6, 30)
    Cat2 = Cat(20, "murka", 5, 27)

    Bobby = Dog(30, "bobby", 10, 10)
    Dog2 = Dog(25, "doggie", 9, 10)

    Kuzya.leap(5)
    Kuzya.show_param()
    Kitten = Kuzya.breeding(Cat2)

    Kitten.voice("MeoooW")
    Kitten.action("Sleep all day long")
    Kitten.show_param()
    Kitten.eat("Fish")
    Kitten.show_param()
    print("\n")

    Doggie = Dog2.breeding(Bobby)
    Doggie.show_param()
    Doggie.eat("Meat")
    Doggie.show_param()
    Doggie.leap(1.5)
    Doggie.action("Jump on the owner")
