import logging
from typing import Any, Type


class _Validater:

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> Any:
        raise NotImplementedError


class Logger_t(_Validater):

    @classmethod
    def validate(cls, v: Any) -> logging.Logger:
        if not isinstance(v, logging.Logger):
            raise ValueError(f"{v} is not a logging.Logger.")
        return v


class LoggerClass_t(_Validater):

    @classmethod
    def validate(cls, v: Any) -> Type[logging.Logger]:
        if not issubclass(v, logging.Logger):
            raise ValueError(f"{v} is not a subclass of logging.Logger.")
        return v
