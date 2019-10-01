from random import randint


def authentication():
    dict1 = {
        "Human": ["pass", randint(-100, 100)],
        "Robot": ["i`m human", randint(-100, 100)],
        "machine": ["01000110", randint(-100, 100)],
        "somebody": ["blah!", randint(-100, 100)],
        "Cool Bob": ["bob the cool", randint(-100, 100)],
        "Boring Bob": ["12345", randint(-100, 100)],
        "Not a Bob": ["54321", randint(-100, 100)],
        "Todd H": ["buy it!", randint(-100, 100)],
        "Bob R": ["just a little accident", randint(-100, 100)],
        "me": ["ME!", randint(-100, 100)]
    }

    login = input("Login: ")

    if login not in dict1:

        dict1[login] = [
            input("Enter your password: "), randint(-100, 100)
        ]

    print(dict1[login][1])


if __name__ == '__main__':
    authentication()
