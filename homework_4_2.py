def pyramid_func():
    stairs = int(input("Enter the number of stairs: "))

    for i in range(1, stairs + 1):
        print((" " * (stairs - i) + ("* " * i)))


if __name__ == '__main__':
    pyramid_func()
