# l6_package/cli.py

import argparse
from l6_package.version import __version__

def main():
    parser = argparse.ArgumentParser(
        description="L6 Package Command-Line Tool"
    )

    parser.add_argument(
        "--version", action="version", version=f"L6 Package {__version__}"
    )

    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="The operation to perform",
    )

    parser.add_argument(
        "x", type=float, help="The first number"
    )
    parser.add_argument(
        "y", type=float, help="The second number"
    )

    args = parser.parse_args()

    if args.operation == "add":
        result = args.x + args.y
    elif args.operation == "subtract":
        result = args.x - args.y
    elif args.operation == "multiply":
        result = args.x * args.y
    elif args.operation == "divide":
        if args.y == 0:
            raise ValueError("Division by zero is not allowed.")
        result = args.x / args.y

    print(f"Result: {result}")
