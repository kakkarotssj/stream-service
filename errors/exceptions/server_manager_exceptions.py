from .base import ExceptionBase


class StreamAlreadyExistsException(ExceptionBase):
    """
    will be raised when stream already exists while adding new stream
    """


class StreamDoesNotExistsException(ExceptionBase):
    """
    will be raised when stream does not exists while deleting stream with that name
    """


class TopicAlreadyExistsException(ExceptionBase):
    """
    will be raised when user try to add topic existing topic in the stream
    """


class TopicDoesNotExistsException(ExceptionBase):
    """
    will be raised when user try to delete non-existing topic in the stream
    """
