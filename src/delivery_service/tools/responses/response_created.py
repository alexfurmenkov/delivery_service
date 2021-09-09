"""
Created response with 201 HTTP status is returned
when a new resource has been created.
"""
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class ResponseCreated(Response):
    """
    The class defines concrete HTTP status and body.
    """

    def __init__(self, message: str, created_resource_id: str):
        super().__init__(
            status=HTTP_201_CREATED,
            data={
                'status': 'success',
                'message': message,
                'id': created_resource_id,
            }
        )
