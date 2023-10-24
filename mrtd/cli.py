import argparse

from mrtd.mrz import check_digit


def main() -> None:
    parser = argparse.ArgumentParser(description="Produce check digit")
    parser.add_argument(
        dest="check",
        type=str,
        help="String to produce check digit for",
    )

    args = parser.parse_args()
    print(check_digit(args.check))


if __name__ == "__main__":
    main()
