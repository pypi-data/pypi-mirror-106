import logging
import sys
import typing as t

if sys.version_info.minor >= 8:
    from typing import Literal
else:
    from typing_extensions import Literal


class _Validater:

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: t.Any) -> t.Any:
        raise NotImplementedError


class Logger_t(_Validater):

    @classmethod
    def validate(cls, v: t.Any) -> logging.Logger:
        if not isinstance(v, logging.Logger):
            raise ValueError(f"{v} is not a logging.Logger.")
        return v


class LoggerClass_t(_Validater):

    @classmethod
    def validate(cls, v: t.Any) -> t.Type[logging.Logger]:
        if not issubclass(v, logging.Logger):
            raise ValueError(f"{v} is not a subclass of logging.Logger.")
        return v
