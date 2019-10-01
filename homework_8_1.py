import os


class ContextClass:
    flag = 0

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def _create_file(self):
        if os.path.isfile(self.filename) is False:
            print("File does not exist.")
            new_file = input(
                "Do you want to create a new file? (y/n)\n"
            )
            if new_file.lower() == "y":
                file_type = input(
                    "Create temporary or permanent file? (t/p)\n"
                )
                if file_type.lower() == "t":
                    self.flag = 1

                self.open_file = open(self.filename, self.mode)

            elif new_file.lower() == "n":
                raise FileNotFoundError
        else:
            self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __enter__(self):
        return self._create_file()

    def __exit__(self, *args):
        if self.flag == 1:
            os.remove(self.filename)
        self.open_file.close()


if __name__ == "__main__":
    with ContextClass("test.txt", "w") as infile:
        a = infile.write("test\n")
