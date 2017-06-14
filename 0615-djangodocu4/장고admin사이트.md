####### 20160614 [Django Documentation]

[문서 바로가기](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/)

# 장고 admin 사이트

> 장고의 가장 강력한 부분 중 하나는 자동 관리 인터페이스이다. 장고는 모델에서 메타 데이터를 읽고 신뢰할 수 있는 사용자가 사이트의 콘텐츠를 관리 할 수 있는 있게 해주는 모델 중심의 빠른 인터페이스를 제공한다. 

> 관리자의 권장 사용은 조직의 내부관리 도구로 제한된다. 프런트엔드 전체를 빌드하기 위한 것이 아니다.

> 관리자는 사용자 정의를 위해 많은 후크를 가지고 있지만 이러한 후크를 독점적으로 사용하려고 할 때는 조심해야한다. 데이터베이스 테이블과 필드의 구현 세부 사항을 추상화하는 프로세스 중심의 인터페이스를 제공해야하는 경우에는 뷰를 만들어 사용한다. 이 문서에서는 Django의 관리 인터페이스를 활성화, 사용 및 사용자 정의하는 방법에 대해 설명할 것이다.

어드민은 기본 프로젝트 템플릿을 제공한다. 터미널에서 `startproject`를 사용하여 프로젝트 폴더를 만들면 바로 어드민 템플릿이 생성된다. 

### 어드민페이지를 위해 만들어야할 것들

1. `settings.py` 내 INSTALLED_APPS에 `django.contrib.admin`을 추가한다.(보통 자동으로 추가되어있음)
2. 또한 어드민페이지를 사용하는 데 필요한 앱을 추가해준다. `django.contrib.auth`, `django.contrib.contenttypes`, `django.contrib.messages`, `django.contrib.sessions`
3. TEMPLATES에 정의된 DjangoTemplates 백엔드의 `context_processors`에는 `django.contrib.auth.context_processors.auth`와 `django.contrib.messages.context_processors.messages`를 추가해주고, MIDDLEWARE에는 `django.contrib.auth.middleware.AuthenticationMiddleware`와 `django.contrib.messages.middleware.MessageMiddleware`를 추가해준다. 이는 모두 프로젝트 생성시 자동으로 추가해주지만, 사용자 정의를 할 경우 수동으로 추가해준다.
4. 앱에 정의해 준 모델 중 관리 인터페이스에서 사용할 모델을 `admins.py`에 등록해준다.

	```python
	### admin.py
	
	admin.site.register(Post)
	```
	
5. 각각의 등록된 모델들에 대해서 선택적으로 ModelAdmin 클래스를 생성해준다. ModelAdmin은 특정 모델에 대한 사용자 정의 된 관리기능 및 옵션을 캡슐화한다.
6. AdminSite를 인스턴스화하고 등록된 모델과 ModelAdmin 클래스에 알려준다.
7. AdminSite 인스턴스를 를 URLconf에 연결해준다.(이것도 `urls.py`에 만들어져 있음)

이 단계를 거치면 설정해준 url패턴으로 접속하여  장고 관리사이트를 사용할 수 있다. 관리페이지에 로그인하기 위해서는 터미널에서 `superuser`를 생성해준다.

<br>

### ModelAdmin 객체들

ModelAdmin 클래스는 관리 인터페이스의 모델을 대표한다. 보통 앱 내 `admin.py`에 저장되어 있다. 

```python
from django.contrib import admin
from myproject.myapp.models import Post

class PostAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Post, PostAdmin)
```

앞의 예제에서 ModelAdmin 클래스는 아직 사용자 정의 값을 정의하지 않았다. 결과적으로는 모델만 등록한 것처럼 기본 관리 인터페이스가 제공된다. **기본 관리 인터페이스에 만족하면 ModelAdmin 객체를 전혀 정의할 필요가 없다.** ModelAdmin 설명을 제공하지 않고도 모델 클래스를 등록할 수 있기 때문이다. 앞의 예제는 다음과 같이 단순화시켜 사용할 수 있다.

```python
from django.contrib import admin
from myproject.myapp.models import Post

admin.site.register(Post)
```

<br>


