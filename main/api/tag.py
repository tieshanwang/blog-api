import json
import time

from flask import request
from sqlalchemy.sql import func

from main import auth, db
from main.api import api
from main.models import Tag, Article
from main.utils import Response

# 查询标签列表
@api.route('/tag_list')
def tag_list():
    tags = Tag.query.order_by(Tag.name).all()

    # 组装数据
    data = []
    for tag in tags:
        data.append({
            'id': tag.id,
            'name': tag.name,
            'article_num': tag.articles.count()
        })
    return Response.success(data)

# 新建标签
@api.route('/create_tag', methods = ['POST'])
@auth.login_required
def create_tag():
    # 获取请求参数
    try:
        data = json.loads(request.data)
    except:
        return Response.error('请求参数错误')
    
    # 数据格式校验
    name = data.get('name')
    if not name or len(name) == 0:
        return Response.error('标签格式错误')
    tags = Tag.query.all()
    for tag in tags:
        if tag.name == name:
            return Response.error('标签已存在')
    
    # 保存数据
    t = Tag(name = name)
    try:
        db.session.add(t)
        db.session.commit()
    except:
        return Response.error('新建标签失败')
    return Response.success('新建标签成功')

# 删除标签
@api.route('/tag_delete/<int:id>')
@auth.login_required
def tag_delete(id):
    tag = Tag.query.get(id)
    if not tag:
        return Response.error('标签信息不存在')
    
    # 执行删除
    try:
        db.session.delete(tag)
        db.session.commit()
    except:
        return Response.error('删除标签失败')
    return Response.success('删除标签成功')

# 按标签查询文章
@api.route('/tag_of_article/<int:id>/<int:page_num>/<int:page_size>')
def tag_of_article(id, page_num, page_size):
    if page_num <= 0 or page_size <= 0:
        return Response.error('分页信息错误')
    
    tag = Tag.query.get(id)
    if not tag:
        return Response.error('标签信息不存在')
    articles = tag.articles.order_by(Article.create_time.desc()).offset((page_num - 1) * page_size).limit(page_size).all()

    # 组装数据
    data = []
    for article in articles:
        data.append({
            'id': article.id,
            'title': article.title,
            'click': article.click,
            'support': article.support,
            'update_time': int(time.mktime(article.update_time.timetuple())) * 1000
        })
    total = tag.articles.count()
    return Response.success({
        'list': data,
        'total': total
    })
