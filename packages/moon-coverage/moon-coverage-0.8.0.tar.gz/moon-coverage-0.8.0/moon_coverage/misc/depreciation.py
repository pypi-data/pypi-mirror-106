"""Depreciation decorator."""

from functools import wraps
from inspect import getmro

from .logger import logger


warn, _ = logger('DepreciationWarning')


def depreciated_renamed(cls):
    """Depreciation rename decorator."""

    @wraps(cls, updated=())
    class DeprecationRenamed(cls):
        """Depreciation renamed class."""

        def __init__(self, *args, **kwargs):
            warn.warning(
                'Class `%s` has been renamed `%s`. '
                'Please update your code to use this new denomination.',
                cls.__name__,
                getmro(cls)[1].__name__
            )

            super().__init__(*args, **kwargs)
            self.__doc__ = '[Depreciated] ' + self.__doc__

    return DeprecationRenamed
