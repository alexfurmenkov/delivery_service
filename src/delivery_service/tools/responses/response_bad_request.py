from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class ResponseBadRequest(Response):
    """
    This class is a wrapper over the original response class.
    """

    def __init__(self, message: str):
        super(ResponseBadRequest, self).__init__(
            status=HTTP_400_BAD_REQUEST,
            data={
                'status': 'error',
                'message': message
            }
        )
