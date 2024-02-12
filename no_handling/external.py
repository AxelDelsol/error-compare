import random


class HttpError(RuntimeError):
    def __init__(self, status_code: int, msg: str) -> None:
        super().__init__(f"Code {status_code} : {msg}")


def call_external(value: int) -> int:
    if value <= 200:
        return random.randint(0, 20)
    elif 400 <= value < 500:
        raise HttpError(
            status_code=400,
            msg=f"Invalid request with {value}. It should be lower than 200",
        )
    else:
        raise HttpError(status_code=500, msg=f"Unknown error with {value}")
