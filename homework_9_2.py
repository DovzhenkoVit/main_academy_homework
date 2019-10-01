class MyIter:

    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        self.line = self.file.readline()
        if not self.line:
            raise StopIteration
        return self.line

    def __add__(self, other):
        return self.line + other

    def __mul__(self, other):
        return self.line * other

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
