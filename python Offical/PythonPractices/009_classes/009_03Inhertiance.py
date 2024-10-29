class BaseClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


class MathT(BaseClass):
    def __init__(self, x, y):
        super().__init__(x, y)


tt = MathT(3, 5)
print(tt.add())
print(tt.subtract())
print(tt.multiply())
print(tt.divide())

print("-------")
import math
print(dir(math))