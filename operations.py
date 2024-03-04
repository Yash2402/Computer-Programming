def add(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


def multiply(x, y):
    return x * y


def substract(x, y):
    return x - y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Division by zero is not allowed!")
