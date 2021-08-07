from itertools import cycle
from string import ascii_uppercase


def check_digit(str):
    def to_value(char):
        if char in ascii_uppercase:
            return ascii_uppercase.index(char) + 10
        elif char.isnumeric():
            return int(char)
        else:
            return 0

    values = [to_value(char.upper()) for char in str]
    weights = [w for v, w in zip(values, cycle([7, 3, 1]))]
    product = [v * w for v, w in zip(values, weights)]

    return sum(product) % 10


if __name__ == '__main__':
    assert check_digit('AB2134<<<') == 5

    assert check_digit('559556128') == 6

    assert check_digit('900703') == 5

    assert check_digit('290327') == 5

    assert check_digit('559556128690070352903275') == 0
