from abc import ABC, abstractmethod
from typing import Any, Callable, NoReturn, override

type Result[T, E] = Ok[T, E] | Err[T, E]


class _Result[T, E](ABC):
    @abstractmethod
    def is_ok(self) -> bool: ...

    @abstractmethod
    def is_err(self) -> bool: ...

    @abstractmethod
    def unwrap(self) -> Any: ...

    @abstractmethod
    def unwrap_err(self) -> Any: ...

    @abstractmethod
    def map[U](self, op: Callable[[T], U]) -> Result[U, E]:
        pass

    # called and_then in Rust
    @abstractmethod
    def fmap[U](self, op: Callable[[T], Result[U, E]]) -> Result[U, E]:
        pass


class Ok[T, E](_Result[T, E]):
    def __init__(self, value: T) -> None:
        self.value = value
        super().__init__()

    @override
    def is_ok(self) -> bool:
        return True

    @override
    def is_err(self) -> bool:
        return False

    @override
    def unwrap(self) -> T:
        return self.value

    @override
    def unwrap_err(self) -> NoReturn:
        raise RuntimeError("Can not unwrap_err from Ok value")

    @override
    def map[U](self, op: Callable[[T], U]) -> Result[U, E]:
        return Ok(op(self.value))

    @override
    def fmap[U](self, op: Callable[[T], Result[U, E]]) -> Result[U, E]:
        return op(self.value)


class Err[T, E](_Result[T, E]):
    def __init__(self, err: E) -> None:
        self.err = err
        super().__init__()

    @override
    def is_ok(self) -> bool:
        return False

    @override
    def is_err(self) -> bool:
        return True

    @override
    def unwrap(self) -> NoReturn:
        # Use exception to simulate panic
        raise RuntimeError(str(self.err))

    @override
    def unwrap_err(self) -> E:
        return self.err

    @override
    def map[U](self, op: Callable[[T], U]) -> Result[U, E]:
        return Err(self.err)

    @override
    def fmap[U](self, op: Callable[[T], Result[U, E]]) -> Result[U, E]:
        return Err(self.err)
