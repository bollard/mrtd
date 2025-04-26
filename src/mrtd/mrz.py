from itertools import cycle
from string import ascii_uppercase


def check_digit(chars: str) -> int:
    def to_value(char: str) -> int:
        if char in ascii_uppercase:
            return ascii_uppercase.index(char) + 10
        elif char.isnumeric():
            return int(char)
        else:
            return 0

    values = [to_value(char.upper()) for char in chars]
    weights = [w for v, w in zip(values, cycle([7, 3, 1]))]
    product = [v * w for v, w in zip(values, weights)]

    return sum(product) % 10
