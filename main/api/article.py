import json
import time

from flask import request
from sqlalchemy.sql import func

from main import auth, db
from main.api import api
from main.models import Article, Tag
from main.utils import Response

# 查询文章列表
@api.route('/article_list/<int:page_num>/<int:page_size>')
def article_list(page_num, page_size):
    if page_num <= 0 or page_size <= 0:
        return Response.error('分页信息错误')
    articles = Article.query.order_by(Article.create_time.desc()).offset((page_num - 1) * page_size).limit(page_size)

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
    total = db.session.query(func.count(Article.id)).scalar()
    return Response.success({
        'list': data,
        'total': total
    })

# 新建文章
@api.route('/create_article', methods = ['POST'])
@auth.login_required
def create_article():
    # 获取请求参数
    try:
        data = json.loads(request.data)
    except:
        return Response.error('请求参数错误')
    
    # 数据格式校验
    title = data.get('title')
    if not title or len(title) == 0:
        return Response.error('标题格式错误')
    content = data.get('content')
    if not content or len(content) == 0:
        return Response.error('内容格式错误')
    tags_name = data.get('tags_name')
    if not tags_name or len(tags_name) == 0:
        return Response.error('标签不能为空')
    
    # 保存数据
    tags = Tag.query.filter(Tag.name.in_(tags_name))
    article = Article(title = title, content = content, tags = tags)
    try:
        db.session.add(article)
        db.session.commit()
    except:
        return Response.error('保存文章失败')
    return Response.success('保存文章成功')

# 查询文章信息
@api.route('/article_info/<int:id>')
def article_info(id):
    article = Article.query.get(id)
    if not article:
        return Response.error('文章信息不存在')
    
    # 文章阅读数加一
    article.click += 1
    try:
        db.session.add(article)
        db.session.commit()
    except:
        return Response.error('文章信息错误')
    return Response.success(article.to_dict())

# 修改文章信息
@api.route('/article_change', methods = ['POST'])
@auth.login_required
def article_change():
    # 获取请求参数
    try:
        data = json.loads(request.data)
    except:
        return Response.error('请求参数错误')
    
    # 数据格式校验
    id = data.get('id')
    if not id:
        return Response.error("文章id不能为空")
    title = data.get('title')
    if not title or len(title) == 0:
        return Response.error('标题格式错误')
    content = data.get('content')
    if not content or len(content) == 0:
        return Response.error('内容格式错误')
    tags_name = data.get('tags_name')
    if not tags_name or len(tags_name) == 0:
        return Response.error('标签不能为空')
    article = Article.query.get(id)
    if not article:
        return Response.error('文章信息不存在')

    # 保存数据
    tags = Tag.query.filter(Tag.name.in_(tags_name))
    article.title = title
    article.content = content
    article.tags = tags
    try:
        db.session.add(article)
        db.session.commit()
    except:
        return Response.error('保存文章失败')
    return Response.success('保存文章成功')

# 删除文章信息
@api.route('/article_delete/<int:id>')
@auth.login_required
def article_delete(id):
    article = Article.query.get(id)
    if not article:
        return Response.error('文章信息不存在')
    try:
        db.session.delete(article)
        db.session.commit()
    except:
        return Response.error('删除文章失败')
    return Response.success('删除文章成功')

# 文章点赞
@api.route('/article_support/<int:id>')
def article_support(id):
    article = Article.query.get(id)
    if not article:
        return Response.error('文章信息不存在')
    
    # 文章点赞数加一
    article.support += 1
    try:
        db.session.add(article)
        db.session.commit()
    except:
        return Response.error('文章信息错误')
    return Response.success('点赞成功')
