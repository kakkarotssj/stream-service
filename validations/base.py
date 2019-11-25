from abc import ABC, abstractmethod


class ValidatorBase(ABC):
    exception = None
    error = None
    error_code = None

    @classmethod
    @abstractmethod
    def validate(cls, *args, **kwargs):
        pass

    def raise_exception(cls, data):
        cls.error.raise_exception(
            cls.error_code,
            data,
            cls.exception
        )
