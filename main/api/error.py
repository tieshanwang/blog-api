from main.api import api
from main.utils import Response

@api.app_errorhandler(404)
def not_found(e):
    return Response.error('请求地址错误')

@api.app_errorhandler(405)
def method_error(e):
    return Response.error('请求方法错误')
