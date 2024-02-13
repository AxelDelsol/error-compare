import argparse

from error import ProjectError
from external import HttpError, call_external
from validation import validate


def external(id: int) -> int:
    try:
        return call_external(id)
    except HttpError as exc:
        raise ProjectError(f"External API error with {id}") from exc


def do_something(id: int) -> bool:
    validate(id)

    with open("exception.log", mode="a") as f:
        output = external(100 * id + id)
        f.write(f"The value is {output}\n")

        return output % 2 == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", type=int)
    args = parser.parse_args()

    id = args.id
    try:
        result = do_something(id)
        print(f"The result is : {result}")
    except ProjectError as exc:
        exc.add_note(f"Failed to call do_something with id={id}")
        raise exc


if __name__ == "__main__":
    main()
