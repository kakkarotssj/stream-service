from abc import ABC, abstractmethod


class ValidatorBase(ABC):
    error_code = None

    def get_error_code(self):
        return self.error_code  # returns error_code

    @classmethod
    @abstractmethod
    def validate(cls, *args, **kwargs):
        pass
