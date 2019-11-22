from .base import ValidatorBase
from constants import VALID_SERVICES, VALID_ACTIVITIES, VALID_EXTRAS
from errors.errors import ArgumentVariableError
from errors.exceptions import InvalidActivityException
from errors.exceptions import InvalidArgumentLengthException
from errors.exceptions import InvalidExtrasException
from errors.exceptions import InvalidServiceException


class ValidateArgumentLength(ValidatorBase):
    error_code = ArgumentVariableError.INVALID_ARGUMENTS_LENGTH

    @classmethod
    def validate(cls, *args, **kwargs):
        if len(args) < 2:
            issue = ValidateArgumentLength.error_code.name
            help = ValidateArgumentLength.error_code.value
            data = {'data': args}

            raise InvalidArgumentLengthException(issue, help, data)


class ValidateService(ValidatorBase):
    error_code = ArgumentVariableError.INVALID_SERVICE

    @classmethod
    def validate(cls, *args, **kwargs):
        service = kwargs['service']

        if service not in VALID_SERVICES:
            issue = ValidateService.error_code.name
            help = ValidateService.error_code.value
            data = {'data': VALID_SERVICES}

            raise InvalidServiceException(issue, help, data)


class ValidateActivity(ValidatorBase):
    error_code = ArgumentVariableError.INVALID_ACTIVITY

    @classmethod
    def validate(cls, *args, **kwargs):
        service = kwargs['service']
        activity = kwargs['activity']

        if activity not in VALID_ACTIVITIES[service]:
            issue = ValidateActivity.error_code.name
            help = ValidateActivity.error_code.value
            data = {'data': VALID_ACTIVITIES}

            raise InvalidActivityException(issue, help, data)


class ValidateExtras(ValidatorBase):
    error_code = ArgumentVariableError.INVALID_EXTRAS

    @classmethod
    def validate(cls, *args, **kwargs):
        service = kwargs['service']
        activity = kwargs['activity']
        extras = kwargs['extras']

        # TO-DO: also add for valid extras, fetched from db later.
        if len(extras) != len(VALID_EXTRAS[service][activity]):
            issue = ValidateExtras.error_code.name
            help = ValidateExtras.error_code.value
            data = {'data': VALID_EXTRAS}

            raise InvalidExtrasException(issue, help, data)
