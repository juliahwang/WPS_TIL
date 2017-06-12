###### 20170601 [Django Documentation Tutorial]

## WPS NOTE / SS - 1, 2, 3

<br>

### (1) 깃 레포 만들기

.gitignore, README.md 만들기

<br>

### (2) 기본 폴더 만들기

<br>

### (3) 장고 설치

```
$ pip install django
$ pip list
```

<br>

### (4) 장고 프로젝트 시작

명령어에서 `.`을 쓰지 않으면 manage.py가 생기지 않는다!!

`.`은 현재 디렉토리에 장고를 설치하라고 스크립트에 알려주기 때문에 중요해요. (축약된 표시입니다)

```
$ django-admin startproject [name] .
```

<br>

### (5) pycharm 에서 만들어진 프로젝트 폴더 열기

<br>

### (6) 가상환경 수동설정 

	- 세팅(cmd+,)에서 파일 경로찾아서 연결

<br>

### (7) 루트폴더 지정

<br>

### (8) 서버 열어서 실행해보기 

데이터베이스 migration하지 않았다는 경고가 뜨지만 블로그 앱 폴더를 만들어 준 후 세팅에 blog를 추가하고 데이터베이스를 생성해줘도 된다. 

```
$ ./manage.py runserver
```

<br>

#### 포트 번호 변경

```
# 터미널에서 

$ ./manage.py runserver 8080 
```

<br>

#### 공유네트워크 포트로 변경

다른 컴퓨터에서 보고싶을 때.

```
# 터미널에서 

./manage.py runserver 0.0.0.0:8000
```

<br>

#### 앱과 프로젝트

장고의 모든 패키지는 애플리케이션이다. 
앱단위로 기능을 만들어서 하나의 큰 프로젝트에 계속 붙여넣기 할 수 있다.

<br>

### 버전이 업그레이드 되었을 떄

`pip freeze` 하여 현재 설치된 프레임워크 버전을 저장한다.

`pip freeze > requirements.txt` 를 작성하여 나중 버전이 나온 후에도 해당 버전으로 실행할 수 있도록 필요한 버전 정보를 넣어주는 기능이다.


### (9) 앱 폴더 추가하고 settings.py에 앱 추가

```
$ django-admin startapp [앱이름]
```


<br>

(11) view 추가

```python
polls/views.py

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

<br>

### (11) polls/urls.py 생성, mysite/urls.py과 분리

만든 view를 연결해주기 위한 url을 생성한다.

대규모 프로젝트시 앱마다 실행하는 url 패턴이 많아, `mysite/urls.py`에서 다 관리할 수 없으므로 앱 폴더 내에 `url dispatcher(polls/urls.py)`를 생성한다. 

```python
# polls/urls.py

from django.conf.urls import url
from . import views

# from polls import views 와 같은 뜻이다.
# 다만 같은 디렉터리 안에 있기 때문에 .으로 쓴다.


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

<br>

`mysite/urls.py`에는 확장가능한 url패턴을 저장한다. 따라서 패턴 polls/ 뒤에 `$`를 붙이지 않았다. 

```python
# mysite/urls.py 

from django.conf.urls import url, include
from django.contrib import admin

from polls import urls as polls_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^polls/', include('polls.urls')),
    # polls/패턴 뒤에 $를 붙이지 않을 때는 polls/urls.py으로 이동하여(include()) 패턴과 일치하는 url을 추가로 매치.
    url(r'^polls/', include(polls_urls)),
    # 두 방법 모두 기능한다.
    #url(r'^polls/', polls.urls)
    # 위와 같이는 기능하지 않는다(polls에 __init__.py가 없으므로.
]
```

<br>

#### include()

다른 URL 패턴을 포함시킬 때 사용.

함수 URLconf가 다른 URLconf를 참조할 수 있도록 해준다. URL요청이 들어올 경우 루트 URLconf와 매치되는 부분을 잘라내고 나머지 문자열을 `include()`함수가 지정한 다른 URLconf로 보내는 역할을 한다.

`admin.site.urls` 만 예외로 한다.

<br>

#### url()

argument: regex

- 정규표현식. 문자열 패턴 매칭을 위한 구문
- GET, POST 파라미터나 도메인 이름은 확인하지 않는다.


`part1 태그 달기`

<br>

## 데이터베이스 셋업

UTC는 협정세계시이다. 데이터베이스는 UTC로 맞춰져 있지만 세팅에서 타임존을 꺼내와 적용한다.

```python
mysite/settings.py

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

`커밋`

<br>

### (10) 데이터베이스에 모델 스키마(체계) 알려주기

**모델?**

모델은 메타데이터를 포함하고 있는 데이터베이스의 레이아웃

migrate는 models에 정의된 클래스(필드)를 생성할 때마다 데이터베이스에 업데이트해주는 명령어이다. 

어플리케이션은 데이터베이스를 사용하므로 앱 실행 전에 테이블을 만들어야한다.

> **migrate 명령어는 실행되지 않은 모든 마이그레이션을 적용**합니다. (장고는 django_migrations 테이블에 적용된 마이그레이션을 기록하여 모델의 변경된 내용을 데이터베이스 스키마와 싱크해 줍니다.)

> 이러한 마이그레이션 기능은 프로젝트를 개발하는 중에 데이터베이스나 테이블을 삭제하고 새로 만들 필요 없이 모델을 변경 가능하게 해주는 강력한 기능입니다. 특히 데이터 손실 없이 라이브로 데이터베이스를 업그래이드 하게 도와줍니다. 이 부분에 대해서는 강좌 후반부에서 다루도록 하겠습니다. 지금은 모델을 변경하기 위한 3가지 스텝만을 기억하여 주십시오.

```
$ ./manage.py migrate  # 모델 변경
# (models.py에 클래스 추가)
$ ./manage.py makemigrations  # 변경사항에 대한 마이그레이션 파일 생성
$ ./manage.py migrate  # 변경내용을 데이터베이스에 적용
```

> 모델은 데이터를 데이터베이스에 저장하기 위한 데이터의 기초입니다. 모델은 저장할 데이터의 중요한 필드와 데이터 형식등을 가집니다. 장고는 DRY Principle 이라는 중복 제거 원리를 따른며, 데이터 모델을 한곳에 정의하고 그 곳에서 모든 것을 만들고자 하는 이념을 가지고 있습니다. 

<br>

### 모델 만들기 

```python
# polls/models.py

from django.db import models


# Create your models here.
class Question(models.Model):  # 테이블명은 polls_question이 된다.
    question_text = models.CharField('질문내용', max_length=200)  # 필드의 이름은 컬럼의 이름이 된다.
    pub_date = models.DateTimeField('발행일자')
    # Field클래스를 정의할 때 첫 옵션 인수를 사용하면 필드의 이름을 사용자정의할 수 있다.
	
	 def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name='해당 질문', on_delete=models.CASCADE)
    # ForeignKey의 경우 다른 필드 인스턴스와는 달리 이름변수를 verbose_name으로 주어야한다.
    # ForeignKey를 통해 각 Choice클래스마다 Question과 연결된다.
    choice_text = models.CharField('선택내용', max_length=200)
    votes = models.IntegerField('총 투표수', default=0)
    
    def __str__(self):
        return self.choice_text
```

<br>

### settings.py 에 만든 모델 알려주기 

```python
# mysite/settings.py

INSTALLED_APPS = [
	...
	'polls.apps.PollsConfig', 
]
```

<br>

### migration file 만들기

마이그레이션은 모델의 변경 내용이 디스크상에 저장되는 단순 파일이다. 직접 migration __init__.py에서 수정을 할 수도 있다. 

```
$ ./manage.py makemigrations
```

<br>

### DB에 변경사항 업데이트 

```
$ ./manage.py migrate
```

#### 모델을 만든 후 수정사항이 있을 때.

(1) 만든 클래스의 이름이나 필드 이름을 변경할 때


<br>

(2) 클래스에 필드를 추가할 때

```python

some_text = TextField()

```

터미널이 그대로 실행하냐는 질문을 (1) 선택하고 ''(빈 값 != null) 적용한다.
그러면 TextField()

<br>

(3) 다시 롤백하고 싶을 때

반드시 migrations 파일이 있어야 돌아갈 수 있다. 

```
$ ./manage.py showmigrations
# 지울 것 확인

$ ./manage.py migrate polls 0001_initial(돌아가고 싶은 마이그레이션)
# 0001 상태로 돌리기 

$ ./manage.py showmigrations
# 지워졌는지 확인하고 models.py에서도 변경사항을 수동으로 되돌려준다.

$ rm migrations/
# 기록을 지워 다시 0001_initial의 변경사항을 migrate할 수 있도록 한다.
```

`커밋`
"add polls application to INSTALLED_APPS, create Question, Choice models, make DB migrations"

<br>

### database API 사용하기

```python

$ from polls.models import Question, Choice  # 만든 모델 클래스 임포트
$ from django.utils import timezone  # 타임존 임포트


$ q = Question(question_text="What's new?", pub_date=timezone.now())
# q라는 Question의 인스턴스를 생성했으나 데이터가 데이터베이스에 들어가지는 않았다.

$ q.id
$ q.pk   # 저장되지 않았으므로 나오지 않는다.

$ q.save()
# 데이터베이스에 인스턴스 데이터를 저장한다.

$ q.question_text = "what's up?"
$ q.save()
# 값이 바뀔 때도 save를 해준다.

$ q.id = '3'
$ q.save() 
# pk값으로 새로운 인스턴스가 생성된다. 그렇다고 pk값이 바뀌지는 않는다.


$ Question.objects.all()
<QuerySet [<Question: Question object>, <Question: Question object>]>
# 어떤 값이 있는지 보이지 않으므로 models.py 클래스에 각각 __str__매직메서드를 추가해줘야한다.

$ Question.objects.all()
<QuerySet [<Question: Whatup?>, <Question: What's your favorite drink?>]>

$ Question.objects.exclude(id=1).delete()
# 1번 아이디 데이터만 남기고 지우기 

$ q.choice_set.create(choice_text="The sky")
$ Choice.objects.create(question=q, choice_text="The sky")
# 위 두 구문은 같은 기능, 같은 뜻이다. choice_set은 ForeignKey로 관계된 함수의 인스턴스를 넣어 그 필드와 관계된 데이터를 생성한다. 
# 'objects ~' : 테이블 전체에서 가져올 때

$ Choice.objects.filter(question__pub_date__year=2017)
# 테이블 전체 데이터 중 question 인스턴스에서 pub_date안에 년도가 2017인 값만 가져온다. 
```

<br>

#### 모델에 함수 추가 

```python

class Question(models.Model):
	...
	
	def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # 발행한지 하루 이내. DateTimeField를 썼으므로 초까지 계산하여 하루 이내의 것만 return하는 메소드.

```

<br>

### 어드민 관리자 만들기 

```
$ ./manage.py createsuperuser
```

<br>

#### 사용자

관리자는 유저의 비번을 알 수 없다. 비밀번호를 생성할 때마다 해시를 36000번 돌려서 암호화하기 때문.

<br>

#### 어드민에서 모델 보기

어드민에서 모델에 데이터를 추가하려면 만든 모델을 `polls/admin.py`에 추가해준다.

```
# polls/admin.py

from polls.models import Question

admin.site.register(Question)
```

<br>

### 뷰 추가

뷰란 장고 어플리케이션이 사용하는 웹페이지의 한 타입이다. 일반적으로 특정함수를 실행하며 특정 템플릿을 가진다. 

ex_ 블로그, 싱글 포스트, 기간별 아카이브 페이지, 커맨드 액션

투표앱에 추가할 페이지는...

- 인덱스 : 최신 질문을 보여주는 페이지
- 디테일 : 투표 유저폼과 하나의 질문을 보여주는 페이지
- 결과 : 특정 질문에 대한 투표결과 페이지
- 투표 액션 : 특정 질문에 대한 투표 핸들링


장고는 웹페이지와 다른 컨텐츠를 보여주기 위해 뷰를 사용한다. 각 뷰는 파이썬의 함수로 만들어진다.

장고는 url요청이 들어왔을 때 **도메인 네임을 제와한** 나머지 url을 보고 적절한 뷰를 찾아 응답한다.
URL을 보고 맞는 뷰를 찾기 위해 `URLconfs`라는 정규표현식으로 표시된 URL패턴을 뷰에 맵핑하여 준다. 

```python
# polls/views.py

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```


뷰를 연결할 URL 패턴도 추가해준다.

```python
# polls/urls.py

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/ 와 매치되면 views.vote가 실행된다.
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```

<br>

### 뷰 구체화

뷰는 페이지에 대한 어떠한 기능이라도 커스터마이징하여 넣을 수 있다. 

어떠한 기능이 있던지 장고는 뷰로부터 HttpResponse나 에러페이지 둘 중 하나만 리턴받으면 된다.

```python
def index(request):
    """
    최근 5개 질문에 대해 보여주는 뷰
    :param request: 요청
    :return: 최근 5개의 질문
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```


<br>
<br>

### 읽어볼 내용

#### WSGI

> 기존의 파이선 웹 애플리케이션 프레임워크는 웹서버를 선택하는데 있어서 제약이 있었다. 보통 CGI, FastCGI, mod_python 과 같은 커스텀API 중에 하나만 사용할 수 있도록 디자인 되었는데, WSGI는 그에 반하여 low-level로 만들어져서 웹서버와 웹 애플리케이션,프레임워크간의 벽을 허물었다.
> WSGI는 서버와 게이트웨이 , 애플리케이션과 프레임워크 양단으로 나눠져있다. WSGI 리퀘스트를 처리하려면, 서버단에서 환경정보와 콜백함수를 애플리케이션단에 제공해야한다. 애플리케이션은 그 요청을 처리하고 미리 제공된 콜백함수를 통해 서버단에 응답한다. WSGI 미들웨어(라고 불린다.)가 WSGI 서버와 애플리케이션 사이를 보충해주는데, 이 미들웨어는 서버의 관점에서는 애플리케이션으로, 애플리케이션의 관점에서는 서버로 행동한다. 이 미들웨어는 다음과 같은 기능을 가진다.

>> 환경변수가 바뀌면 타겟 URL에 따라서 리퀘스트의 경로를 지정해준다.
>> 같은 프로세스에서 여러 애플리케이션과 프레임워크가 실행되게 한다.
>> XSLT 스타일시트를 적용하는 것과 같이 전처리를 한다.

<br>

#### 장고 초보 개발자가 하는 흔한 실수와 대처법

[바로가기](https://www.toptal.com/django/django-top-10-mistakes)

<br>

### 관계형 데이터베이스

**부모 테이블** : Question

primarykey field|상단바: 필드 또는 컬럼이라고 부른다.(질문)|
---|----|
pk는 데이터 생성시 자동으로 부여 | 값1 |
1| 색깔?
2| 모양?

<br>

**자식 테이블** : Choice

Choice의 <br>primarykey field| ForeignKey<br>(Question) | 필드 또는 컬럼1-1(선택지)|
---|----|----|
pk는 데이터 생성시<br>자동으로 부여 | 1 | 값1
1 | 1 | 빨강
2 | 1 | 노랑
3 | 1 | 주황
4 | 2 | 세모
5 | 2 | 네모
6 | 2 | 원

```python
$ Questions.objects.all()
# Question 테이블의 모든 데이터를 가져온다.
# Question 테이블의 색깔, 모양을 모두 가져올 것임.

$ Choice.objects.all()
# Choice 테이블의 모든 데이터를 가져온다.
# Choice테이블의 1~6번 데이터 모두를 가져올것임.

$ q = Questions.objects.get(id=1)
$ q.choice_set.all() 
# ForeignKey가 1인 자식테이블의 데이터를 모두 가져온다.
# 빨강, 노랑, 주황만 가져올것임.(ForeignKey가 1번인 것들만)
```

<br>

+

만약 손자테이블도 ForeignKey로 Questions와 연결된다면?
(개념만 알아두기)

**손자 테이블** : ChoiceOptions

ChoiceOptions의 <br>primarykey field| ForeignKey<br>(Question) | ForeignKey<br>(Choice) | 필드 또는 컬럼(구체적으로?)|
---|----|----|----
pk는 데이터 생성시<br>자동으로 부여 | 1 | 값1
1 | 1 | 1 | 연한 빨강
2 | 1 | 1 | 새빨간색
3 | 1 | 1 |와인색
4 | 2 | 4 | 정삼각형
5 | 2 | 4 | 직각삼각형
6 | 2 | 4 | 그외 삼각형
