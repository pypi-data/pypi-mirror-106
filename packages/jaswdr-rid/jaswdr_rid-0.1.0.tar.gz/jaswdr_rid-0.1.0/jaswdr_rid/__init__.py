__version__ = "0.1.0"

from .exceptions import InvalidResourceError, NotResourceError
from .resource import Resource

__all__ = ["Resource", "InvalidResourceError", "NotResourceError"]
