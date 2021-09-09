from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class ResponseValidationError(Response):
    """
    This class is a wrapper over the original response class.
    """

    def __init__(self, message: str, invalid_keys: list):
        super(ResponseValidationError, self).__init__(
            status=HTTP_400_BAD_REQUEST,
            data={
                'status': 'error',
                'message': message,
                'invalid_keys': invalid_keys
            }
        )
