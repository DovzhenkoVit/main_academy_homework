class CircleFunc:
    pi = 3.14

    @classmethod
    def circle_length(cls, radius):
        return 2 * radius * cls.pi

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2


class SphereFunc:
    pi = 3.14

    @classmethod
    def sphere_volume(cls, radius):
        return (4 / 3) * cls.pi * radius ** 3

    @classmethod
    def sphere_area(cls, radius):
        return 4 * cls.pi * radius ** 2
