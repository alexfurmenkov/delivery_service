"""
Not found response with 404 HTTP status is returned when a requested resource
cannot be found based on the given parameters.
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND


class ResponseNotFound(Response):
    """
    The class defines concrete HTTP status and body.
    """

    def __init__(self, message: str):
        super().__init__(
            status=HTTP_404_NOT_FOUND,
            data={
                'status': 'error',
                'message': message
            }
        )
