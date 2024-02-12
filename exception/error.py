# We define a custom exception class to avoid leaking dependencies' errors.
class ProjectError(RuntimeError):
    pass
