from .base import ValidatorBase
from constants import VALID_SERVICES, VALID_ACTIVITIES, VALID_EXTRAS
from errors.errors import ArgumentVariableError
from errors.exceptions import InvalidActivityException
from errors.exceptions import InvalidArgumentLengthException
from errors.exceptions import InvalidExtrasException
from errors.exceptions import InvalidServiceException


class ValidateArgumentLength(ValidatorBase):
    error = ArgumentVariableError
    error_code = ArgumentVariableError.INVALID_ARGUMENTS_LENGTH
    exception = InvalidArgumentLengthException

    @classmethod
    def validate(cls, *args, **kwargs):
        if len(args) < 2:
            cls.raise_exception(ValidateArgumentLength, {'data': args})


class ValidateService(ValidatorBase):
    error = ArgumentVariableError
    error_code = ArgumentVariableError.INVALID_SERVICE
    exception = InvalidServiceException

    @classmethod
    def validate(cls, *args, **kwargs):
        service = kwargs['service']

        if service not in VALID_SERVICES:
            cls.raise_exception(ValidateService, {'data': VALID_SERVICES})


class ValidateActivity(ValidatorBase):
    error = ArgumentVariableError
    error_code = ArgumentVariableError.INVALID_ACTIVITY
    exception = InvalidActivityException

    @classmethod
    def validate(cls, *args, **kwargs):
        service = kwargs['service']
        activity = kwargs['activity']

        if activity not in VALID_ACTIVITIES[service]:
            cls.raise_exception(ValidateActivity, {'data': VALID_ACTIVITIES})


class ValidateExtras(ValidatorBase):
    error = ArgumentVariableError
    error_code = ArgumentVariableError.INVALID_EXTRAS
    exception = InvalidExtrasException

    @classmethod
    def validate(cls, *args, **kwargs):
        service = kwargs['service']
        activity = kwargs['activity']
        extras = kwargs['extras']

        # TO-DO: also add for valid extras, fetched from db later.
        if len(extras) != len(VALID_EXTRAS[service][activity]):
            cls.raise_exception(ValidateExtras, {'data': VALID_EXTRAS})
