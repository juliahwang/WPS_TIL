###### 20170601 [Django Documentation Tutorial]

## wpsnote - 3, 4, 6, 7

<br>

### 인덱스 뷰 구체화


### 인덱스 템플릿 만들기

djangopolls/template/polls/ 안에 index.html을 만든다.

디폴트 경로에서 커스텀으로 경로를 바꾸게 되면 반드시 `mysite/settings.py`에 디렉터리 위치를 등록해준다.

### 인덱스 뷰 업데이트하기 

(1) loader사용하여 템플릿 불러오기 

polls/index.html 템플릿을 로딩하고 템플릿에 context라는 변수를 전달한다.

context 변수는 템플릿 변수를 파이썬 오브젝트에 맵핑해주는 파이썬 사전이다.


(2) Shortcut : render()

템플릿을 로딩하고 context를 채우고, 템플릿과 함께 HttpResponse를 리턴하는 것은 매우 많이 하는 작업이기 때문에 코드를 간단히 해주는 `render()` 함수를 사용한다. 

`render()`를 사용하면 `loader`와 `HttpResponse`를 임포트하지 않아도 된다.

`render()` 함수는 첫번째 인자로 받은 request(요청) 오브젝트를, 두번째 인자로 템플릿 이름을, 세번째 옵션인자로 context(파이썬 사전)을 전달받는다. 

전달받은 템플릿을 `HttpResponse` 오브젝트로써 전달받은 context를 템플릿의 파이썬 코드에 맵핑하여 페이지로 출력한다.


### 디테일 뷰 : 404 예외처리

요청으로 들어온 question오브젝트의 id가 데이터베이스 상에 존재하지 않을 때 Http404 예외를 발생시킨다.


### Shortcut : Http404

> get_object_or_404() 함수는 장고 모델을 첫 번째 인자로 받습니다. 두 번째 인자로는 키워드 인자를 받고 모델 메니저의 get() 함수에 전달합니다. 그리고 이 모델 메니저는 오브젝트가 존재하지 않을 경우에 Http404 예외를 발생시킵니다.

> get_object_or_404() 이외에도 get_object_or_404()와 똑같이 쓰여지는 `get_list_or_404()` 함수가 있습니다.  다만 get_list_or_404() 함수는 get()이 아닌 `filter() 함수`를 사용하여 모델 오브젝트 리스트를 리턴합니다. 하지만 리스트가 비어있을 경우에는 Http404 예외를 발생시킵니다.


### 디테일 템플릿 만들기

> `{{ question.question_text }}`를 예로 들면 question_text를 찾기 위해 question 오브젝트가 가지고 있는 파이썬 사전을 가장 먼저 검색 하고 사전안에서 찾지 못하면 속성(attribute)에서 다시 검색을 시작합니다. 그리고 속성 검색에서도 실패를 하면, 리스트 인덱스를 검색 합니다.

> `{% for %}` 루프 안에서는 메소드 호출(method-calling)이 발생합니다. **question.choice_set.all은 Python 코드인 question.choice_set.all()로 변환**되며 {% for %} 태그에서 사용 가능한 iterable인 Choice 오브젝트를 리턴합니다.


### 템플릿에서 하드코딩 URL 지우기

urls.py에서 템플릿 링크를 바꾸면 모든 템플릿 링크도 바꿔주어야 한다. 

<a href="/polls/{{ question.id }}/"></a>

<br>

urls.py의 url마다 이름을 부여하여 템플릿에서 변수로 주면 urls.py에서 한번만 바꿔도 모두 적용된다. 

<a href="{% url 'detail' pk=question.id %}"></a>


### 네임스페이싱 URL 이름

하나의 프로젝트 안에 여러 개의 앱이 있을 경우 겹치는 url 이름을 구별시키기 위해 다음과 같이 작성한다. 

<a href="{% url 'polls:detail' question.id %}"></a>


## 장고 튜토리얼 4

### 간단 유저폼 만들기

### 제네릭 뷰 

뷰는 보통 URL안의 파라메터를 보고 데이터베이스에서 필요한 데이터를 가져와 템플릿에 로딩하여 보여준다.

제네릭 뷰 시스템은 뷰를 생성할 때 일반적인 코드의 반복을 없애주는 숏컷을 제공한다.

일반적으로 장고 앱을 만들기 전에 제네릭 뷰를 만들 수 있는지 판단하고 시작할 때부터 사용한다.

#### URLconf 수정

#### 뷰 수정


