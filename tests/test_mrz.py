import pytest

from mrtd.mrz import check_digit

@pytest.mark.parametrize("chars, expected", [
    ("AB2134<<<", 5),
    ("559556128", 6),
    ("900703", 5),
    ("290327", 5),
    ("559556128690070352903275", 0),
])
def test_check_digit(chars: str, expected: int):
    assert check_digit(chars) == expected
