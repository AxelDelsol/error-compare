from typing import Optional

from error import Error, ProjectError


def validate(value: int) -> Optional[Error]:
    if value < 0 or value > 9:
        return ProjectError(
            f"Invalid value: {value}. It should be between 0 and 9 inclusive"
        )

    return None
