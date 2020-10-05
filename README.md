# My Blog Project

## Setup

1. Virtual environment

   ```bash
   python3 -m venv venv
   ```

2. PATH

   ```bash
   $env:FLASK_APP = 'blog.py'
   ```

3. Database initialization

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Application interface

### File upload

```bash
POST /api/upload
```

Parameter

```json
form-data key:files
```

Response

```json
{
    "code": 0,
    "msg": "ok",
    "data": "文件上传成功"
}
```

### Administrator exists

```bash
GET /api/has_admin
```

Parameter

```json
None
```

Response

```json
{
    "code": 0,
    "data": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMTY0MzM1NSwiZXhwIjoxNjAxNjQzOTU1fQ.eyJpZCI6MX0.MBc5Ms7LKlOjEQIPzPpIRDspJhNZ1sAmtJDEgogu0s-ywtJmeIe9DpV4kZ5_rCvqccCCjw0zSWGdMU5rFF4oXw",
    "msg": "ok"
}
```

### Setting password

```bash
POST /api/set_password
```

Parameter

```json
{
    "password": "111111"
}
```

Response

```json
{
    "code": 0,
    "data": "设置密码成功",
    "msg": "ok"
}
```

### Administrator  login

```bash
POST /api/admin_login
```

Parameter

```json
{
    "password": "111111"
}
```

Response

```json
{
    "code": 0,
    "data": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMTY0MzY4MSwiZXhwIjoxNjAxNjQ3MjgxfQ.eyJpZCI6MX0.zb1zGMTKvlw488XO7djglorYjQKleJU1TAXZIGg7g_MB-LlQG27ct8nutXXVPmTrMovDGYgYCzp8BPPU2V9BFA",
    "msg": "ok"
}
```

### Article list

```bash
GET /api/article_list/{page_num}/{page_size}
```

Parameter

```json
None
```

Response

```json
{
    "code": 0,
    "data": [],
    "msg": "ok"
}
```

### Create article

```bash
POST /api/create_article
```

Parameter

```json
{
    "title": "测试标题",
    "content": "测试内容",
    "tags_name": [
        "数据结构"
    ]
}
```

Response

```json
{
    "code": 0,
    "data": "保存文章成功",
    "msg": "ok"
}
```

### Article information

```bash
GET /api/article_info/{id}
```

Parameter

```json
None
```

Response

```json
{
    "code": 0,
    "data": {
        "click": 1,
        "content": "测试内容",
        "create_time": 1601615307000,
        "id": 1,
        "support": 0,
        "tags": [
            {
                "id": 1,
                "name": "数据结构"
            }
        ],
        "title": "测试标题",
        "update_time": 1601615504000
    },
    "msg": "ok"
}
```

### Change article

```bash
POST /api/article_change
```

Parameter

```json
{
    "id": 1,
    "title": "修改标题",
    "content": "修改内容",
    "tags_name": [
        "数据结构"
    ]
}
```

Response

```json
{
    "code": 0,
    "data": "保存文章成功",
    "msg": "ok"
}
```

### Delete article

```bash
GET /api/article_delete/{id}
```

Parameter

```json
None
```

Response

```json
{
    "code": 0,
    "data": "删除文章成功",
    "msg": "ok"
}
```

### Support article

```bash
GET /api/article_support/{id}
```

Parameter

```json
None
```

Response

```json
{
    "code": 0,
    "data": "点赞成功",
    "msg": "ok"
}
```

### Tag list

```bash
GET /api/tag_list
```

Parameter

```json
None
```

Response

```json
{
    "code": 0,
    "data": [
        {
            "id": 1,
            "name": "数据结构"
        }
    ],
    "msg": "ok"
}
```

### Create Tag

```bash
POST /api/create_tag
```

Parameter

```json
{
    "name": "数据结构"
}
```

Response

```json
{
    "code": 0,
    "data": "新建标签成功",
    "msg": "ok"
}
```

### Delete Tag

```bash
GET /api/tag_delete/{id}
```

Parameter

```json
None
```

Response

```json
{
    "code": 0,
    "data": "删除标签成功",
    "msg": "ok"
}
```

### Search article by tag

```bash
GET /api/tag_of_article/{id}/{page_num}/{page_size}
```

Parameter

```json
None
```

Response

```json
{
    "code": 0,
    "data": [
        {
            "click": 1,
            "id": 1,
            "support": 0,
            "title": "测试标题",
            "update_time": 1601615504000
        }
    ],
    "msg": "ok"
}
```

