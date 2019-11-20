from .base import ErrorBase


class ArgumentVariableError(ErrorBase):
	"""
	defines all errors related to argument variables provided
	"""

	INVALID_ARGUMENTS_LENGTH = 'Invalid Number Of Arguments Provided'
	INVALID_SERVICE = 'Invalid Service Provided'
	INVALID_ACTIVITY = 'Invalid Activity Provided For Given Service'
	INVALID_EXTRAS = 'Invalid Extras Provided For Given Service And Activity'
