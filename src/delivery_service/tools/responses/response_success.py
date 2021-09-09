from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ResponseSuccess(Response):
    """
    This class is a wrapper over the original response class.
    """

    def __init__(self, message: str, response_data: dict = None):
        if response_data is None:
            response_data: dict = {}

        super(ResponseSuccess, self).__init__(
            status=HTTP_200_OK,
            data={
                'status': 'success',
                'message': message,
                **response_data,
            }
        )
