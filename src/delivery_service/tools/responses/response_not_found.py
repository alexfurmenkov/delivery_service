from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND


class ResponseNotFound(Response):
    """
    This class is a wrapper over the original response class.
    """

    def __init__(self, message: str):
        super(ResponseNotFound, self).__init__(
            status=HTTP_404_NOT_FOUND,
            data={
                'status': 'error',
                'message': message
            }
        )
