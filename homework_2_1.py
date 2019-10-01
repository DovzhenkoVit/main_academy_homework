def words_in_text():
    text = input("Введите текст: ").lower()
    word = input("Слово: ").lower()

    a = text.count(word)

    print("Слово {}  встречается в этом предложении {} раз".format(word, a))


if __name__ == '__main__':
    words_in_text()
