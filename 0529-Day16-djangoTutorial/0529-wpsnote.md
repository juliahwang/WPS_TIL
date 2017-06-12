###### 20170529 [Django]

# wpsnote

##DjangoGirls Tutorial

- 장고 내의 클래스는 입력한 데이터를 저장하고 프로그램을 종료해도 다시 꺼내 쓸 수 있는 '저장' 기능을 제공한다.

- 데이터베이스 : 체계화된 데이터의 모임
- 'sqlite 데이터베이스는 기본 장고 데이터베이스 어댑터입니다.'
- sqlite는 데이터베이스가 하나의 파일로 구성되어 있다.
- 애플리케이션 = 기능

	ex_ 회원가입 => 멤버 어플리케이션

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

(1) 블로그 글 모델 생성

- 생성하기 전에 pycharm 예전 버전을 쓰는 경우 버전을 수동으로 선택해주어야한다.
- project:djangogirls에서 `project interpreter`를 아래의 경로로 지정해준다.

`/usr/local/var/pyenv/versions/djangogirls_env/bin/python`


<br>

### 데이터베이스에 모델을 위한 테이블 만들기 

(1) SQLite 데이터베이스 프로그램 설치 

http://sqlitebrowser.org/


(2) 변경사항 반영 

`./manage.py migrate`

- 변경사항을 데이터베이스에 반영한다는 명령어

~~~
# Terminal
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
~~~

`./manage.py makemigrations`
- 처음 기본 파일과 비교하여 사용자가 기록한 변경사항을 반영하는 명령어

~~~
# Terminal
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
~~~

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

>'blog_post' 가 생겼다!

(3) migrations.py 가 필요한 이유?

- 함께 작업할 경우 중간과정이 필요
- 커밋 시점의 데이터베이스를 확인하는 데에 중요하게 사용되므로 (커밋 이후의 코드와 이전의 코드상태)

#### 명령어

`./manage.py` = `python manage.py`

<br>

### 장고 관리자 페이지 만들기 

(1) admin.py에 명령어 Post 클래스 등록

- 관리자 화면을 볼 수 있게 blog/admin.py에 내용추가하기 

~~~python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
~~~

(2) 서버 실행하기 

`./manage.py runserver`

- 서버를 실행하여 웹페이지에서 로컬로 볼 수 있는 명령어
- `http://127.0.0.1:8000/admin/`

(3) 슈퍼사용자 생성하기

`./manage.py createsuperuser
`

- admin 아이디와 패스워드를 생성할 수 있는 명령어.

<br>

### 장고 url

url? 

url configuration = url resolver

`url(r'^$', views.post_list), `

<br>

### 장고 view

- view != controler
- 장고에서 뷰는 컨트롤러, 컨트롤러는 템플릿을 실행시킨다

<br>

### HTML 시작하기

- blog내에 따로 만들지 않고, `django_app`폴더 내에 templates폴더를 만들어준다.

- BASE_DIR 를 출력해보면 

~~~
BASE_DIR:  /Users/hwangseonjeong/projects/django/djangogirls/django_app
~~~


#### TEMPLATE_DIR 만들어주기


### 장고 ORM 과 쿼리셋

ORM : 객체지향 프로그래밍 언어에서 데이터를 바로 관계형 데이터베이스로 추가할 수 있는 툴.
개발에서 데이터베이스 맵핑이 추가하는 비중을 줄이기 위한 목적. 

![orm-img](http://www.entityframeworktutorial.net/Images/ORM.png)

장고 인터렉티브 콘솔 실행
`./manage.py shell`

서버에 올려놓은 글목록을 모두 불러온다.
`from blog.models import Post`
`Post.objects.all()`

= 쿼리셋(전달받은 모델의 객체 목록)

~~~
<QuerySet [<Post: 블로그 안내>, <Post: 블로그 운영>, <Post: 주의사항>, <Post: 희망을
~~~

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

제목 filter하기

~~~
# 명령어
>>> Post.objects.filter(title__contains='희망')
<QuerySet [<Post: 희망을 가져라>]>
>>> p1 = Post.objects.filter(title__contains='희망')
>>> print(p1.query


# SQL문
SELECT "blog_post"."id", "blog_post"."author_id", "blog_post"."title", "blog_post"."text", "blog_post"."created_date", "blog_post"."published_date" FROM "blog_post" WHERE "blog_post"."title" LIKE %희망% ESCAPE '\'
~~~

발행시간 filter하기

- published date를 지정하지 않응 것은 나오지 않는다.

~~~
>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: 블로그 안내>, <Post: 블로그 운영>]>
~~~

조건에 맞는 열 하나를 가져오기  `.get()`

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

### 템플릿 동적데이터

-날리기

### 과정

- request가 들어오면 url.py(`urlresolver`)로 이동하여 연결될 url을 선택하고 views.py(`controler`)는 models 클래스에서 만든 클래스 속성과 메소드를 가져다가template(`view`)을 render하여 request가 들어온 url로 다시 response를 보내준다.


#### ajax 

- 페이지의 모든 구성요소를 다시 reload하는 것이 아니라 변화가 필요한 부분만 다시 로드하는 경우 ajax형태로 제작한다.
- ex_ 목록 더 불러들이기






