import os

# 应用路径
base_dir = os.path.abspath(os.path.dirname(__file__))

# 配置类
class Config:
    # 开发模式
    #DEBUG = True

    # 解决中文乱码
    JSON_AS_ASCII = False

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 文件上传
    UPLOAD_FOLDER = '/var/www/html/static/blog/images'
    #UPLOAD_FOLDER = os.path.join(base_dir, 'files')
    ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif' }
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024

    # 服务端密钥
    SECRET_KEY = '715290'
