from flask import Blueprint

# 定义蓝本
api = Blueprint('api', __name__)

from main.api import upload
from main.api import admin
from main.api import article
from main.api import tag
from main.api import error
