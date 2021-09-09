"""
Successful response with 200 HTTP status is returned when an operation
has finished its execution without any errors.
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ResponseSuccess(Response):
    """
    The class defines concrete HTTP status and body.
    """

    def __init__(self, message: str, response_data: dict = None):
        if response_data is None:
            response_data: dict = {}

        super().__init__(
            status=HTTP_200_OK,
            data={
                'status': 'success',
                'message': message,
                **response_data,
            }
        )
