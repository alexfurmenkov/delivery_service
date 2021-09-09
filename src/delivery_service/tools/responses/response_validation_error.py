"""
Validation error response with 400 HTTP status is
returned when request body is invalid.
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class ResponseValidationError(Response):
    """
    The class defines concrete HTTP status and body.
    """

    def __init__(self, message: str, invalid_keys: list):
        super().__init__(
            status=HTTP_400_BAD_REQUEST,
            data={
                'status': 'error',
                'message': message,
                'invalid_keys': invalid_keys
            }
        )
