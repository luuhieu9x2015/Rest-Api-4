from rest_framework import status
from rest_framework.exceptions import APIException, _get_error_details
from django.utils.translation import gettext as _

from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    print('error handele')
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

class ValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Bad Request')
    default_code = 'ERR_BAD_REQUEST'

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        self.detail = _get_error_details(detail, code)
        self.code = 400

