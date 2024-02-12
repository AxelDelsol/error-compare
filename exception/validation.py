from error import ProjectError


def validate(value: int):
    if value < 0 or value > 9:
        raise ProjectError(
            f"Invalid value: {value}. It should be between 0 and 9 inclusive"
        )
