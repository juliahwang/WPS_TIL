###### 20170529 [Django Girls Tutorial]


## 0. 들어가기전에...

#### 장고? 

파이썬으로 만들어진 무료 오픈소스 웹 어플리케이션 프레임워크.

쉽고 빠르게 웹사이트를 개발할 수 있도록 돕는 구성요소로 이루어진 웹 프레임워크

웹사이트를 개발할 때 항상 만들어야하는 요소들 (ex_ 회원가입, 로그인, 로그아웃 등의 사용자인증/ 관리자 패널, 폼, 파일업로드 등의 기능)
을 바로 사용할 수 있게 만든 프레임워크.

#### 누군가 서버에 웹사이트를 요청하면...

- 요청은 장고로 전달된다.
- 장고의 urlresolver는 웹페이지 주소를 가져오고 url.py와 대조하여 식별한다.
- 매치하는 url 패턴이 있으면 요청을 view.py에 넘겨준다.
- view함수는 요청 권한을 확인하여 response를 생성한다.
- 만들어진 response는 장고에게 전달되어 사용자의 웹브라우저에 보내진다.

<br>

## 1. 가상환경 생성

### pyenv-virtualenv를 사용한 가상환경 관리

- virtualenv는 프로젝트 기초 전부를 python/django와 분리해준다.
- 따라서 웹사이트에 변경사항이 있어도 개발 중인 것에는 영향을 미치지 않는다.


#### 컴퓨터 전체에서 사용할  파이썬 환경 설정

~~~
pyenv global <version or env_name>
~~~

#### 가상환경 생성

~~~
pyenv virtualenv <version> <env_name>
~~~

#### 가상환경을 해당 폴더에서 사용하도록 지정

~~~
pyenv local <env name>
~~~

#### 가상환경이 적용되어있는지 확인

~~~
pyenv version
~~~

<br>

#### 콘솔창에서 접두어로 가상환경 이름이 안보인다면? 

>모든 작업은 가상환경(virtualenv) 안에서 해야 하는 것을 꼭 기억하세요. 현재 콘솔 창에서 접두어로 (myvenv)가 안 보인다면 먼저 virtualenv를 활성화해야 합니다. Django 설치하기 장에서 virtualenv 작동법에 대해 배웠어요. 윈도우에서는 myvenv\Scripts\activate를 타이핑하고, 맥 OS과 리눅스에서는 source myvenv/bin/activate을 입력하세요.

<br>

## 2. Django 실행

- 터미널에서 장고를 실행하기 위해 아래의 명령어로 파일을 다운받아준다.

~~~
# 터미널
django-admin startproject mysite

# tree .
.
└── mysite
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
~~~

<br>

#### (1) 폴더명 변경하기

- mysite라는 폴더가 2개 생기므로 구분하기 어렵다. 
- 따라서 겉의 mysite폴더명을 `django_app`으로 바꿔준다.

~~~
mv mysite django_app
~~~

<br>

#### (2) .gitignore 파일 생성 

~~~
https://www.gitignore.io/
~~~

- git에 연결하기 전, 특정 확장자 파일을 푸시하지 않도록 .gitignore파일을 생성하여준다.
- pycharm, macOS, Django를 선택한 후 나오는 텍스트를 복사하여 .gitingore파일에 붙인다.
- 더 추가할 확장자는 custom에 붙여넣는다.

~~~
.idea/
.*.swp
~~~

<br>

## 3. 깃헙 연결

- 깃헙에서 레포를 하나 생성하여 ssh 주소를 연결한다.

~~~ 
git@github.com:juliahwang/DjangoGirls-Homework.git
~~~

- 첫 커밋 `.gitignore` 파일과 `README.md`를 추가하였다.

<br>

>##### 주의사항.
>깃헙에서 README.md 파일을 추가할 경우 로컬 저장소에는 README.md파일이 없어 다음번 커밋부터는 push되지 않는다. 
>이 경우에는 README.md 파일을 추가하고 나서  터미널에서 `git pull origin master` 명령어를 통하여 최신 상태로 브랜치를 합쳐준다.

<br>

## 4. 블로그 생성

장고걸스 튜토리얼에서는 프로젝트에서 바로 코드 폴더로 사용하지만 wps에서는 프로젝트 폴더 안에 코드 폴더를 따로 만들어준다.
 
- `./manage.py` : 현재위치에서 manage.py를 실행하라는 명령어


### 어플리케이션 만들기

(1) 블로그 생성

`./manage.py startapp blog`

(2) djangogirls 폴더에서  파이참을 열고 가상환경이 적용되었는지 확인한다.

`cat .python-version`

(3) django_app을 root폴더로 지정해준다.

(4) 튜토리얼에 제시된 것과 같이 django에 애플리케이션 사용을 알려줘야하므로 `settings.py`에 설정을 추가한다.
추가 하지 않을 경우 장고 내의 데이터베이스 및 애플리케이션으로 동작하지 않는다.

(5) 현상태 커밋

<br>

### 블로그 글 모델 만들기

- 모든 Models 객체는 blog/models.py에 선언하여 만든다. 
- 앞으로 만들 블로그 글 모델도 이 파일 안에 클래스로 정의한다.

**(1) pycharm 버전 정해주고 확인**

- 생성하기 전에 pycharm 예전 버전을 쓰는 경우 버전을 수동으로 선택해주어야한다.
- `project:djangogirls`에서 `project interpreter`를 아래의 경로로 지정해준다.

~~~
/usr/local/var/pyenv/versions/djangogirls_homework/bin/python
~~~

<br>

**(2) 블로그 글 모델 생성**

~~~python
# blog/models.py

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
~~~

<br>

### 데이터베이스에 모델을 위한 테이블 만들기 

**(1) SQLite 데이터베이스 프로그램 설치** 

http://sqlitebrowser.org/

~~~
# mysite/settings.py안에 이미 설정되어 있다.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
~~~

<br>

**(2) 변경사항 migrate하기**

`./manage.py migrate`

- 변경사항을 데이터베이스에 반영한다는 명령어
- 위 명령어를 실행하면 `db.sqlite3` 파일이 생성된다.

~~~
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK

~~~

<br>

**(3) 변경사항 반영하기**

`./manage.py makemigrations`
- 처음 기본 파일과 비교하여 사용자가 기록한 변경사항을 반영하는 명령어

~~~
# Terminal
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
~~~

<br>

`./manage.py migrate`

- 위의 변경사항을 다시 데이터베이스에 적용시키기 위하여 다시 명령어를 실행한다.

~~~
# Terminal
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
~~~

Database에서 해당 파일을 다시 불러오면 변경사항이 적용된 것을 볼 수 있다. 

**데이터베이스 내에 'blog_post' 가 생겼다!**

<br>

**(4) migrations.py 가 필요한 이유?**

- 함께 작업할 경우 중간과정이 필요
- 커밋 시점의 데이터베이스를 확인하는 데에 중요하게 사용되므로 (커밋 이후의 코드와 이전의 코드상태)

<br>

#### 명령어 알고가기

`./manage.py` = `python manage.py`


<br>

## 5. 장고 관리자 

**(1) admin.py에 명령어 Post 클래스 등록**

- 관리자 화면을 볼 수 있게 blog/admin.py에 내용추가하기 

~~~python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
~~~

<br>

**(2) 서버 실행하기**

`./manage.py runserver`

- 서버를 실행하여 웹페이지에서 로컬로 볼 수 있는 명령어

~~~
http://127.0.0.1:8000/admin/`
~~~

<br>

**(3) 슈퍼사용자 생성하기**

`./manage.py createsuperuser
`

- admin 아이디와 패스워드를 생성할 수 있는 명령어.

<br>

### 장고 url

#### url? 

- 웹 주소
- 인터넷의 모든 페이지는 고유한 url을 가지고 있어야한다. 
- url configuration = url resolver

~~~python
# mysite/urls.py

from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list),   # 127.0.0.1:8000 url에만 적용된다.
]
~~~

- 서버를 실행하면 아직 view가 없으므로 `no attribute 'post_list'` 에러가 난다

<br>

### 장고 view

- view = controler
- 장고에서 뷰는 컨트롤러, 컨트롤러는 템플릿을 실행시킨다
- `HttpResponse()` 함수는 직접 입력한 값을 출력해준다.

~~~python
# blog/views.py

def post_list(request):
    return HttpResponse('<html><body>Post List</body></html>')
~~~

<br>

## 6. HTML 시작하기

- blog내에 따로 만들지 않고, `django_app`폴더 내에 templates폴더를 만들어준다.

- BASE_DIR 를 출력해보면 

~~~
BASE_DIR:  /Users/hwangseonjeong/projects/django/djangogirls/django_app
~~~


**(1) TEMPLATE_DIR 만들어주기**

~~~python
# mysite/settings.py

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# 파일 내 TEMPLATES 에도 추가.
TEMPLATES = [
...
'DIRS' : [TEMPLATES_DIR],
...
]
~~~

<br>

**(2) templates/blog/ 내에 post_list.html 생성**

~~~
<!doctype html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>My DjangoGirls Blog</title>
    </head>
    <body>
        <div>
            <h1><a href="#">Django Girls Blog</a></h1>
        </div>

        <div>
            <p>published: 29.05.2017 09:35</p>
            <h2><a href="">My First Post</a></h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Distinctio fuga ipsam magni nobis officiis, porro praesentium quaerat quas quod? Accusamus.</p>
        </div>
        <div>
            <p>published: 28.05.2017, 09:36</p>
            <h2><a href="">My second post</a></h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facere necessitatibus sint voluptatem! Autem, deleniti dolor, dolore dolorem dolorum eius eos facilis itaque numquam pariatur quae quas quis sunt tempore ut.</p>
        </div>
    </body>
</html>
~~~

<br>
<br>

## 7. 장고 ORM 과 쿼리셋

#### ORM

 객체지향 프로그래밍 언어에서 데이터를 바로 관계형 데이터베이스로 추가할 수 있는 툴.

개발에서 데이터베이스 맵핑이 추가하는 비중을 줄이기 위한 목적. 

![orm-img](http://www.entityframeworktutorial.net/Images/ORM.png)

<br>

#### 장고 인터렉티브 콘솔 실행

`./manage.py shell`

서버에 올려놓은 글목록을 모두 불러온다.
`from blog.models import Post`
`Post.objects.all()`

<br>

#### 쿼리셋 = 전달받은 모델의 객체 목록

~~~
<QuerySet [<Post: 블로그 안내>, <Post: 블로그 운영>, <Post: 주의사항>, <Post: 희망을
~~~

#### 쿼리셋 - 객체생성 

`Post.objects.create(title="title", text='text')`

실행시 에러나는 이유는 User모델이 없고 models.py에서 auth의 권한에 옵션이 주어지지 않았기(Null) 때문. 
 
따라서 User모델을 불러와준다.

~~~
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(id=1)
>>> user
<User: admin_h>
~~~

다시 create문을 작성하면...
잘 생성된다.

~~~
>>> Post.objects.create(title='Test title', text='test txt', author=user)
<Post: Test title>
~~~

<br>

#### 쿼리셋 : 제목 filter하기

~~~
# 명령어
>>> Post.objects.filter(title__contains='희망')
<QuerySet [<Post: 희망을 가져라>]>
>>> p1 = Post.objects.filter(title__contains='희망')
>>> print(p1.query


# SQL문
SELECT "blog_post"."id", "blog_post"."author_id", "blog_post"."title", "blog_post"."text", "blog_post"."created_date", "blog_post"."published_date" FROM "blog_post" WHERE "blog_post"."title" LIKE %희망% ESCAPE '\'
~~~

<br>

#### 쿼리셋 : 발행시간 filter하기

- published date를 지정하지 않은 것은 나오지 않는다.
- 모든 글을 보이게 하고 싶다면 filter()를 지우고 다시 `.all()`을 붙여준다.

~~~
>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: 블로그 안내>, <Post: 블로그 운영>]>
~~~

<br>

#### 정렬하기 

- 객체 목록을 정렬한다.

~~~python
# 오름차순 정렬
Post.objects.order_by('created_date')

# 내림차순 정렬
Post.objects.order_by('-created_date')
~~~

<br>

#### 조건에 맞는 열 하나를 가져오기  `.get()`

~~~
>>> post = Post.objects.get(title='Test title')
>>> post
<Post: Test title>
>>> post.publish(). # Post클래스의 publish 함수를 준다.
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: 블로그 안내>, <Post: 블로그 운영>, <Post: Test title>]>

# SQL문
SELECT "blog_post"."id", "blog_post"."author_id", "blog_post"."title", "blog_post"."text", "blog_post"."created_date", "blog_post"."published_date" FROM "blog_post" WHERE "blog_post"."published_date" <= 2017-05-29 07:00:15.970706

~~~

<br>
#### 쿼리셋 연결하여 한번에 작성

~~~python
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
~~~

<br>
<br>

## 8. 지금까지의 과정을 설명하면...

- request가 들어오면 콘트롤러는url.py(`urlresolver`)에서 response와 연결될 url을 매치한다.
- views.py(`controller`)는 models 클래스에서 만든 클래스 속성과 메소드를 가져다가 template(`view`)을 render한다.
- request가 요청한 url로 render한 view를 response로 보내준다.


#### ajax 

- 페이지의 모든 구성요소를 다시 reload하는 것이 아니라 변화가 필요한 부분만 다시 로드하는 경우 ajax형태로 제작한다.
- ex_ 목록 더 불러들이기