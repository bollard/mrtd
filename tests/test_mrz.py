import unittest

from mrtd.mrz import check_digit


class TestMachineReadableZone(unittest.TestCase):
    def test_check_digit(self):
        test_cases = [
            ("AB2134<<<", 5),
            ("559556128", 6),
            ("900703", 5),
            ("290327", 5),
            ("559556128690070352903275", 0),
        ]

        for chars, expected in test_cases:
            with self.subTest(chars=chars, expected=expected):
                self.assertEqual(check_digit(chars), expected)
