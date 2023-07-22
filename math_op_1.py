"""
任意类型的数值运算
"""

from dataclasses import dataclass

@dataclass
class Vector:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        # subtract
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        # multiply
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        # divide
        return Vector(self.x / scalar, self.y / scalar)
    
    def __floordiv__(self, scalar):
        # floor divide
        return Vector(self.x // scalar, self.y // scalar)

if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * 2)
    print(v1 / 2)
    print(v1 // 2)