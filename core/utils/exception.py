from rest_framework.exceptions import APIException


class QueryInvalid(APIException):
    status_code = 400
    default_detail = 'Invalid Query!'
    default_code = 'invalid_query'
