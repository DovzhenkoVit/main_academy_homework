import random


def homework_1():
    a = random.randint(1000, 1000000)

    b = a // 1000

    print(a)
    print(str(b)[-1])


if __name__ == '__main__':
    homework_1()
