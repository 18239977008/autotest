#安装环境
##安装django
```bash
$ pip install django
```

##搭建mysql环境
```bash
$ https://downloads.mysql.com/archives/installer/
```
创建数据库
修改autotest文件下的settings.py文件下
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autotest',  #数据库昵称
        'USER':'root',     #账号
        'PASSWORD':'root',   #密码
        'HOST':'127.0.0.1',  # ip
        'PORT':'3306',   # 端口
    }
}

