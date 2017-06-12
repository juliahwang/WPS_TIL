###### 20170530 [Djangogirls Tutorial]

## 동적 데이터

#### (1) view(views.py)

 모델(models.py의 Post 클래스)과 템플릿(post_list.html)를 연결한다.
 
 컨트롤러라고 불린다.
 
~~~python
# blog/views.py

from django.shortcuts import render

# 기본 뷰 모델
def post_list(request):
	context = {
	
	}
	return render(request, 'blog/post_list.html', context)
	# render함수에는 사용자가 요청한 request, 요청을 받았을 때 연결할 정적파일, 그리고 보여줄 정보인 context 딕셔너리로 구성되어 있다.
~~~

<br>

#### (2) 쿼리셋으로 응답할 데이터 가져오기

Post 모델에서 블로그 글을 가져오려면 테이블 데이터를 가져오는 것이므로 **쿼리셋**을 사용한다.
 
~~~python
# blog/views.py

from django.shortcuts import render
from .models import Post
# . 은 현재 디렉토리 및 애플리케이션을 의미한다. 동일 디렉터리 내에 해당 파일이 있으므로 상위 폴더명을 쓰지 않아도 내용을 가져온다.


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# post는 가져올 쿼리셋의 이름이다.
	context = {
		'post': post,
	}
	return render(request, 'blog/post_list.html', context)
	# 템플릿을 사용하기 위해 'post' 매개변수를 딕셔너리에 추가한다. 
~~~

<br>

>  쿼리셋 활용예시 Tip

~~~python
# 위와 아래의 구문은 같다.

posts = Post.objects.all().order_by('-created_date')

posts =
Post.objects.order_by('-created_date')
~~~

<br>

## 장고 템플릿

#### (1) 템플릿 태그

HTML에 파이썬 코드를 바로 넣으면 브라우저는 파이썬 코드를 인식하지 못한다.

**why?** 

파이썬은 동적 언어이고 html은 정적 언어이기 때문.

따라서 **템플릿 태그를 이용하여 파이썬 코드를 html로 인식**하게 해주고, 동적인 웹사이트를 만들 수 있다.

<br>

#### (2) post 목록 템플릿 보여주기

`views.py`에서 생성한 post_list 함수에서 데이터를 쿼리셋으로 가져와 `'post'` 변수에 할당해 주었다. 

이 변수를 html에 사용하기 위해서는 아래와 같이 html에 추가해준다.

~~~
<div>
	{{ post }}
</div>

# [<Post: My second post>, <Post: My first post>]
~~~

장고는 `{{ post }}`를 객체 목록으로 이해하고 처리했다. 

위와 같이 뜨면 지저분하므로 목록에서 값만 출력하기 위해서는 `for문`을 사용한다. 

~~~
<div>
	{% for item in post %}  # 실행문에는 '%' 기호를 사용한다.
		{{ item }}  # post 데이터셋 하나씩 출력
	{% endfor %}   # for문이 종료되었다는 표시 
</div>
~~~

<br>

#### (3) 데이터 속성별로 템플릿 보여주기 

글 제목, 본문, 작성자 등을 모두 보여주고 싶을 경우 html과 템플릿 태그를 섞어서 작성

Post모델에서 정의한 각 필드의 데이터에 접근하기 위하여 아래와 같은 표기법을 사용한다. 

`|linebreaksbr ` 

행이 바뀌면 문단으로 변환하도록 하는 의미.

~~~
{% for item in post %}
	<div>
		<p>published: {{ item.published_date }}</p>
		<h1><a href="">{{ item.title }}</a></h1>
		<p>{{ item.text|linebreaksbr }}</p>
	</div>
{% endfor %}
~~~

<br>

## 템플릿 확장하기

#### (1) 기본템플릿(base.html) 생성

장고의 기능 중에 템플릿 확장(template extending)이 있다. 

이 방법으로 동일한(중복되는) 코드를 `base.html`에 넣어놓고 import하여 사용할 수 있다.

**`base.html` 에 추가할 것들**

~~~
{% load staticfiles %}  # html 최상단에 추가하기
{% block content %}  # 내용이 안에 추가된다. 
{% endblock %} # 블록이 들어가는 끝지점을 알려주는 실행문 
~~~

<br>

#### (2) 템플릿 연결하기 

역시 파이썬 코드를 html화하여 사용하는 템플릿 태그를 사용한다. 

~~~
{% extends 'blog/post.html' %}
연결시킬 파일 최상단에 위 코드를 넣는다.

{% block contents %}
... 코드 추가 ...
{% endblock %}
~~~

<br>

## 8. CSS 속성 추가


#### (1) STATIC 파일 위치지정

blog안에 static 폴더를 만들면 디폴트 경로로 장고가 바로 폴더를 찾는다. 따라서 따로 경로를 지정해주지 않아도 된다.

하지만 이경우 폴더 관리하기 힘들다.

그보다는 루트폴더인 `django_app` 하위에 바로 만들어 주고 경로를 따로 지정해주는 것이 낫다. 

#### (2) 정적파일 폴더 만들기

`'static'` 이라는 이름의 폴더를 만들어준다.(사실 아무렇게나 지어도 이름만 통일하면 동작하지만 보기 쉽게 static으로 짓는다.)

<br>

#### (3) 장고에게 static폴더 경로 알려주기 

`mysite/settings.py` 안에 커스텀 경로를 정해주어 장고가 폴더 경로를 찾을 수 있게 한다.

~~~python 
# mysite/settings.py

# 위와 같은 방법으로 django_app/static폴더의 경로를 STATIC_DIR에 할당
STATIC_DIR = os.path.join(BASE_DIR, 'static')
print('STATIC_DIR: ', STATIC_DIR)


STATIC_URL = '/static/'
# /static/으로 시작하는 url은 정적파일들의 위치에서 파일을 찾아 서빙
# 기본값으로는 blog 어플리케이션 안에서 static/을 찾는다.
# 따라서 아래와 같이 적어준다
# 이 리스트(또는 튜플)의 경로는 STATIC_URL로 요청된 파일을 찾는 경로로 사용된다.
STATICFILES_DIRS = (
    STATIC_DIR,
)
~~~

<br>

#### (4) 정적파일 분류하기

부트스트랩을 다운받았다면 `django_app/static` 폴더 안에 넣어준다.

추가적으로 css파일을 적용할 경우에는 따로 `django_app/static` 안에 css폴더를 만들어 넣어준다. 

<br>

## bootstrap 추가하기

#### (1) 웹링크 추가하기

인터넷에 있는 파일을 연결하는 웹링크

html <head></head> 태그 내에 적용할 경우 바로 디자인이 적용되지만 인터넷이 안되는 곳에서는 적용되지 않는다.

~~~
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
~~~

<br>

#### (2) 부트스트랩 설치

[부트스트랩 홈페이지 바로가기](https://getbootstrap.com/)

<br>

## 어플리케이션 확장 - (1) 글보기 페이지(post/n/) 만들기

블로그 게시글 제목을 클릭했을 때 각 페이지마다 보이게 만들려면? 

controller(views.py)에서는 실행할 함수를 만든다. 

urls.py에서는 패턴이 일치하는 url에 콘트롤러에서 만든 실행함수를 연결한다.

<br>

#### (1) `views.py`에 기본형 콘트롤러 만들어주기 

~~~python
# blog/views.py

def post_detail(request):
	context = {
	
	}
	return render(request, 'blog/post_detail.html', context=context)
~~~

<br>

#### (2) `urls.py`에서 클릭했을 때 response로 주어질 url 패턴 만들기

url에 이름을 주어 정적 파일과 url 파일 모두 수정하지 않도록 한다.(DRY 적용)

url파일만 수정해도 이름이 등록되어있으므로 자동으로 적용된다.

~~~python
# mysite/urls.py 내 urlpatterns 리스트에 새로운 url 패턴을 추가한다.

urlpatterns = [
	url(r'post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]

# 번호에 pk라는 이름을 주어 글번호에 따라 다른 데이터를 가져오도록 매치시킬 것이다.
# 정규표현식에서 '+'를 사용한 이유는 1개 이상의 숫자가 반드시 와야하기 때문이다. 
# 포스트 넘버에 'pk'라는 키값을 주고, post_detail()함수에는 위치인자로 pk 매개변수를 할당해준다.
~~~

<br>

#### (3) 다시 `views.py`로 돌아와 뷰에 매개변수 'pk' 추가하기 

post라는 키값을 사용하여 pk값이 매개변수로 주어진 pk변수와 같은 Post객체를 전달한다.

~~~python
# blog/views.py

def post_detail(request, pk):
	context = {
		'post': Post.objects.get(pk=pk)
		# 'pk=' 테이블 데이터 생성시 자동으로 생성되는 primary-key(id)를 불러온다
	}
	return render(request, 'blog/post_detail.html', context=context)
~~~

<br>

#### (4) 보여질 html 템플릿 생성하기

~~~
# templates/post_detail.html

{% extends 'blog/base.html' %}

{% block content %}
	<div class="posts">
	    <p class="publishdate">published: {{ post.published_date }}</p>
	    <h2><a href="/">{{ post.title }}</a></h2>
	    <p class="author"><small>{{ post.author }}</small></p>
	    <p class="text">{{ post.text }}</p>
	</div>
{% endblock %}
~~~

<br>

#### (5) `post_list.html`템플릿에서 제목에 url 이름 부여하기

~~~
# templates/blog/post_list.html

{% extends 'blog/base.html' %}

{% block content %}
<div>
    <div class="buttons">
        <a href="{% url 'post_create' %}" class="btn btn-primary">write</a>
    </div>
    {% for post in posts %}
    <div class="posts">
        <div class="modify_button">
            <a href="{% url 'post_detail' pk=post.pk %}" class="btn btn-primary">modify</a>
            # title에 걸리는 링크는 urls.py에서 패턴으로 할당해준 post_detail url로 연결되고, pk 변수는 데이터셋에서 id값으로 불러오게 된다.
        </div>
        <p class="publishdate">published: {{ post.published_date }}</p>
        <h2><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2>
        <p class="author"><small>{{ post.author }}</small></p>
        <p class="text">{{ post.text|truncatechars:120 }}</p>
    </div>
    {% endfor %}
</div>
{% endblock %}
~~~

<br>

## 어플리케이션 확장 - (2) 글쓰기 페이지(/post/create) 만들기

#### (1) `views.py`에서 post_create 콘트롤러 틀 만들기

~~~python
# blog/views.py

def post_create(request):
	context = {
	
	}
	return render(request, 'blog/post_create.html', context)
~~~

#### (2) `urls.py`에서 패턴 지정하기 

~~~python 
# mysite/urls.py

urlpatterns = [
	url(r'post/create/$', views.post_create, name='post_create')
]
~~~

#### (3) `forms.py`에서 폼 만들어주기

~~~python 
# blog/forms.py

from django import forms


class PostCreateForm(forms.Form):
    title = forms.CharField(
        label='제목',
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    text = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        required=True
    )
~~~

<br>

#### (4) `views.py`에서 method 속성마다 실행문 만들어주기 

~~~python
def post_create(request):
    if request.method == 'GET':
    # 요청의 방식이 GET이면 아래 실행문 실행
        form = PostCreateForm()
        context = {
        'form': form,
    }
    # forms.py에 만들어 놓은 form을 보여준다.
        return render(request, 'blog/post_create.html', context=context)
    elif request.method == 'POST':
    # 요청방식이 POST이면 아래 실행문 실행
        # data = request.POST
        form = PostCreateForm(request.POST)
        if form.is_valid():
        # 유효성 검사시 True이면 아래 실행
            title = form.cleaned_data['title']
            title 변수에 .cleaned_data에 입력값을 할당한 폼을 전달
            text = form.cleaned_data['text']
            user = User.objects.first()
            post = Post.objects.create(
                author=user,
                title=title,
                text=text
            )
            # 새로운 글을 생성할 때는 반드시 author를 지정해주어야 하는데, User는 get_user_model()함수로 가져온다.
            return redirect('post_detail', pk=post.pk)
      		  # redirect는 생성된 글에 url주소를 불러와 생성해주는 reverse함수이다.
        else:
        # 유효성 검사 결과 False이면 화면전환을 해주지 않는다.
            context = {
                'form': form,
            }
            return render(request, 'blog/post_create', context)
~~~

<br>

#### (5) `post_create.html` 생성하기 

~~~

~~~
## 새로운 개념정리 

### POST 요청, method = 'POST'

- 서버의 데이터를 변화시킬 때 보내는 요청이다. 
- 데이터를 새로 만들거나, 수정하거나 지울 때는 보통 POST 요청이다.

### GET 요청, method = 'GET'

- 서버는 GET요청에서 데이터를 조회, 게시해주는 역할만 해준다.


### 사이트간 요청위조

- 사용자에게 보여주는 html파일을 조작하여 링크를 바꾸면 버튼이 실제 요청한 일과 다른 일을 처리하게 된다.


#### csrf

- 응답이 올바른 html에서 왔는지 판단하는 것.
- csrf는 사용자만 받을 수 있다.(다른 외부 해커가 키값을 생성하여 보내면 일치하지 않으므로 블록된다.)
- POST 요청을 받을 때는 서버에서 생성하여 보내주는 특정 키값이 response을 보낼 때 같이 들어있지 않으면 사이트간 요청위조라 간주하고 요쳥을 막는다.
- 따라서 Post요청을 보낼 때는 csrf token 템플릿 태그를 넣어준다.
- 거의 모든 웹 프레임워크에 사용된다.