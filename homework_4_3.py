def read_file():
    f = open(__file__)            # Variant 1
    print(f.read())
    f.close()

    with open(__file__) as f:     # Variant 2
        print(f.read())


if __name__ == '__main__':
    read_file()
