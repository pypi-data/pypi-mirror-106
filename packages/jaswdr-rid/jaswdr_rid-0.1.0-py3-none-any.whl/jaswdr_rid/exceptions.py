class ResourceError(Exception):
    pass


class InvalidResourceError(ResourceError):
    pass


class NotResourceError(ResourceError):
    pass
