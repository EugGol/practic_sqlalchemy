class BaseException(Exception):
    description = None


class ObjectNotFound(BaseException):
    description = "Object not found"


class UserNotFound(BaseException):
    description = "User not found"


class ProductNotFound(BaseException):
    description = "Product not found"
