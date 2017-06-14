###### 20170614 [Django Documentation - instagrom]

## Instagram 만들기 실습

### (1) 가상환경 생성

쉘에서 가상환경을 python 3.6.0으로 생성해주고 폴더에 적용해준다.

```python
# pyenv virtualenv <버전> <가상환경이름>
$ pyenv virtualenv 3.6.0 djangoinstahw

# 가상환경 이름으로 해당 폴더에 가상환경 설정
$ pyenv local djangoinstahw
```

### (2) .gitignore 생성, 필요 패키지 설치   

사용하는 언어와 프레임워크, OS, 툴에 따라 git에 버전관리하고 싶지 않은 확장자를 알려주는 사이트에서 텍스트를 복사해와 `.gitignore`를 만든다. [바로가기](gitignore.io)

그리고 장고프레임워크를 사용할 것이므로 필요한 관련 패키지들을 `pip`명령어로 설치해준다.

```python
# 장고 설치
$ pip install django
# 장고 익스텐션 설치
$ pip install django_extensions
# ipython 설치
$ pip install ipython

# 위의 버전을 설치해야 개발을 진행할 수 있다. 따라서 requirements.txt를 작성한다.
$ pip freeze > requirements.txt
```

그리고 가상환경을 설정해준 폴더 내에 내부폴더(django_app)을 만든 후 프로젝트폴더를 생성한다. 

```python
$ django-admin startproject config .
```

프로젝트 폴더명과 앱 폴더명은 한번 정하고 마이그레이트시킨 후에는 변경이 어렵다. 설정파일에도 모두 해당이름으로 등록되어 단순히 폴더이름만 교체하는 것이 아니라 여러 곳에서 설정을 바꿔줘야하기 때문이다. 
이 경우에는 마우스 오른쪽 클릭 - 폴더 이름바꾸기에서 `refactor`기능을 사용하면 한번에 다 바꿔준다.

<br>

### (3) 장고의 User모델 사용하기
 
장고의 사용자 인증 시스템은 사용자 계정, 그룹, 권한, 쿠키기반 사용자 세션을 기반으로 동작한다. 모델을 만들 때 로그인과 보안기능을 추가하려면 이미 장고에서 만들어놓은 User모델을 사용한다.

<br>

#### 참고 > 쿠키 기반 사용자 세션 

http연결은 불연속적이므로(요청이 있을 때만 연결) 서버에 요청이 올 때마다 연속적인 요청인지 알 수 없다. 따라서 키값을 부여하고 서버에 세션으로 저장을 해둔다. 브라우저 내부에서 세션 키값을 클라이언트 입장에서도 저장하는데 이를 쿠키라고 부른다. 이를 통해 요청이 첫 요청인지 연속적인 요청인지 구별해낸다.

<br>

#### 참고 > A pluggable backend system

인증할 때 사용하는 기능. 일반적으로 유저네임과 패스워드를 제공한다. 다른 것으로는 페이스북으로 로그인, 네이버로 로그인(OAuth라고 부른다.) 등의 시스템을 제공하기도 한다. 

<br>

[참고- User 객체 생성하기](https://docs.djangoproject.com/en/1.11/topics/auth/default/#user-objects)

사용자 모델을 정의할 때는 장고의 User모델을 불러와서 만든다.

```python
>>> from django.contrib.auth.models import User
>>> user = User.objects.create(username='julia')
```

### (4) User모델을 member앱에 정의하고 settings에 등록

`member`라는 이름의 장고 앱을 만들고 User모델을 정의한다.
 
```python
$ ./manage.py startapp member

### 폴더 내의 models.py에서 User모델 생성
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	pass
# AbstractUser는 User의 객체가 기능할 수 있는 여러 메서드를 제공하는 장고 내장클래스이다. 

### config/settings.py에서 만든 User클래스를 설정해준다.
AUTH_USER_MODEL = 'member.User'
```

<br>

### (5) post앱을 만들고 기본 모델 정의하기

User모델을 정의한 후에는 다른 이름의 앱을 만들어 사용할 주요 모델들을 정의해준다.

```python
### post/models.py
from config import settings
from django.db import models

class Post(models.Model):
	# User모델을 일대다필드로 불러올 때는 member앱에서 불러오는 것이 아니라 settings에 
	# 설정된 변수명으로 불러온다. 
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	photo = models.ImageField(upload_to = 'post', blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	like_users = models.ManyToManyField(
		settings.AUTH_USER_MODEL,
		through = 'PostLike',
		related_name='liked_post",
	)

# Post와 User의 중간자 모델
class PostLike(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.ForeignKey(Post)
	created_date = models.DateTimeField(auto_now_add=True)
	
class Comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.ForeignKey(Post)
	content = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
```
<br>

#### 참고 > 중간자 모델을 나중에 정의할 때 migrate fake 

PostLike 중간자 모델을 나중에 정의할 경우 자동생성 중간자모델의 테이블과 같은 형태로 정의하고  meta 클래스를 선언하여 db의 자동생성 테이블을 가리키게 한 다음 migration파일을 만들어준다. 그 후 migrate를 할 때 fake옵션을 주어 테이블 간 충돌이 발생하지 않도록 한 후 추가 필드를 생성하고 Meta 클래스를 비활성화하여 migrate하면 사용자정의한 PostLike 모델명을 소문자한 테이블이 새로 생성되고, 추가 필드도 생긴다.

<br>

#### Extending the existing User model

User는 장고 코드 안에 있어서 커스터마이징할 수 없다. 이 경우에는 OneToOneField를 사용하여 본래 모델을 확장하거나 AUTH_USER_MODEL을 사용하여 새로 정의하는 방법이 있다.

기본 사용자모델로 충분하더라도 사용자 지정 사용자 모델을 정의하는 것이 좋다.
member앱을 생성한 후 AbstractUser를 상속받는 User모델을 새로 정의해준다.

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

또한 `AUTH_USER_MODEL`을 `settings.py`에 다음과 같이 사용하겠다는 것을 알려준다.

```python
# config/settings.py

AUTH_USER_MODEL = 'models.User'
``` 

```python
# member/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

다시 post/models.py로 돌아와서 User모델명을 사용한 곳을 모두 `settings.AUTH_USER_MODEL`로 바꿔준다.

member앱에서 바로 User모델을 import하면 되지 않냐고 하는데 그렇게는 잘 쓰지 않고 settings에서 불러오는 방법을 사용한다. 

그 후 migrations 파일들과 db파일을 모두 삭제하고 새로 migrate, makemigrations해준다.

만약 migration파일을 삭제할 수 없는 상황이라면 OneToOneField를 사용하여 User모델을 확장 정의해주는 방법을 사용한다.

장고의 User 모델은 기본적으로 AbstractUser모델을 상속받는데, 상속받으면 해당 모델에서 거의 모든 사용자 기능을 사용할 수 있다. 해당 모델은 정해진 username을 커스터마이징하여 사용할 수 있다.

비밀번호나 마지막 로그인 기능 같은 경우에는 AbstractBaseUser를 상속받아서 사용한다. 이 모델은 로그인하는 username 필드의 양식이 딱히 정해져있지 않다.(전화번호, 이메일, 아이디 등 모두 가능)

<br>

#### macOS에서 Pillow library 생성하기

모델에 ImageField를 사용하는 경우 추가적으로 Pillow라는 라이브러리를 설치해주어야한다. 
Pillow는 파이썬의 이미징 라이브러리로 이미지 파일 핸들링을 용이하게 해준다. [레퍼런스](https://pillow.readthedocs.io/en/latest/index.html)

```python
$ brew install libtiff libjpeg webp little-cms2
$ pip install Pillow
```

<br>

#### 이미지 저장시 경로 설정

루트폴더(`django_app/`) 내에 `media/<앱이름>` 이름의 폴더를 만든다. 해당 경로는 해당 앱에서 만든 모델에 이미지를 업로드, 다운로드할 때 이미지 파일이 저장되는 경로이다. 

```python
### config/settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
MEDIA_ROOT - root폴더에 이미지가 저장된다. 
따라서 settings 에서 이미지가 media폴더에 저장될 수 있도록 패스를 설정해준다.

프로젝트의 urls모듈에서 다음과 같이 업로드될 이미지 저장경로를 설정해준다.

```python
### config/urls.py

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
```

<br>

### (6) admin 페이지 생성하고 글 등록하기

만들어진 모델을 해당 앱 폴더 내 `admin.py`에 등록해준다. 

```python
### post/admin.py

class PostAdmin(admin.ModelAdmin):
	pass

admin.site.register(Post)
```

터미널에서 admin에 접속할 수 있는 createsuperuser를 만든다. 

```python
# 사용자이름, 비밀번호를 입력할 수 있는 프롬프트가 실행된다.
$ ./manage.py createsuperuser

# 사용자이름 미리 정의
# 비밀번호 입력 프롬프트가 실행된다. 
$ ./manage.py createsuperuser --username=admin
```

admin페이지의 url은 이미 생성되어 있으므로 로컬 주소를 통해 서버를 실행시킨다. 

```python
$ ./manage.py runserver
```

생성되어 있는 Post를 눌러 글을 여러 개 등록해준다.

<br>

### (7) post앱의 urls 모듈 생성, include()를 사용하여 url 패턴 지정

```python
### post/urls.py
from django.conf.urls import url
from . import views


app_name = 'post'
urlpatterns = [
	# 아무것도 없는 url 패턴을 찾으면 views의 post_list뷰로 연결되는 post_list이름의 url 생성
	url(r'^$', views.post_list, name='post_list')
	# post의 id값이 있는 패턴을 찾으면 view의 post_detail로 연결되는 post_detail url
	url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail')
	# post를 생성할 수 있는 url패턴을 만들고 post_create 뷰로 연결되는 post_create url
	url(r'^create/$', views.post_create, name='post_create')
	# 만들어져있는 post를 수정하는 url패턴을 만들고 post_modify뷰로 연결되는 post_modify url
	url(r'^(?P<post_pk>\d+)/modify/$', views.post_modify, name='post_modify')
	# 만들어져있는 post를 삭제하는 url패턴을 만들고 post_delete 뷰로 연결되는 post_delete url
]


### config/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	
	# post앱의 urls.py 모듈에 있는 모든 url은 다음 정규식(post/)이 앞에 붙도록 정의해준다.
	url(r'^post/', include('post.urls'),
]
```

<br>

### (7) view 만들기 - `post_list(request)`

등록한 모든 포스트를 보여주기 위해서는 post_list 뷰를 생성하여 데이터베이스의 정보를 가져와야한다. 

```python
### post/views.py

def post_list(request):
	posts = Post.objects.all()
	context = {
		'posts': posts,
	}
	return render(request, 'post/post_list.html', context=context)
```

### (8) base 템플릿, post_list 템플릿 만들기

template 폴더 내에 common/base.html을 만든다. 해당 html파일에는 공통으로 들어가는 html 구조를 넣어 중복을 방지해준다. 

반드시 최상단에 `{% load static %}`을 넣어 동작하도록 해준다.

```html
<!--common/base.html-->

<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Instagram</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

post_list는 게시글 목록형태로 구성되어 있다. 따라서 for문을 돌면서 post 데이터를 가져오는 것이 좋다. 또한 이미지는 그 경로를 이미지태그에 넣어 로드시켜준다.

인스타그램은 게시일을 클릭하면 디테일뷰로 넘어가므로 게시일에 post_detail url과 해당 id값을 연결해준다.

```html
<!--post/post_list.html-->

{% block content %}
	{% for post in posts %}
		<img src="{{ post.photo.url }}" alt="">
    	<p>{{ post.author }}</p>
    	<a href="{% url 'post:post_detail' post_pk=post.pk %}">{{ post.created_date }}</a>
	{% endfor %}
{% endblock %}
```

<br>

### (9) view 만들기 - `post_detail(request)`

등록한 포스트의 생성일을 누르면 해당 포스트의 디테일 페이지로 이동하는 post_detail 뷰를 생성한다.
post_detail url은 `post_pk`로 이름지은 해당 포스트의 id값을 불러와야하기 때문에 쿼리셋에서 id값에 해당하는 데이터를 불러와 페이지를 렌더링해준다.

```python
### post/views.py
# 기본 post_detail 페이지 뷰

def post_detail(request, post_pk):
	post = Post.object.get(pk=post_pk)
	context = {
		'post': post,
	}
	return render(request, 'post/post_detail.html', context=context)


# get()메소드의 에러 처리 
def post_detail(request, post_pk):
	try:
		post = Post.objects.get(pk=post_pk)
		context = {
		'post': post,
		}
		return render(request, 'post/post_detail.html', context=context)
	except DoesNotExist as e:
		return HttpResponseNotFound('Post not found, detail : {}'.format(e))
	
		

# post_list view로 돌아가기 - (1) redirect() 사용
def post_detail(request, post_pk):
	try:
		post = Post.objects.get(pk=post_pk)
		context = {
		'post': post,
		}
		return render(request, 'post/post_detail.html', context=context)
	except DoesNotExist as e:
		return redirect('post:post_list')
	

		
# post_list view로 돌아가기 - (2) HttpResponseRedirect() 사용
def post_detail(request, post_pk):
	try:
		post = Post.objects.get(pk=post_pk)
		context = {
		'post': post,
		}
		return render(request, 'post/post_detail.html', context=context)
	except DoesNotExist as e:
		url = reverse('post:post_list')
		return HttpResponseRedirect(url)
			
	
# 찾는 id값이 없을 경우 404 페이지로 이동하는 뷰
# 템플릿을 사용할 경우 render()를 사용한다.
def post_detail(request, post_pk):
	post = get_object_or_404(Post, pk=post_pk)
	context = {
		'post': post,
	}
	return render(request, 'post/post_detail.html', context=context)
	
	
# render()를 사용하지 않고 템플릿을 불러올 경우 
def post_detail(request, post_pk):
	try: 
		post = Post.objects.get(pk=post_pk)
		# 장고가 템플릿 디렉토리를 순회하며 일치하는 템플릿을 확인한 후 template에 리턴
		template = loader.get_template('post/post_detail.html')
		context = {
			'post': post,
		}
		rendered_string = template.render(request, context)
		return HttpResponse(rendered_string)
	except DoesNotExist as e:
		url = redirect('post:post_list')
```

<br>

### (10) post_detail 템플릿 만들기

post_detail은 원하는 포스트의 게시일을 눌렀을 때 해당 포스트의 상세페이지를 로드한다. 따라서 고유 id값과 일치하는 포스트 하나를 로드하기 위해서 템플릿을 만들어준다.

```html
{% block content %}
<img src="{{ post.photo.url }}" alt="">
<p>{{ post.author }}</p>
<p>{{ post.created_date }}</p>
{% endblock %}
```

<br>

### (11) view 만들기 - `post_create(request)`

post_create는 `사용자에게 보여줄 화면을 제공하는 기능(GET방식)`과 `사용자가 입력한 값을 넘겨주는 기능(POST방식)`이 함께 구현되어야 한다. 

GET일 때는 post_create 템플릿 양식을 그대로 보여주면 된다.

POST일 때는 사진을 업로드하고 댓글을 달 수 있으며 넣은 데이터를 서버로 전송할 수 있어야한다. 따라서 사용자가 보내온 데이터를 하나의 row로 데이터베이스에 저장하고 페이지를 리다이렉트하여 올린 결과를 보여줘야한다.

```python
### post/views.py

def post_create(request):
	if request.method == "POST":
		post = Post.objects.create(
			author=Post.objects.first()
			photo=request.FILES['files']
		)
		return redirect('post:post_detail', post_pk=post.pk)
	else:
		return render(request, 'post/post_create.html')
```

<br>

### (12) post_create 템플릿 만들기

post_create는 form태그를 사용하여 사용자가 데이터를 입력하고 전송할 수 있도록 한다. name을 붙여 태그이름으로 view를 구현할 수 있도록 한다.

이와중에 form태그 내부에는 반드시 보안을 위하여 `{% csrf_token %}`을 써준다.

```html
{% block content %}
<form action="" method="post" enctype='multipart/form-data>
	{% csrf_token %}
	<input type="file" name="file">
	<input type="text" name="comment" placeholder='댓글달기'>
	<button type="submit">등록</button>
</form>
{% endblock %}
```

### (13) 




