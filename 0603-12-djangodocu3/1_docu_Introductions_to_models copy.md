###### 20170604-0605 [Django Documentation_models]


# Introduction to Models


[문서 바로가기](https://docs.djangoproject.com/en/1.11/topics/db/models/#model-inheritance)

## model의 정의 

	- 데이터베이스 필드와 데이터가 가지는 필수 행동(메서드)을 정의한다.
	- 각각의 모델은 django.db.models.Model의 서브클래스들이다.
	- 장고는 모델과 쿼리셋을 통해 데이터베이스에 접근할 수 있는 API를 생성할 수 있다.
	
```python
# blog/models.py

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

- first_name과 last_name은 모델의 필드들이다. 
- 각각의 필드들은 클래스 속성들이며 이 속성은 데이터베이스의 컬럼을 나타내기도 한다.
- 위의 모델은 아래의 SQL문과 같다..

```
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);

# PostgreSQL문법을 사용하여 작성한 것.
# id 필드는 데이터 생성시 자동으로 생성된다.(오버라이드 가능)
# Django는 대부분의 ORM이 그렇듯이 설정에 따라 코드 변경없이 다양한 데이터베이스 엔진을 사용할 수 있다.
```

<br>

## Using models

모델을 정의한 후에는 장고에서 어떤 모델을 쓸 것인지 알려줘야한다. `settings.py`에서 정의한 모델이 들어있는 앱이름을 `INSTALLED_APPS`에 넣어준다.



```python
# mysite/settings

INSTALLED_APPS = [
    #...
    'blog',
    #...
]
```

설정에 추가한 후에는 `manage.py migrate` 명령어를 통해 데이터베이스에 모델의 변경(추가)사항을 알려주고, `manage.py makemigrations`로 마이그레이션파일을 만든 후 변경사항을 저장해준다.

<br>

## Fields

모델을 구성하는 가장 중요한 개념은 `필드 선언`이다. 각각의 Fields는 클래스 속성으로, 데이터베이스 필드를 정의하는 하나의 리스트라고 생각하면 된다.

필드 이름은 modelsAPI와 겹치지 않도록 지어야 한다. ex_clean, save, delete

```python 
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```
<br>

### Field의 종류

모델 안의 각각의 필드는 Field 클래스의 인스턴스여야 한다. 장고는 필드 클래스 타입으로 속성을 정의하는 데에 내장 필드타입 또는 직접 만든 필드타입을 사용한다.

	- 컬럼의 종류 (INTEGER, VARCHAR, TEXT 등 데이터의 타입 정의) 
	- django의 Form을 이용하여 기본 HTML 위젯으로 렌더링할 때 각 필드를 어떻게 표현할 지
	- django admin 페이지, 자동생성된 form에서 수행할 최소 유효성 체크(is_valid())
 
+ 직접 만든 필드타입을 사용하는 경우 

전화번호 입력필드에서 양식이 전화번호양식인지 확인하고 싶을 때 필드를 직접 정의하여 사용

<br>

### Field 옵션

각각의 필드에 옵션을 줄 수 있고, 특정필드에만 사용할 수 있는 옵션들도 있다.

	ex_ CharField
	
	CharField 타입에서는 max_lengh를 필수로 주어야 한다. 
	DB에 VARCHAR 컬럼을 생성할 때 길이를 초기화할 수 있기 때문이다.


<br>

#### 선택옵션들의 예시

모든 필드타입에 공통적으로 사용할 수 있는 옵션(선택가능)들 중 자주 쓰는 옵션들 

**null**
	
	- 값이 True일 때 해당 컬럼에서 Null(값을 알 수 없을 때) 값을 줄 수 있다.
	- 데이터베이스에서 NOT NULL과 상관있다.
	- ex_ 고객의 정보를 모를 때, 손실된 데이터, 알 수 없는 데이터
	
**blank**

	- 값이 True이면 필드값이 없는 것을 나타낸다. 
	- DB의 어떠한 제약과도 상관없으나 유효성 검증과 연관있다. 기본 값은 False이다. 
	- HTML 폼 검증 시 blank 옵션을 False로 주면 필수입력필드로 처리된다.
	- ex_ 필수입력필드를 만들고 싶을 때, 단순히 값이 아예 없을 때

**choices**

	- 순환가능한 2중튜플(튜플 안에 값이 2개 있는 튜플 or 리스트) 형태로 설정한다.
	- enum 과 같이 필드에 저장할 수 있는 값을 제한할 경우에 사용한다.
	- 디폴트 form widget은 셀렉트 박스 형태로 표시된다.
	- 따라서 주어진 선택권 안에서만 데이터를 '선택'할 수 있다.  

	YEAR_IN_SCHOOL_CHOICES = (
		('FR', 'Freshman'),
		('SO', 'Sophomore'),
		...
	)
	
	각 튜플의 첫번째 값은 데이터베이스에 저장되는 값이다.
	두번째 값은 디폴트 form widget에 저장되거나 ModelChoiceField에 저장된다.
	데이터베이스에 저장되는 값과 사용자에게 보여지는 값을 다르게 설정가능.

choices가 보여지는 방법은 `get_FOO_display() 메소드`를 사용한다.

`get_shirt_size_display()`

```python
# blog/models.py

class PersonShirts(models.Model):    SHIRT_SIZES = (        ('S', 'Small'),        ('M', 'Medium'),        ('L', 'Large'),    )    name = models.CharField(max_length=60)    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


# ./manage.py shell
>>> from blog.models import PersonShirts
>>> p = PersonShirts(name="Fred", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'   # DB에 저장된 형태
>>> p.get_shirt_size_display()
'Large'  # 사용자에게 보여지는 형태
```	

**default**

	- 필드 값에 기본으로 주어지는 값이다.
	- 단순 value나 함수 모두 가능하다.
	- 함수를 옵션으로 설정하면 새로운 모델객체(인스턴스)를 만들 때마다 함수가 호출된다.
	
**help_text**

	- 필드가 폼위젯으로 표시될 때 함께 표시하는 도움말을 설정할 수 있다.
	- 해당 모델을 폼에서 쓰지 않더라도 모델을 문서화하는 데 도움이 된다.
	
**primary_key**

	- 별도의 설정이 없으면 장고는 'id'라는 IntegerField를 모델에 자동으로 추가한다.
	- 그리고 그 필드에 'primary_key=True' 옵션이 자동으로 설정된다.
	- 디폴트 primary_key옵션을 덮어쓰고 싶을 경우에는 원하는 필드에 'primary_key=True'을 주면 된다. 
	
	- primary_key 필드는 읽기 전용이다.
	만약, primary_key가 적용된 값을 변경하고 저장하면 값이 바뀌는 게 아니라 복사가 되며, 해당데이터 다음에 새로 생긴다.
	
```python
# blog/models.py
class Fruit(models.Model):    name = models.CharField(max_length=100, primary_key=True)

# ./manage.py shell
>>> fruit = Fruit.objects.create(name='Apple'). # 데이터 생성
>>> fruit.name = 'Pear' # 생성된 데이터의 이름필드 변경
>>> fruit.save() # 저장
>>> Fruit.objects.values_list('name', flat=True) # name필드의 데이터 호출
<QuerySet ['Apple', 'Pear']> # Apple이 Pear로 변경되는 게 아니라 새로 생성되었다.
``` 

**unique**

	- True이면 해당 필드값은 해당 테이블 안에서 유일한 값을 가져야한다.(unique 제약)
	
<br>
	
### Automatic primary key fields

기본값으로 장고는 각각의 모델들에 다음과 같은 필드를 제공한다.

```python
id = models.AutoField(primary_key=True)

# 이는 auto-increment(자동으로 1씩 증가하는) primary key 필드이다.
``` 

custom primarykey를 주고싶은 경우에는 이 키값을 주고 싶은 필드에 `primary_key=True`옵션을 주면된다. 장고는 다른 필드에 해당 설정이 있는 것을 확인한 순간 자동 id 컬럼을 생성하지 않는다. 

각 모델들은 디폴트이든 커스텀 설정이든 **반드시 primary_key=True 설정이 주어진 1개의 필드를 포함해야 한다.**

<br>

### Verbose field names

각 필드타입들은 첫번째 위치인자로써 'verbose_name'이라는 선택옵션 위치인자를 가진다.

```python 
# first_name 필드에 'person's first name'이라는 verbose_name 속성값을 주었다. 

first_name = models.CharField('person's first name', max_length=30)
```

`verbose_name`이 주어지지 않으면(선택옵션이므로) 장고는 필드의 속성이름을 이용해 자동으로 생성한다.
속성값의 언더스코어(`_`)를 스페이스로 변환한 것이 필드의 verbose_name이다. 

```python
# first_name의 verbose_name은 'first name'이다. 

first_name = models.CharField(max_length=30)
```

<br>

예외) ForeignKey, ManyToManyField, OneToOneField은 첫번째 인자를 클래스로 받야하 하므로 `verbose_name= 이 붙은 키워드인자`를 가진다.

```python
poll = models.ForeignKey(Poll, verbose_name="the related poll")
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(Place, verbose_name="related place")
```

`verbose_name`을 지정할 때는 관습적으로 첫글자를 포함하여 모두 소문자로 설정한다.
장고가 필요한 경우에는 알아서 해주기 때문.

<br>

### Relationships

관계형 테이블의 가장 큰 영향력은 테이블 간의 관계를 정의할 때 나타난다.
장고는 3가지의 가장 일반적인 테이블 간 관계 형태를 제시한다. 

`many-to-one`, `many-to-many`, `one-to-one`

#### (1) 일대다, `one-to-many` 관계

**`django.db.models.ForeignKey` 를 사용하여 관계를 정의한다.**

`ForeignKey`는 모델 내의 필드타입처럼 해당 필드에 클래스 속성으로 할당한다.

`ForeignKey`는 해당 모델과 관련있는 클래스명을 첫번째 위치인자로 받는다. 

```python
# many-to-one relationshipclass Manufacturer(models.Model):    # ...    passclass Car(models.Model):    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
```

```python
# many-to-one example
class Reporter(models.Model):    first_name = models.CharField(max_length=30)    last_name = models.CharField(max_length=30)    email = models.EmailField()    def __str__(self):        return "%s %s %s" % (self.first_name, self.last_name, self.email)class Article(models.Model):    headline = models.CharField(max_length=100)    pub_date = models.DateField()    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)    def __str__(self):        return self.headline    class Meta:        ordering = ('headline',)
```

쿼리셋에서 테스트 해보기

```python
# 기자 정보 생성
>>> r = Reporter(first_name='julia', last_name='hwang', email='hello@example.com')
# 기자 정보 저장
>>> r.save()

>>> from datetime import date
# reporter에 생성한 데이터를 연결한 기사 정보 생성 
>>> a = Article(id=None, headline='test page is opened', pub_date=date(2017, 6, 3), reporter=r)  
# 저장
>>> a.save() 
# 두번째 테이블에서 첫번째 테이블의 정보를 가져올 수 있다.
>>> a.reporter.id   
1
>>> a.reporter
<Reporter: julia hwang>

# r의 정보와 연결된 기사를 모두 가져온다.
>>> r.article_set.all() 
# 위의 명령줄과 같다.
>>> Article.objects.get(reporter=r)  

# 기자 정보 생성 후 저장하지 않으면 pk값이 생성되지 않는다. 따라서 외래키에서 불러올 수 없다.
>>> r = Reporter(first_name='julia', last_name='hwang', email='hello@example.com')
```

**일대다 관계에서 재귀적 사용**

```python
models.ForeignKey('self', on_delete=models.CASCADE)
```

**역참조**

모델에 ForeignKey가 있는 경우 외래 키 모델의 인스턴스는 `Manager`를 통해 첫 모델의 모든 인스턴스에 접근 가능하다. 기본적으로 Manager는 `Foo_set`의 형태로 제작되며 `FOO`는 모델명을 소문자화한 것이다. 

이 Manager는 쿼리셋을 반환하여 필터, 수정, 생성 등을 할 수 있다. 

```python
>>> Car.objects.get(pk=1)
>>> m = Manufacturer.objects.get(pk=1)
>>> m.car_set.filter(pk=1)
```

<br>

#### (2) 다대다, `many-to-many` 관계

**`ManyToManyField`를 사용하여 다대다 관계를 정의한다.**

이 또한 모델 내의 필드타입처럼 해당 필드에 클래스 속성으로 할당한다.

`ManyToManyField`는 첫번째 위치인자로 관계있는 모델클래스명이 필요하다.

예시> 피자는 다양한 토핑이 필요하다. 토핑 또한 다양한 피자종류에 공통적으로 넣을 수 있다.

```python
from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
```

쿼리문 실행 

```python
In [27]: Pizza.objects.filter(toppings__id__lte=2)
Out[27]: <QuerySet [<Pizza: SuperSupreme pizza>, <Pizza: SuperSupreme pizza>, <Pizza: cheese pizza>]>
# 토핑의 id가 2 이하, 그 중 1개는 2개의 피자에 들어있으므로 supersupreme이 2번 나온다.

In [28]: Pizza.objects.filter(toppings__id__lte=2).distinct()
Out[28]: <QuerySet [<Pizza: SuperSupreme pizza>, <Pizza: cheese pizza>]>
# 중복제거

In [29]: Pizza.objects.filter(toppings__id__lte=2).distinct().count()
Out[29]: 2
# count()는 반드시 distinct()를 먼저 쓴 후 사용

In [30]: Pizza.objects.filter(toppings__id__lte=2).count().distinct()
# 반대로 사용하면 AttributeError 발생

In [32]: Topping.objects.filter(pizza__name__startswith='cheese').exclude(name='cheese')
Out[32]: <QuerySet [<Topping: tomato sauce>]>
# 토핑 중에 피자이름이 cheese로 시작하는 피자에 속한 토핑인데 'cheese'토핑을 제외한 값

In [33]: t_cheese.delete()
Out[33]: 
(3,
 {'introduction_to_models.Pizza_toppings': 2,
  'introduction_to_models.Topping': 1})
삭제하면 중간테이블, 토핑테이블에서 삭제된 값을 알려준다.
```

또한 재귀관계를 나타낼 수 있다. 
즉, 다대다 관계를 지니는 테이블 자신과 재귀관계를 가질수는 있으나 추천하지는 않는다.

**ManyToManyField를 넣어줄 필드명은 복수형(ex_ toppings)으로 짓는 것이 좋다.**

**어떤 모델이 ManyToManyField를 가지는지는 상관없지만, 두 모델 중 하나에만 넣어야 한다.**

일반적으로 ManyToManyField는 폼에서 편집할 수 있는 객체에 할당된다. 위의 예시에서 토핑은 여러 종류의 피자 위에 있는 모습보다는 피자 안에 토핑이 있는 것을 떠올리기가 더 일반적이고 자연스럽다. 따라서 Pizza 모델 안에 toppings 필드를 두고 ManyToManyField를 설정한 것이다. 

또, Pizza 폼에서 사용자들은 토핑을 고를 수 있게 된다.

<br>

#### `many-to-many` 관계에서의 다양한 필드들 

ManyToManyField는 다른 추가 인자(선택)들을 가지고 있다.
Pizza와 Topping 은 ManyToManyField만 선언하면 되지만 두 모델 간 관계에 추가적인 데이터가 들어가는 경우가 많다.

예를 들어 음악 밴드들에는 각각 뮤지션들이 가입되어 있고 다대다관계를 가지고 있다. 그런데 뮤지션들이 가입한 날짜를 넣고 싶다면 어떻게 해야할까?

이런 경우 장고에서는 다대다 관게를 가지는 모델 이외에 추가 데이터를 저장할 또다른 `중간모델(intermediate)`을 정의하게 해준다.

이 `중간모델`에 저장하고 싶은 필드를 넣으면 된다. 
`중간모델`은 기본 두 모델 중 다대다관계 속성을 준 필드에 `through` 인자를 통하여 알려줘야 한다. 

**만약 중간모델에 같은 모델의 pk를 불러오는 ForeignKey 필드가 2개 이상 있을 경우에는 어떤 필드로 해당 모델의 row를 받아올 지 모호해진다. 따라서 소스모델의 `ManyToManyField`에 `through-fields`를 설정해 정확히 어떤 필드로 연결할 지 정의해줘야한다.**

소스모델 - ManyToManyField 가 정의된 모델
대상모델 - ManyToManyField 가 정의되지 않은 모델 

```python
class Musicians(models.Model):
	name = models.CharField(max_length=128)
	
	def __str__(self):  # Musicians 객체를 만들고 출력할 수 있게 해준다. 
		return self.name
		
		
class Group(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(Musicians, through='Membership') 
	# members에 Musicians 모델과의 다대다관계필드를 주었다.
	# 추가 데이터를 위해서는 through 인자에 Membership 중간모델을 설정했다. 
	
	
class Membership(models.Model):
	person = models.ForeignKey(Musicians, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	# 모델 두개 모두 ForeignKey(일대다관계)로 받아온다.
	# 자기자신에게 다대다 관계를 가지는 모델의 경우에는 중간모델에 동일한 모델에 대한 ForignKey를 2개 선언하기도 한다.
	date_joined = models.DateField()   # 추가 데이터필드를 정의한다. 
	invite_reason = models.CharField(max_length=300)
```

쿼리셋에서 실행해보기

```python
>>> from blog.models import *
>>> ringo = Musicians.objects.create(name="Ringo Starr") # Musicians 인스턴스 생성
>>> paul = Musicians.objects.create(name="Paul McCartney") # Musicians 인스턴스 생성
>>> beatles = Group.objects.create(name="The Beatles") # Group 인스턴스 생성
>>> m1 = Membership(person=ringo, group=beatles, date_joined=date(1962, 8, 16), invite_reason="Needed a new drummer")
# Membership 인스턴스 생성, person에 Musicians의 인스턴스, group에 Group의 인스턴스를 각각 할당하였다.
>>> m1
<Membership: Membership object>
>>> m1.save()  # 반드시 저장해야함
>>> beatles.members.all()
<QuerySet [<Musicians: Ringo Starr>]>
>>> m2 = Membership(person=paul, group=beatles, date_joined=date(1962, 8, 1), invite_reason="Wanted to form a band.")
>>> beatles.members.all()
<QuerySet [<Musicians: Ringo Starr>]>
>>> m2.save() # 저장하지 않으면 등록되지 않는다. 
>>> beatles.members.all()
<QuerySet [<Musicians: Ringo Starr>, <Musicians: Paul McCartney>]>
```

<br>

**중간모델이 있는 경우 add(), create(), set()로 관계생성 불가**

```python
# 에러 발생
>>> beatles.members.add(john)
>>> beatles.members.create(name="George Harrison")
>>> beatles.members.set([john, paul, ringo, george])
```

그 이유는 해당 쿼리셋 구문이 `Musicians모델`과 `Group모델`의 관계를 설명해줄 수 없기 때문이다. **이 관계는 `Membership모델`의 모든 필드를 충족시켜서 객체를 생성하여 정의되어야 한다.** add나 create는 추가 요소들을 구체화할 수 없다. 

따라서 add, create, set 메소드는 다대다 관계에서 쓸모가 없다. 

`remove()` 메소드도 같은 이유에서 사용할 수 없다. 중간모델인 `Membership`의 인스턴스를 지우기 전까지는 `Musicians`나 `Group`의 인스턴스를 지워도 관계정보가 남아있으므로 지워지지 않는다. 


```python
>>> Membership.objects.create(person=ringo, group=beatles, date_joined=date(1968, 9, 4), invite_reason="You've gone for a money and we miss you")
<Membership: Membership object>
>>> beatles.members.all()
<QuerySet [<Musicians: Ringo Starr>, <Musicians: Paul McCartney>, <Musicians: Ringo Starr>]>
>>> beatles.members.remove(ringo)

AttributeError: Cannot use remove() on a ManyToManyField which specifies an intermediary model. Use blog.Membership's Manager instead.
```
 
대신 `clear()`는 다대다 관계의 모든! 인스턴스들을 지우는데 사용된다. 

```python
>>> beatles.members.clear()
>>> Membership.objects.all()
<QuerySet []>
```

관계를 생성하고 지울 때 제약이 있다. 하지만 필터를 하거나 값을 가져올 때는(쿼리) 일반 다대다관계와 동일하게 사용한다. 

```python
# 필터 

>>> Group.objects.filter(members__name__startswith='Paul')
[<Group: The Beatles>]
``` 

```python
# 중간모델의 필드를 사용가능 

Person.objects.filter(
	group__name='The Beatles',
	membership__date_joined__gt=date(1961,1,1))
[<Person: Ringo Starr>]
```

```python
# Membership 모델에서 직접 쿼리 가능

>>> ringos_membership = Membership.objects.get(group=beatles, person=ringo)
>>> ringos_membership.date_joined
datetime.date(1962, 8, 16)
>>> ringos_membership.invite_reason
u'Needed a new drummer.'
```

```python
# Person객체에서 membership 다대다역참조를 해도 쿼리 가능

>>> ringos_membership = ringo.membership_set.get(group=beatles)
>>> ringos_membership.date_joined
datetime.date(1962, 8, 16)
>>> ringos_membership.invite_reason
u'Needed a new drummer.'
```

<br>

#### (3) `one-to-one` 관계

`OneToOneField`를 사용하여 일대일 관계를 정의한다.

다른 필드타입과 같이 모델 내의 클래스 속성으로 정의한다. 

하나의 모델을 다른 모델로 `확장`할 때 유용하게 쓰인다. 
예를 들어, '가게정보'가 담긴 모델을 정의하고 그 안에 가게에 대한 기본정보 필드를 구현했다. 그런데 맛집정보를 가게정보에 추가하려고 한다면 새로 모델을 만들어 기존의 기본정보 필드를 다시 추가하는 것보다 OneToOneField를 선언하여 기존 모델을 새 모델의 내용으로 확장하게 할 수 있다.

ForeignKey 필드와 마찬가지로 자기자신, 아직 선언되지 않은 모델에 대해서 관계를 가질 수 있다.

일대일필드는 parent_link 속성을 가질 수 있다.

	- True이고 다른 모델에서 상속받은 모델일 경우, 해당 필드가 서브클래스의 일대일관계필드가 아닌 부모모델을 참조하는 링크로 쓰인다. 


사용 예시

```python
# one-to-one example

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # Place 모델을 확장하여 핫도그, 피자 판매여부 필드를 추가한 Restaurant모델 정의
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
	# 레스토랑과 일대다 관계를 가지는 웨이터 모델을 정의했다.
	
    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
```

쿼리셋 실행

```python
>>> p1 = Place(name='Demon Dogs', address='shinsa')
>>> p1.save()
>>> p2 = Place(name='Ace Computer', address='gangnam')
>>> p2.save()
>>> r = Restaurant(place=p1, serves_hot_dogs=True, serves_pizza=False)
>>> # Restaurant에 Place모델의 인스턴스 p1을 할당하고 추가 필드를 작성한 r 객체 생성
>>> r.save()
>>> r.place 
<Place: Demon Dogs the place>
>>> r.restaurant # set을 쓰지 않고 바로 접근 가능
<Restaurant: Demon Dogs the restaurant>
>>> hasattr(p2, 'restaurant') 
# hasattr(<row변수명>, '문자'), 해당 변수에 문자가 들어있는지 체크(에러검사)
False
```

<br>

### 파일 간 모델들 (models across files)

앱 간에 모델들을 연결할 수 있다. 현재 models.py에서 다른 앱의 관계된 모델이 있는 models.py 파일을 불러오는 명령어를 현재 models.py 맨 윗줄에 추가해준다. 
 
```python
from django.db import models
from geography.models import ZipCode


class Restaurant(models.Model):
	zip_code = models.ForeignKey(
		ZipCode,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
```

### 필드이름 제한 (Field name restrictions)

장고에서 모델필드 이름을 제한하는 경우는 단 2가지다.

#### (1) python 예약어는 안돼!

```python
# pass는 파이썬 예약어이므로 필드명에 사용할 수 없다.

class Example(models.Model):
	pass = models.IntegerField()
```

#### (2) 1개 이상의 연속된 언더스코어(`_`)를 포함할 수 없다!


```python
# 장고의 쿼리문이 언더스코어를 2개 사용하므로 겹치지 않도록 단어구분시 1개만 써준다.

class Example(models.Model):
	foo__bar = models.IntegerField()  # (x)
	foo_bar = models.IntegerField()  # (o)
```


**Field.db_column**
	
	- 지정하고 싶은 데이터베이스 컬럼명이 python, SQL예약어라 곤란한 경우 사용한다.
	- .db_column은 장고가 테이블명을 파이썬, sql 에러를 피해 지정할 수 있도록 해준다.


SQL 예약어의 경우(join, where, select 등)에는 필드이름으로 허용된다. (어차피 문자열로 쓰게 되므로) Django가 쿼리문을 만들때, 모든 컬럼명과 테이블 명을 모두 이스케이프 처리하기 때문이다. 실제 데이터베이스 엔진에 맞게 알아서...


### 직접 만드는 필드타입들 (Custom field types)

장고의 내장 필드타입은 모든 가능한 데이터베이스 컬럼 타입을 포함하지 않는다. 따라서 목적에 맞게 필드타입을 정의하여 사용할 수 있다. 

```python
class Hand(object):
	"""A hand of cards"""
	
	def __init__(self, north, east, south, west):
		self.north = north
		self.east = east 
		self.south = south
		self.west = west		
```

쿼리문 실행

```python
>>> example = MyModel.objects.get(pk=1)
>>> print(example.hand.north)
>>> new_hand = Hand(north, east, south, west)
>>> example.hand = new_hand
>>> example.save()
```

<br>

## 메타 옵션 (Meta options)

내부 메타 클래스를 선언하여 모델에 메타데이터를 선언해줄 수 있다.

```python
class Ox(models.Model):
	horn_length = models.IntegerField()
	
	class Meta:
		ordering = ["horn_length"]
		verbose_name_plural = "oxen"
```

모델의 메타데이트는 필드 단위의 옵션이 아닌 모델 단위의 옵션이다. 

모델의 메타데이터는 필드가 아닌 것들을 지정할 때 사용한다. 예를 들어 `정렬옵션(ordering)`, `데이터베이스 테이블명(db_table)`, `읽기좋은 이름(verbose_name)`이나 `복수(plural)이름`을 지정해줄 수 있다.

모델클래스의 메타클래스는 선택사항이다. 

<br>

## 모델 속성 (Model attributes)

**objects**

```python
class Person(models.Model):
	"""manager를 직접 지정해줄 경우"""
	people = models.Manager()
```

모델 클래스에서 가장 중요한 속성(어트리뷰트)는 `Manager`이다. 

Manager 객체는 모델 클래스 선언을 기반으로 실제 데이터베이스에 대한 쿼리 작업을 제공하거나 데이터베이스 레코드를 모델객체로 인스턴스화 하는데 사용되는 인터페이스이다. 

모든 모델에 최소 하나 이상의 Manager가 있다.

	 >>> Example.objects.all()

**Manager를 할당하지 않으면 장고는 Default Manager객체를 클래스 속성(어트리뷰트)으로 자동 할당한다. 이 때의 어트리뷰트 이름이 `objects`이다.**

Manager는 모델클래스를 통해 접근하며 모델 인스턴스를 통해서는 접근 불가하다. 

	>>> Example.objects.all()  (o)
	>>> r.objects.all()  (x)

<br>

## 모델 메서드 (Model methods)

"테이블 단위"의 기능을 구현할 때는 Manager에 구현해준다. 

"레코드(row) 단위"의 기능을 구현하고자 할 경우 모델 클래스에 메서드를 구현해준다. 모델메서드의 경우 특정 모델 객체에서만 작동한다. 

모델에서 비지니스 로직을 구현할 때 자주 사용되는 기법이다. 

```python

class BirthPerson(models.Model):    first_name = models.CharField(max_length=100)    last_name = models.CharField(max_length=100)    birth_date = models.DateField()    def babe_boomer_status(self):        """BirthPerson의 베이비부머 상태를 알려준다"""        import datetime        if self.birth_date < datetime.date(1945, 8, 1):            return "Pre Boomer"        elif self.birth_date < datetime.date(1965, 1, 1):            return "Baby Boomer"        else:            return "Post Boomer"    @property    def full_name(self):        """BirthPerson객체의 이름 전체를 반환한다"""        return '%s %s' % (self.first_name, self.last_name)
        # 
```

<br>

모델에 자동으로 주어지는 메서드들이 있고, 이를 override하여 직접 메서드를 만들 수도 있다. 그 중 항상 오버라이드 해줘야할 메서드는 다음과 같다.

### (1) `__str__()`

python3에서는 `__unicode__`를 `__str__`이 대신한다. 기본출력은 도움이 되지 않으므로 override하여 대화형콘솔, 어드민에서 오브젝트를 출력하여 보여주고 싶을 때 사용한다.

### (2) `get_absolute_url()`

이 메서드는 객체를 위하여 장고가 어떻게 URL을 연산할지 알려준다. 장고는 관리자 인터페이스에서 해당 메서드를 사용하며 오브젝트의 URL을 알아내야하는 곳이라면 언제든 사용한다. 

URL이 유일한 객체라면 해당 메소드를 사용하는 것이 좋다.  

<br>


### 미리 정의된 모델 메서드를 재정의하기 (Overriding predefined model methods)

모델 메서드에는 데이터베이스의 여러 동작을 커스터마이징하여 캡슐화할 수 있는 다른 모델메서드 세트들이 있다. 예를 들어, `save()`나 `delete()`의 경우에는 그 방식을 바꾸고 싶을 때가 많다. 

해당 메서드를 오버라이드하여 수행할 행동을 바꿔줄 수 있다. 

내장 메서드를 오버라이드하는 일반적인 예로는 저장할 때마다 몇가지 동작을 더 추가해주는 메서드를 재정의하는 것이다. 예를 들어 저장할 때마다 저장내용에 대한 이메일을 보내준다든지...

```python
class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()
	
	def save(self, *args, *kwargs):
		do_something()
		super(Blog, self).save(*args, **kwargs)  # 원래 save()메서드를 호출
		do_something_else()
```

혹은 저장을 막을 수도 있다.


```python
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
    def save(self, *args, **kwargs):
    if self.name == "Yoko Ono's Blog":
    	return # Yoko shall never have her own blog!
    else:
    	super(Blog, self).save(*args, **kwargs) 
    	# super()로 데이터베이스에 저장, 원래 save()메서드 내 인자 호출
```

이 경우에는 본래의 부모클래스의 메서드를 호출하고 save()를 호출해 저장해야한다. override하더라도 객체가 데이터베이스에 여전히 저장되어야하기 때문이다. 부모클래스의 메서드가 없으면 본래 동작(저장)이 호출되지 않으므로 데이터베이스에 데이터가 저장되지 않는다. 

	super(Blog, self).save(*args, **kwargs)

또한 원래 save() 괄호 안에 있던 인자들을 모두 받아오기 위해서 `위치인자(*args)`와 `키워드인자(**kwargs)` 모두를 써준다. 따라서 미리 정의된 모든 인자를 포함시켜준다.

<br>

**벌크 조작시 오버라이드 모델 메서드가 실행되지 않는다.**

	delete()를 사용하여 대량의 데이터를 삭제, 계단식으로 데이터를 삭제할 때(벌크조작)
	호출이 안된다. 이 경우에는 pre_delete나 post_delete를 사용한다. 
	
	한편, 대량의 데이터를 create나 update할 때는 오버라이드된 메서드를 실행할 수 없다.
	pre_save나 post_save도 없고 해결책이 없다...
	
<br>

### 커스텀 SQL문 실행하기 (Exacuting custom SQL)

모델 메서드나 모듈 레벨의 메서드에 SQL문을 직접 만들어서 사용할 수도 있다. 

```python
class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)
```

쿼리문 실행

```python
>>> for p in Person.objects.raw('SELECT * FROM myapp_person'):
...     print(p)
John Smith
Jane Jones

# 대화형 프롬프트에서 바로 SQL문을 사용할 수 있다.
```

<br>

## Model inheritance

장고 모델의 상속은 파이썬의 상속과 거의 같다. 단, 모델 상속의 경우 베이스 클래스는 `django.db.models.Model` 클래스의 서브클래스여야 한다.

**(1) Abstract class** - 추천!

부모는 테이블을 생성하지 않고 자식 모델들이 부모 모델에 선언된 공통 필드를 각자 자신의 테이블에 생성할 것인가?

	- 이 경우 부모 클래스는 자신의 테이블을 만들지 않고 자식 클래스에 필드선언, 메서드선언만 상속해준다. 
	- 상속받은 자식모델은 데이터베이스 테이블에 상속받은 부모 테이블과 자기자신의 필드로 구성된 테이블을 가진다. 

<br>

**(2) Multi-table 상속** - 웬만하면 쓰지 않음

부모가 자신의 데이터베이스 테이블을 가지도록 할 것인가?
	
	- 이미 존재하는 모델(먼저 선언되어 사용되고 있었거나 테이블을 생성한)을 상속할 경우
	- 부모 모델은 자신의 데이터베이스를 가져서 자식 모델과 별개로 사용할 수 있다.
	- OneToOneField와 똑같이 동작한다.

<br>

**(3) Proxy model**

	- 모델의 필드 선언은 전혀 변경하지 않고 파이썬 레벨의 코드만 수정할 경우

<br>

### (1) Abstract base classes

추상 클래스방식은 **여러 개의 모델 클래스가 공통적인 정보를 가지도록 하고 싶은 경우**에 유용하다.
**Meta class에 abstract=True 옵션을 선언하면 그 모델 클래스는 추상클래스가 된다.** 이 클래스는 데이터베이스에 테이블을 생성하지 않으며 다른모델이 이 클래스를 상속받아 테이블을 만든다. 부모클래스의 필드들은 자식클래스의 테이블에 추가되고, 만약 컬럼이름이 겹치면 에러가 나게 된다. 

```python
class Commoninfo(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField()
	
	class Meta:
		abstract = True  
		# 해당 선언을 통해 Commoninfo는 추상클래스가 되었다.
		# 이부분은 상속되지 않는다. 
		# 자식도 추상클래스로 만들려면 자식모델 하위에 메타클래스로 다시 명시해준다.

class Student(CommonInfo): # 상속방법은 파이썬과 동일
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return 'HomeGroup {}\'s student({}, {})'.format(
            self.home_group,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_student'


class Teacher(CommonInfo):
    cls = models.CharField(max_length=20)

    def __str__(self):
        return 'Class {}\'s teacher ({}, {})'.format(
            self.cls,
            self.name,
            self.age,
        )
```

상속을 통해 `Student모델`은 3개의 필드를 가진다.

쿼리문 실행

```python
>>> CommonInfo.objects.all()
Error! 테이블이 생성되지 않았으므로.
```

`Commoninfo모델`은 추상클래스이기에 더이상 일반 장고 모델로 기능할 수 없다. **데이터베이스 테이블을 만들지 않고 manager(objects)도 없으며 객체화되거나 저장될 수도 없다.**

<br>

#### Meta inheritance

추상클래스가 만들어질 때 장고는 그 안에 선언한 메타 내부 클래스를 속성으로 만든다. 자식모델이 메타클래스를 선언하지 않으면 부모의 내부 메타클래스가 상속된다. 자식모델이 부모의 메타클래스를 확장할 수도 있다. 

```python
class Commoninfo(models.Model):
	# ...
	class Meta:
		abstract = True
		ordering = ['name']
		
		
class Student(Commoninfo):
	# ...
	class Meta:
		db_table = 'student_info'
```

이때 장고는 내부적으로 조정을 하는데, 자식모델의 Meta클래스를 활성화하기 전에 부모의 abstract를 False로 변경한다. 추상클래스를 상속해서 자식모델도 추상클래스가 되지 않도록 방지하는 것이다. 만약, 자식모델도 추상클래스로 만들고 싶다면 자식의 메타클래스에 `abstract=True`로 선언해주면 된다.

부모모델과 자식모델의 메타 클래스를 따로 지정한 이유는 추상클래스에서 지정할 수 없는 속성이 있기 때문이다. 추상클래스는 테이블을 만들지 않으므로 `db_table`과 같은 속성은 자식모델의 메타클래스에 따로 지정해준다.

<br>

#### Be careful with `related_name` and `related_query_name`

`related_name`이나 `related_query_name`을 `ForeignKey` 또는 `ManyToManyField`에 사용할 경우 그 필드에는 유일한 이름을 사용해야한다. 추상클래스에서는 이것이 종종 문제가 되는데, 추상클래스 내의 필드들이 모두 같은 값을 가진 채 자식모델로 포함되기 때문이다.

```python
name = models.ForeignKey(
		Manufacturer,
		on_delete = models.CASCADE,
		related_name= 'cars',
		# 역참조할 때
		# m = Manufacturer.objects.first()
		# m.cars
		related_query_name='manufacturer_car',
		# 쿼리에서 필터할 때
		# Manufacturer.objects.filter(manufacturer_car__name='320')
		)
```

```python
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    # cars 필드에 MTM으로 related_name, related_query_name을 설정 후 migrate
    cars = models.ManyToManyField(
        Car,
        related_name='%(app_label)s_%(class)s_related',
        # 역참조 c.teacher_set이 더이상 동작하지 않는다.
        # c.introduction_to_models_teacher_related
        related_query_name='%(app_label)s_%(class)ss'
        # 역방향 쿼리 필터시 모델명을 사용하면 동작하지 않는다.
        # >>> Teacher.objects.filter(cars__name__contains="d")
        # <QuerySet [<Teacher: Class wps's teacher (julia, 20)>]>
        # >>> Car.objects.filter(introduction_to_models_teachers__name='julia')
        # <QuerySet [<Car: 520d>]>
    )
```

**따라서 `related_name`, `related_query_name`을 추상클래스에서 사용할 때는 값의 일부가 '%(app_label)s' and '%(class)s'를 포함해야한다.**

**'%(class)s'** : 사용된 자식클래스의 필드명을 소문자화한 이름으로 대체된다.

	- %(abc)s % (abc='help!') 위의 s는 문자열 포맷(s)를 나타낸다.

**'%(app_label)s'** : 자식클래스가 속해있는 앱이름을 소문자화한 이름으로 대체된다. 각가의 애플리케이션 이름들은 유일해야하며 하나의 앱 내의 모델 클래스 이름도 유일해야한다. 따라서 이 두개의 조합으로 유일한 이름을 만드는 것이다.

```python
# common/models.py 

class Base(models.Model):
	m2m = models.ManyToManyField(
		OtherModel,
		related_name="%(app_label)s_%(class)s_related",
		related_query_name="%(app_label)s_%(class)s",
	)
	
	class Meta:
		abstract = True
		
		
class ChildA(Base):
	pass
	
	
Class ChildB(Base):
	pass
```

`ChildA.m2m 필드의 역참조 이름`은 `common_childa_related`가 된다.
`ChildB.m2m 필드`는 `common_childb_related`가 된다.

```python
# rare/models.py

from common.models import Base

class ChildB(Base):
	pass
```
rare/models.py의 ChildB 클래스의 역참조 이름은 `rare_childb_related`이다.
`OtherModel`은 총 3개의 역참조 속성(어트리뷰트)를 가지게 된다.

이렇게 하지 않고 `related_name 옵션`을 주지 않으면 각각 `childa_set`, `childb_set`이 되어 구별 가능하지만, 다른 앱에서 사용된 동일 클래스명도 `childb_set`이라는 이름을 갖게 되므로 에러가 난다. 

<br>

### (2) Multi-table inheritance

부모, 자식모델 모두 각자의 데이터베이스 테이블을 가진다. 공통부분의 데이터는 부모모델의 테이블에 저장하고 자식모델의 고유한 데이터만 자식모델 테이블에 저장하는 것이다. 

자식모델은 부모 모델에 대한 링크를 가진다. 이 링크는 OneToOneField를 통해 연결된다.

해당 방법은 상위 모델의 테이블을 사용할 수 있으므로 편리하다. 그렇지만 상속을 많이 사용하게 되므로 성능이 현저히 떨어질 수 있다. 되도록이면 추상테이블 기법을 사용하는 것이 좋다. 만약 1개의 상속을 받는 경우에는 `OneToOneField`를 사용한 것과 마찬가지이므로 사용해도 성능이 나빠지지 않는다.

```python
class Place(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	
	
class Restaurant(Place):
	serves_hot_dogs = models.BooleanField(default=False)
	serves_pizza = models.BooleanField(default=False)
```

Place 모델 자체에서도 테이블이 생기므로 쿼리문을 사용할 수 있다.

```python
>>> Place.objects.get(id=1)
```
 
Place 모델에 선언된 모든 필드는 Restaurant 모델에서 사용할 수 있고, 각각의 테이블에 저장된다. 

```python
>>> Place.objects.filter(name="Bob's Cafe")
>>> Restaurant.objects.filter(name="Bob's Cafe")
```

Place모델과 Restaurant 모델을 모두 만족하는 객체가 있다면 Restaurant모델명을 소문자화한 이름으로 Place모델 객체에서 Restaurant모델에 데이터에 접근할 수 있다. 

```python
>>> p = Place.objects.get(id=12)
# p가 Restaurant 모델의 객체이면 자식클래스에게 전달된다.
>>> p.restaurant
<Restaurant: ...>
```

반면에 p가 Restaurant의 속성을 가지고 있지 않으면((Place 모델을 통해 직접 생성되었다거나, Restaurant 모델이 아닌 다른 자식클래스를 통해 만들어진 경우) DoesNotExist 에러가 난다.

```python
>>> a = Place.objects.create(name="Bob's Forge", address="LA")
>>> a.restaurant
# Restaurant.DoesNowExist 예외 발생
```

Place 모델과 자동으로 연결되는 Restaurant 모델의 OneToOneField는 다음과 같다.

```python
place_ptr = models.OneToOneField(
	Place, 
	on_delete = models.CASCADE,
	parent_link = True,
)
``` 

Restaurant 모델의 OneToOneField에 `parent_link=True` 속성을 주어 본래 필드를 오버라이드할 수 있다.

<br> 

#### Meta and multi-table inheritance

멀티 테이블 상속에서 자식 모델이 부모의 메타클래스를 상속하는 것은 말이 되지 않는다. 모든 메타 옵션들은 부모모델에서 지정해주었고 그것을 자식모델에서 다시 정해주는 것은 모순 동작을 일으킬 수 있기 때문이다. (추상 클래스와 반대임-부모클래스가 일반모델이 아니므로)

**따라서 자식모델은 부모의 메타클래스에 접근할 수 없다. 그러나 자식이 부모의 행동을 상속받을 수 있는 몇가지 제한적인 방법도 있다.**

	- 자식이 정렬 속성(ordering)을 정의하지 않았을 때.
	- get_latest_by 속성이 없을 때

	이 경우에는 부모의 속성을 받아온다.

부모의 메타클래스에 정렬속성이 있으나 자식모델에 상속하고 싶지 않다면 자식 메타클래스에서 속성을 오버라이드 해준다.

```python
class ChildModel(models.Model):
	# ...
	class Meta
		# 부모의 정렬속성을 없애는 방법은 아래줄과 같이 재정의해주는 것이다.
		ordering = []
```

<br>

#### Inheritance and reverse relations

멀티테이블 상속은 암묵적으로 OneToOneField을 생성한다. 이미 CommonInfo2의 필드(부모)를Students2(자식)에서 상속받아 사용하고 있는데, extra_info로 ForeignKey필드를 만들게 되면 어떤 것을 받아올 지 모호해지므로 `related_name`을 지정해준다. 

```
class CommonInfo2(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ('-name',)
        db_table = 'introduction_to_models_mti_commoninfo'

class Student2(CommonInfo2):
    home_group = models.CharField(max_length=5)
    extra_info = models.ForeignKey(
        CommonInfo2,
        related_name='extra_students',
        null=True,
        blank=True,
    )
    # ForeignKey필드나 ManyToManyField를 더 선언해줄 경우.
```

<br>

#### Specifying the parent link field

앞에서 언급했듯이 멀티테이블 상속의 경우 OneToOneField 가 자동으로 생성된다. **만약 이 OneToOneField를 직접 지정하고 싶다면**, OneToOneField를 하나 더 추가하고 필드 옵션에 `parent_link=True`로 설정해주면 된다.

<br>

### (3) Proxy Models

멀티테이블 상속을 사용할 때 새로운 데이터베이스 테이블은 부모모델의 자식클래스들에 의해 생겨난다. 자식클래스는 부모클래스에 없는 추가 데이터 필드를 저장할 수 있기 때문에 사용하는 것이 일반적이다. 

**그러나 가끔은 모델의 파이썬 동작만을 변경하고 싶을 때도 있다. 아마도 기본 관리자(objects)를 변경하거나 새로운 메소드를 추가하고 싶을 때는 Proxy model을 사용한다.**

예를 들어 기본 모델을 관리자 권한을 가진 사용자가 실행했을 때와 사용자가 실행했을 때의 메서드를 각각 다르게 정의하고 싶다면 관리자용 메서드를 프록시모델로 정의하여 만들어두고, 사용자용도 다른 프록시 모델로 정의하여 각각 다르게 동작하도록 하는 방법이 있다. 

프록시 모델은 `부모모델의 '프록시(proxy); 임시, 대리'`를 생성하고 싶을 때 사용한다.

	- 프록시모델의 인스턴스를 생성, 삭제, 수정할 수 있다.
	- 마치 부모모델에 데이터를 조작하는 것처럼 동작한다. 
	- 기본 모델의 정렬방법이나 기본관리자(objects)를 기본모델 자체를 수정하지 않고도 프록시모델을 통하여 수행할 수 있다.
	- 또한 프록시모델은 일반 모델처럼 선언한다. 

장고에게 프록시모델임을 알려주는 설정은 다음과 같다. 

프록시 모델의 메타클래스에 `proxy=True`를 적용한다.

```python
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class MyPerson(Person):
	class Meta:
		proxy = True    # MyPerson은 Person의 프록시모델이다.
		
	def do_something(self):
		# ...
		pass	
```

MyPerson모델은 Person모델의 데이터베이스 테이블을 사용한다. 또, Person의 인스턴스는 MyPerson모델을 통해서도 접근 가능하다.

```python
>>> p = Person.objects.create(first_name="foobar")
>>> MyPerson.objects.get(first_name="foobar")
<MyPerson: foobar>

# Person과 MyPerson은 데이터 생성, 수정, 필터시 row의 pk값을 공유한다. 
```

기본 정렬순서를 바꿔주고 싶을 경우 프록시모델을 사용한다. 

```python
class OrderedPerson(Person):
	class Meta:
		ordering = ['last_name']
		proxy = True
```

<br>

#### QuerySets still return the model that was requested

장고에서 프록시모델은 오로지 본모델의 연장으로만 사용되는 것이지 새로운 창조물로 기능하지 않는다. 즉, MyPerson 객체를 생성해도 Person 객체로만 인식할 것이다. 

**프록시 객체의 목적은 본모델의 본래 코드를 기준으로 연장된 몇가지 설정을 사용하는 데에 있다.** 
만약 Person모델을 재창조한 모델로 사용하기 위해 프록시 모델을 사용했다면 다른 방법을 알아봐야할 것이다.(추상클래스...)

<br>

#### Base class restrictions

**프록시 모델은 반드시 추상클래스가 아닌 1개의 모델로부터 상속받아야한다.** 프록시모델로는 여러개의 비추상클래스모델 테이블로부터 레코드를 쿼리할 수 없기 때문이다. 

추상클래스모델의 경우에는 모델이 필드를 가지지 않을 때(메서드만 가질 때) 몇 개든 상속이 가능하다. 

프록시 모델에서 선언하지 않은 Meta옵션은 부모 모델로부터 상속받게 된다.

<br>

#### Proxy model managers

**프록시 모델에 manager를 지정하지 않으면 부모의 manager를 상속받는다.** 직접 지정하면 그 설정을 따르고, 부모 manager도 사용할 수 있다. 

manager는 다음과 같이 변경한다. 

```python
class NewManager(models.Model):
	# ...
	pass
	

class MyPerson(Person):
	objects = NewManager()
	
	class Meta:
		proxy = True
```

아래처럼 부모모델의 기본 manager를 상속받고 새로운 manager를 추가할 수도 있다. 추상클래스에 새로운 manager를 선언하고 그 추상클래스를 상속받는다. 

```python
# 새로운 manager를 위해 추상클래스를 선언

class ExtraManagers(models.Model):
	secondary = NewManager()
	
	class Meta:
		abstract = True
		

class MyPerson(Person, ExtraManagers):
	class Meta:
		proxy = True

# 단, 흔하지 않은 방법이다. 잘 사용하지 않는다...
```

<br>

#### Differences between proxy inheritance and unmanaged models

**장고에서 테이블을 만들지 않게 하려면??**

1) 프록시 모델 정의

2) 모델 클래스를 하나 선언한 후 `managed=False` 속성을 주면 해당 모델은 테이블을 생성하지 않는다. 이 때 `db_table` 과 같은 데이터베이스 속성을 주면? 

방식 | proxy model | unmanaged model
---- |---------| ------
데이터베이스 생성방식 | 아예 데이터베이스 테이블을 생성하지 않고, 부모모델의 테이블을 갖다쓴다.| 데이터베이스 테이블이 자동으로 생성되지 않는다.
수정여부 | 원본모델이 변경되도 프록시모델은 수정사항이 거의 없다.| 직접 데이터베이스 테이블을 생성/수정해야한다.
manager 처리방식 | 프록시모델은 원본의 기본 manager 뿐만 아니라 모든 매니저를 상속받는다. | 원본모델과 관련이 없으므로 자체 선언에 따른다./ 다중테이블 상속의 경우에는 부모의 manager를 상속받지 않는다.


**어떤 것을 사용할까?**

> 1. 만약 이미 존재하는 모델이나 데이터베이스 테이블을 참조하되, 원본 테이블의 모든 컬럼이 필요하지 않다면, Meta.managed=False 옵션을 사용하세요. Django에 의해 제어되지 않는 데이터베이스 뷰나 테이블을 사용하는 경우에 유용합니다.

> 2. 만약에 기존 모델의 파이썬 코드들을 오버라이드 하되, 원본 모델과 동일한 필드를 가지도록 하고 싶다면 Meta.proxy=True 옵션을 사용하세요.

<br>

### 다중상속, Multiple inheritance

파이썬처럼, 장고모델도 다중상속이 가능하다. 이 때는 파이썬의 `name resolution rules`이 적용된다. 다양한 부모로부터 상속받을 떄 각각의 Meta클래스 중에 첫 부모의 Meta클래스를 상속받고, 나머지는 무시하는 것이다. **따라서 상속 순서가 중요!(이렇게 잘 쓰지는 않는다.)**

장고에서는 여러 부모모델을 상속하는 경우가 딱히 없지만 `mix_in`클래스처럼 공통으로 사용하는 필드나 메서드를 묶어서 하나의 클래스로 선언하고 여기저기 상속하는 경우가 있다. 이 때는 특정 필드가 어느 부모 클래스에 선언되어있는지 명확해야한다.

생성된 날짜, 수정된 날짜 등은 mix_in 클래스를 정의하여 만들어놓고, 다른 글작성 모델에서 상속받아 사용한다. 

```python
# django_app/utils/models/mixins.py

from django.db import models


class TimeStampedMixin(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    # 객체가 생성된 시간을 자동으로 기록
    modified_date = models.DateTimeField(auto_now=True)
    # 객체가 업데이트된 시간을 자동으로 기록
    
    class Meta:
        abstract = True
        
# django_app/models/mixin.py

class User(TimeStampedMixin):
    name = models.CharField(max_length=20)
    # created_date = models.DateTimeField(auto_now_add=True)
    # # 객체가 생성된 시간을 자동으로 기록
    # modified_date = models.DateTimeField(auto_now=True)
    # # 객체가 업데이트된 시간을 자동으로 기록


class Post(TimeStampedMixin):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    # 글 1개에 대하여 작성자는 1명이므로 ForeignKey 사용
    title = models.CharField(max_length=100)
    content = models.TextField()
    # created_date = models.CharField(max_length=10, default='abc')


class Comment(TimeStampedMixin):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    content = models.TextField()
```

<br>

### Field name “hiding” is not permitted

파이썬 클래스 상속에서 자식클래스는 부모클래스의 속성을 오버라이드할 수 있다. **장고에서는 필드 속성의 경우 오버라이드가 불가능하다.** 비추상 부모클래스에 'author'라는 이름의 필드가 선언되어 있으면 자식클래스에는 동일한 필드명을 선언할 수 없다!

이는 **필드 속성**에만 해당한다. 부모 모델의 필드를 오버라이드하면 `FieldError`를 발생시킨다.

다만, 추상클래스 모델에서 상속된 모델 필드는 이런 제한이 없다. 왜냐하면 추상클래스는 그 자체의 테이블을 만들지 않기 때문이다. 예를 들어, 위의 모델 중 Post모델에서는 TimeStampedMixin 모델에서 상속받은 created_date를 자동으로 받아오고 싶지 않을 때 다음과 같이 사용한다. 

```python
class Post(TimeStampedMixin):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    # 글 1개에 대하여 작성자는 1명이므로 ForeignKey 사용
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.CharField(max_length=10, default='abc')
    # 같은 이름으로 필드를 작성하고 데이터생성시 default 값이 들어간다.
```

<br>

## Organizing models in a package

manage.py startapp 명령어는 models.py가 있는 앱 구조를 생성한다. 모델이 많다면 하나의 파일에 넣기보다 여러 파일로 분리해서 관리하는 것이 좋다. 

바로 **모델 패키지(models package)**를 만드는 것이다. 

1) 기존 models.py를 삭제한다.

2) myapp/models 디렉토리를 생성하고 `__init__.py`를 만들어 패키지로 만든다.

3) 해당 디렉토리에는 모델들을 저장할 다른 파일들도 만든다. 

4) `__init__.py`에 사용할 모델이 있는 파일을 import한다. 

```python
from .car import Car, Manufacturer
from .person import Person
```

`from .models import *` 보다 각각의 모델을 개별 임포트 해주는 것이 좋다.

	- 네임스페이스가 뭉치는 것을 방지
	- elqjrldtl코드의 가독성을 높인다.
	- 코드 분석툴을 유용하게 한다.

<br>
