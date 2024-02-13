import argparse

from error import Error, GoTuple, ProjectError
from external import HttpError, call_external
from validation import validate


def external(id: int) -> GoTuple[int, Error]:
    try:
        return call_external(id), None
    except HttpError as exc:
        return None, ProjectError(f"External API error with {id} : {exc}")


def do_something(id: int) -> GoTuple[bool, Error]:
    err = validate(id)

    if err is not None:
        return None, ProjectError(f"Validation error with {id}: {err.error()}")

    # Opening a file may fail but we don't model defer here
    with open("tuple.log", mode="a") as f:
        output, err = external(100 * id + id)

        # using if err is not None creates a linter issue for the final return
        if output is None:
            return None, ProjectError(f"API error with {100 * id + id}: {err.error()}")

        f.write(f"The value is {output}\n")

        return output % 2 == 0, None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", type=int)
    args = parser.parse_args()

    id = args.id
    result, err = do_something(id)

    if result is None:
        # double nested if is required to avoid static typing error
        if err is not None:
            # exception to simulate panic
            raise RuntimeError(
                f"Failed to call do_something with id={id} : {err.error()}"
            )
    print(f"The result is : {result}")


if __name__ == "__main__":
    main()
