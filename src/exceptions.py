class BaseExceptionError(Exception):
    description = None


class ObjectNotFound(BaseExceptionError):
    description = "Object not found"


class UserNotFound(BaseExceptionError):
    description = "User not found"


class ProductNotFound(BaseExceptionError):
    description = "Product not found"


class InvalidDateRangeError(BaseExceptionError):
    description = "Invalid date range"
