lst = [1, 2, 3, 45, 6, 3, 5, 23, 6, 5, 543, 76, 32, 75]
iseven = lambda x: True if x % 2 == 0 else False
square = lambda x: x * x
lstOfSquares = list(map(square, lst))
even_no = list(filter(iseven, lst))
print(lst)
print(f"Square of each number in the above list: {lstOfSquares}")
print(f"Even numbers in the above list: {even_no}")


import operations

print(operations.add(23, 4, 5, 346, 234))
print(operations.substract(29, 15))
print(operations.multiply(23, 45))
print(operations.divide(24, 6))

import math
import random

print("sin(30) =", math.sin(math.radians(30)))
print("abs(-34) =", math.fabs(-34))
print("These are 5 random integer between 1 and 100 (including both 1 and 100):")
for _ in range(5):
    print(random.randint(1, 100))
