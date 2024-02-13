import argparse

from external import call_external
from validation import validate


def do_something(id: int) -> bool:
    validate(id)

    with open("no_handling.log", mode="a") as f:
        output = call_external(100 * id + id)
        f.write(f"The value is {output}\n")

        return output % 2 == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", type=int)
    args = parser.parse_args()

    id = args.id
    result = do_something(id)
    print(f"The result is : {result}")


if __name__ == "__main__":
    main()
