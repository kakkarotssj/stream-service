from .base import ExceptionBase


class StreamAlreadyExistsException(ExceptionBase):
    """
    will be raised when stream already exists while adding new stream
    """


class StreamDoesNotExistsException(ExceptionBase):
    """
    will be raised when stream does not exists while deleting stream with that name
    """
