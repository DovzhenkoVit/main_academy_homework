class FreezeClass:
    flag = None

    def freeze(self):
        self.flag = True

    def unfreeze(self):
        object.__setattr__(self, "flag", False)

    def __setattr__(self, key, value):
        if self.flag:
            raise AttributeError("Class is frozen")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if self.flag:
            raise AttributeError("Class is frozen")
        object.__delattr__(self, item)
