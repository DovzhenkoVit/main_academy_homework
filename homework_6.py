sort_dict = {}


def register_sort(*name):
    def wrapper(func):
        for sort_type in name:
            sort_dict[sort_type] = func

        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return wrapper


def sort(sort_type, *key):
    def wrapper(func):
        def inner(*args):
            result = sort_dict[sort_type](func(*args), *key)

            return result
        return inner
    return wrapper


@register_sort("bubble")
def bubble_sort(_list, key=lambda x: x):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(_list) - 1):
            left, right = key(_list[i]), key(_list[i + 1])
            if left > right:
                _list[i], _list[i + 1] = _list[i + 1], _list[i]
                swapped = True

    return f"{_list} --> Bubble sort"


@register_sort("quick")
def quick_sort(_list, key=lambda x: x):
    if _list:
        pivot = key(_list[0])

        low = [i for i in _list[1:] if key(i) < pivot]
        high = [i for i in _list[1:] if key(i) > pivot]
        pv_list = [i for i in _list if key(i) == pivot]

        result = quick_sort(low, key) + pv_list + quick_sort(high, key)
        return result
    else:
        return _list


@sort("bubble")
def some_func():
    return [(8, 5), (8, 1), (4, 3), (2, 6)]


@sort("quick", lambda x: x[1])
def other_func(a):
    return a


if __name__ == '__main__':
    print(some_func())
    print(other_func([(8, 5), (8, 3), (4, 1), (2, 6)]))
