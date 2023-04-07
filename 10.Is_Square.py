from math import sqrt
def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    elif n**0.5 % 1 == 0:
        return True
    return False

print(is_square(25))
print(is_square(17))