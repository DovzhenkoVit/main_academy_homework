import string
import random


def rand_word():
    word = random.sample(string.ascii_letters, 10)
    word = (''.join(word).lower())

    print(word)

    for a in word:
        print(f"{a} встречается {word.count(a)} раз")


if __name__ == '__main__':
    rand_word()
