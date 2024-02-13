import argparse

from external import HttpError, call_external
from result import Err, Ok, Result
from validation import validate


def external(id: int) -> Result[int, str]:
    try:
        return Ok(call_external(id))
    except HttpError as exc:
        return Err(f"External API error with {id} : {exc}")


def do_something(id: int) -> Result[bool, str]:
    valid = validate(id)

    if valid.is_err():
        return Err(valid.unwrap_err())

    with open("monad.log", mode="a") as f:
        output = external(100 * id + id)
        match output:
            case Ok(value=v):
                f.write(f"The value is {v}")
                return Ok(v % 2 == 0)
            case Err(err=e):
                return Err(e)


# The monadic approach suggest a refactor
def do_something_refactor(id: int) -> Result[bool, str]:
    res = validate(id).fmap(lambda i: external(100 * id + id)).map(lambda v: v % 2 == 0)

    if res.is_ok():
        with open("monad.log", mode="a") as f:
            f.write(f"The value is {res.unwrap()}\n")

    return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", type=int)
    args = parser.parse_args()

    id = args.id
    # result = do_something(id)
    result = do_something_refactor(id)
    match result:
        case Ok(value=v):
            print(f"The result is : {v}")
        case Err(err=e):
            # Simulate panic and ensure that the program returns non zero
            raise RuntimeError(f"Failed to call do_something with id={id} : {e}")


if __name__ == "__main__":
    main()
