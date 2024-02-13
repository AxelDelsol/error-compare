from result import Err, Ok, Result


def validate(value: int) -> Result[int, str]:
    if value < 0 or value > 9:
        return Err(f"Invalid value: {value}. It should be between 0 and 9 inclusive")

    return Ok(value)
