import json

from flask import request

from main import auth, db
from main.api import api
from main.models import Admin
from main.utils import Response

# 管理员是否存在
@api.route('/has_admin')
def has_admin():
    admin = Admin.query.first()
    if not admin:
        # 创建管理员
        admin = Admin(password = '123123')
        try:
            db.session.add(admin)
            db.session.commit()
        except:
            return Response.error('创建管理员失败')
        
        # 获取令牌
        token = admin.generate_auth_token()
        return Response.success(token)
    return Response.success(True)

# 设置密码
@api.route('/set_password', methods = ['POST'])
@auth.login_required
def set_password():
    # 获取请求参数
    try:
        data = json.loads(request.data)
    except:
        return Response.error('请求参数错误')
    
    # 数据格式校验
    password = data.get('password')
    if not password or len(password) < 6:
        return Response.error('密码格式错误')
    
    # 修改密码
    admin = Admin.query.first()
    if not admin:
        return Response.error('管理员不存在')
    admin.password = password
    
    # 保存数据
    try:
        db.session.add(admin)
        db.session.commit()
    except:
        return Response.error('设置密码失败')
    return Response.success('设置密码成功')

# 管理员登录
@api.route('/admin_login', methods = ['POST'])
def admin_login():
    # 获取请求参数
    try:
        data = json.loads(request.data)
    except:
        return Response.error('请求参数错误')
    
    # 数据格式校验
    password = data.get('password')
    if not password or len(password) < 6:
        return Response.error('密码格式错误')
    
    # 验证密码
    admin = Admin.query.first()
    if not admin:
        return Response.error('管理员不存在')
    if not admin.verify_password(password):
        return Response.error('密码错误')
    
    # 获取令牌
    token = admin.generate_auth_token(3600)
    return Response.success(token)
