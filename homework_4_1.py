def stairs_func():
    stairs = int(input("Enter the number of stairs: "))

    for i in range(1, stairs + 1):
        print("*" * i)
        print("*" * i)


if __name__ == '__main__':
    stairs_func()
