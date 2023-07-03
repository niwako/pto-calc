#!/usr/bin/env python3

import datetime
import argparse


def calculate(
    as_of: datetime.date,
    current_pto: float = 0,
    daily_accrual_rate: float = 15 * 8 / 365,
) -> float:
    delta = as_of - datetime.date.today()
    delta = delta.days
    pto_as_of = current_pto + delta * daily_accrual_rate
    return pto_as_of


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--as-of",
        type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d").date(),
        help="A date in the future in the form of yyyy-mm-dd",
        required=True,
    )
    parser.add_argument(
        "--current-pto",
        type=float,
        help="Currently available PTO hours, defaults to 0",
        default=0,
    )
    parser.add_argument(
        "--pto-days",
        type=float,
        help="Number of PTO days offered per year, defaults to 15",
        default=15,
    )
    args = parser.parse_args()

    pto_as_of = calculate(args.as_of, args.current_pto, args.pto_days * 8 / 365)
    print(pto_as_of)


if __name__ == "__main__":
    main()
