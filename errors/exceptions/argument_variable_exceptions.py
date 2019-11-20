from .base import ExceptionBase


class InvalidArgumentLengthException(ExceptionBase):
	"""
	will be raised when invalid number of arguments are provided
	"""


class InvalidServiceException(ExceptionBase):
	"""
	will be raised when invalid service is provided
	"""


class InvalidActivityException(ExceptionBase):
	"""
	will be raised when invalid activity as per service is provided
	"""


class InvalidExtrasException(ExceptionBase):
	"""
	will be raised when invalid extras are provided as per service and activity
	"""
