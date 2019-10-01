def cycle_func():
    last_n = int(input("Enter the last number: "))
    main_list = []

    for i in range(2, last_n + 1):
        if i not in main_list:
            print(i)
            for j in range(i * i, last_n + 1, i):
                main_list.append(j)


if __name__ == '__main__':
    cycle_func()
