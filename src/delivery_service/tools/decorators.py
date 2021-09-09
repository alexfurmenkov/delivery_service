"""
This module contains decorators used in the meetups_backend project.
"""
import functools

from rest_framework.request import Request

from delivery_service.tools.responses import ResponseValidationError, ResponseNotFound


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


def ensure_existing_record(db_model_class):
    """
    The decorator is used in endpoints to check if
    a record with requested id exists in the DB.
    If the record is not found -> returns 404 response.
    The use of this decorator allows to avoid
    code duplication in endpoints handlers.
    """
    def ensure_existing_record_inner(handler):

        @functools.wraps(handler)
        def _wrapper(view, request: Request, pk: str, *args, **kwargs):
            if not db_model_class.objects.filter(id=pk).exists():
                return ResponseNotFound(message=f'Resource with id {pk} is not found.')
            return handler(view, request, pk, *args, **kwargs)

        return _wrapper

    return ensure_existing_record_inner
