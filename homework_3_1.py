from string import ascii_letters
from random import sample, choice


def do_dict():
    str_list = []
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    dict1 = {}

    for i in range(10):
        rand_str = ''.join((sample(ascii_letters, choice(range(2, 10)))))

        str_list.append(rand_str)

        dict1[str_list[i]] = int_list[i]

    print(str_list)
    print(dict1)


if __name__ == '__main__':
    do_dict()
