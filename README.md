# error-compare
This project compares different error handling mecanisms found in various languages.

## Context

The goal is to implement a `do_something` function that takes an `int` and returns a `bool`.

The function does the following operations:

1. Validate the input value
1. Open/create a file (it emulates resource aquisition)
1. Make an API call to retrieve a value from the input (the API call is made using an external library that can not be modified)
1. Write the API response to the file
1. Close the file
1. Process the API result and return

Each step may generate an error and as a developer, we must properly handle them. This project tries four differents error handling mecanism found in common languages nowadays and asks the following questions:

1. How easy is it for an end user to fill a ticket / ask for help when an error occurs ? It implies that he does not know ANYTHING about the code. He could be a client trying to add an item to his cart and gets an error.
1. If `do_something` was part of a library, can you easily know whether you incorrectly use the function or you should fill a github issue.
1. You are asked to maintain the code, how hard is it to get started ?


## Error handling

- [x] No handling
- [x] Exception (native python)
- [ ] Result monad (functional programming & Rust)
- [ ] Tuple (golang style)

### No handling

It does not handle any errors and only focus on the "happy path".

This methods is not recommended for production code. Only use it for PoC or if you want to get started with a new tool.

---
1. The user has no idea how to report the except "it fails when I did this". A lot of some is wasted trying to reproduce the issue.
1. Unless a good documentation is written, a developer using `do_something` can not tell whether the function raises an error or not.
1. Knowing which exception to raise and where it is used requires to read the internal of each function. It may be fine on a small project, but becomes really complicated.


### Exception

Exception is the most popular way to handle errors. Many languages use it: C++, Python, Java... When an error occurs, an exception is raised/thrown. This causes the program to stop its "normal" execution and the exception is propagated up the calling stack until it is catched or the program crashes.

Exceptions are handled at the language level. It provides a way to raise/throw an error, to catch an error and (sometimes) execute code before the propagation.

1. The user can now report the stack trace and the associated notes that the author of `do_something` added to help with debugging.
1. Unless a good documentation is written, a developer using `do_something` can not tell whether the function raises an error or not.
1. Knowing which exception to raise and where it is used is a bit simpler with the try/except keywords. The note feature of python's exception allows to help ourselves in the future by adding extra comments to an error.

### Result

Languages such as Haskell or Rust do not have exceptions. Instead, they use their type system to encode when an error occurs.

In simple term, Result is a type that can either contain a value or an error. Functions that may generate an error return a Result and the caller decide what to do with it.

### Tuple

Golang takes a different approach. It is based on two features: (i) anything has a "null value" and (ii) a function can return multiple values.
Thus, an idiomatic way to indicate that an error occurs is to make your function returns a tuple (value, error). If the function is successful, error is set to  nil and value contains the "real" function return. If there is an error, value contains its "null value" and the error contains a useful object (it actually implements the error interface).