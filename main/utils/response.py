from flask import jsonify

# 响应类
class Response:
    # 成功
    @staticmethod
    def success(data = None):
        return jsonify({
            'code': 0,
            'msg': 'ok',
            'data': data
        })
    
    # 失败
    @staticmethod
    def error(msg = None):
        return jsonify({
            'code': 1,
            'msg': msg,
            'data': None
        })
