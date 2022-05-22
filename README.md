# software_engineer
software engineer project

techs:python qt

#Back-end
## 生成数据库
首先要打开自己的mysql，然后在Back1/myback1/myback1/settings.py进行如下修改
```shell
DATABASES = {
    #不使用默认的数据库，使用mysql数据库
    #'default': {
    #   'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'db_software',
        'USER': 'root',
        'PASSWORD': '写为自己的密码',
    }
}
```
然后使用如下命令，创建数据库
```shell
python manage.py makemigrations
python manage.py migrate
```

在Back1/myback1/myapp/views.py中，每一个路径即为一个调用，可以调用后端函数（尚未完善）：
```html
<a href="/system/borrowreturn/" type="button" class="btn btn-primary " style="float:right;"><i
                            class="fa fa-plus" aria-hidden="true" style="margin-right: 6px;"></i>还书</a>
```
href的值即为此按钮触发时调用的函数

templates文件夹中用于存放html文件

static中存放网页中引用的图像，音视频，CSS，JavaScript等，我将一些常用的工具放在里面，当然也可以自己编写








