"""
This module contains decorators used in the meetups_backend project.
"""
import functools

from rest_framework.request import Request

from delivery_service.tools.responses import ResponseValidationError


def request_validation(serializer):
    """
    Validates request according to the given serializer.
    Passes the request further if the serializer is valid.
    :param serializer: HTTP Request serializer
    """
    def request_validation_inner(handler):

        @functools.wraps(handler)
        def _wrapper(view, request: Request, *args, **kwargs):
            if request.method == 'GET':
                validation_serializer = serializer(data=request.query_params)
            else:
                validation_serializer = serializer(data=request.data)
            if not validation_serializer.is_valid():
                return ResponseValidationError(
                    message='Request body is invalid.',
                    invalid_keys=list(validation_serializer.errors.keys())
                )
            return handler(view, request, *args, **kwargs)

        return _wrapper

    return request_validation_inner
