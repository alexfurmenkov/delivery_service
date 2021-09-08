from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class ResponseCreated(Response):
    """
    This class is a wrapper over the original response class.
    """

    def __init__(self, message: str, created_resource_id: str):
        super(ResponseCreated, self).__init__(
            status=HTTP_201_CREATED,
            data={
                'status': 'success',
                'message': message,
                'id': created_resource_id,
            }
        )
