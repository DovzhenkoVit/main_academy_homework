import os
from os.path import isfile, isdir, join


inp_path = input("Input the directory:")


def _tuples_list(path):
    full_path = os.listdir(path)

    dirs = [
        directory for directory in full_path
        if isdir(join(path, directory))
    ]

    files = [
        file for file in full_path
        if isfile(join(path, file))
    ]

    return path, dirs, files


def walker(somepath):
    result = []

    def walker_inner(somepath):
        a = _tuples_list(somepath)
        for directory in a[1]:
            b = (join(somepath, directory))
            result.append(_tuples_list(b))
            walker_inner(b)
        return result
    return walker_inner(somepath)


if __name__ == '__main__':
    for i in walker(inp_path):
        print(i)
