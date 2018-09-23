# coding=utf-8
from rest_framework.exceptions import APIException
from rest_framework import status


class KSException(APIException):
    default_detail = u"您的请求无法接受"
    status_code = status.HTTP_406_NOT_ACCEPTABLE  # busniss Not Acceptable
