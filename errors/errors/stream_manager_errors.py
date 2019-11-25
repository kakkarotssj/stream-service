from .base import ErrorBase


class StreamManagerError(ErrorBase):
    """
    defines all errors related to stream manager
    """

    STREAM_ALREADY_EXISTS = "Stream with this name already exist"
    STREAM_DOES_NOT_EXISTS = "Stream with this name does not exist"
