from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash

from main import auth, db

# 管理员认证
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True)
    password_hash = db.Column(db.String(128), nullable = False)

    # 只写密码
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # 设置密码
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # 校验密码
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # 生成令牌
    def generate_auth_token(self, expiration = 600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': self.id }).decode('utf-8')
    
    # 校验令牌
    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return Admin.query.get(data['id'])
