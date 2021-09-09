"""
Bad request response means that there was a conflict.
For example, an attempt to create an existing resource.
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class ResponseBadRequest(Response):
    """
    The class defines concrete HTTP status and body.
    """

    def __init__(self, message: str):
        super().__init__(
            status=HTTP_400_BAD_REQUEST,
            data={
                'status': 'error',
                'message': message
            }
        )
