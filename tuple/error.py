from typing import Protocol, Tuple

# Technically not enforced by Golang but it is assumed by convention
type GoTuple[T, E] = Tuple[T, None] | Tuple[None, E]


class Error(Protocol):
    def error(self) -> str: ...


class ProjectError:
    def __init__(self, message: str) -> None:
        self.message = message

    def error(self) -> str:
        return self.message
