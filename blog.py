from flask_cors import CORS
from flask_migrate import Migrate

from main import create_app, db

# 创建实例
app = create_app()
CORS(app, supports_credentials = True, max_age = 600)

# 数据库迁移
migrate = Migrate(app, db)

# 运行
if __name__ == '__main__':
    app.run(host = '0.0.0.0')
