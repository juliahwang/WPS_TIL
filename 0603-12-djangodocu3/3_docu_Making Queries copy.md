###### 20170609 [Django Documentation]

# Making Queries

[문서 바로가기](https://docs.djangoproject.com/en/1.11/topics/db/queries/) 


데이터 모델을 만들면 장고는 자동으로 객체를 생성, 검색, 업데이트 및 삭제할 수 있는 데이터베이스 추상화 API를 제공한다. 이 문서는 이 API를 사용하는 방법을 설명합니다.

```python
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
```

<br>

### 오브젝트 생성 (Creating Objects)

파이썬 객체의 데이터베이스 테이블 데이터를 나타내기 위해서 장고는 직관적인 시스템을 사용한다. 모델 클래스는 데이터베이스 테이블 자체를, 인스턴스는 그 테이블의 특정 레코드를 대변한다. 

객체를 생성하려면 키워드 인자를 사용하여 모델 클래스에 인스턴스를 생성한 다음 save()를 호출하여 객체를 데이터베이스에 저장한다. 

```python
>>> b = Blog(name='Beatles Blog', tagline="All the latest Beatles news")
>>> b
<Blog: Beatles Blog>
>>> b.save()
```

위의 구문은 SQL에서 INSERT를 사용한 것과 같다.

장고는 `save()`를 사용하지 않으면 생성한 객체를 데이터베이스에 저장하지 않는다. 참고로 `save()`는 리턴 값이 없다.

```python
# Tip! - 생성과 저장을 한번에 하려면 create() 사용

>>> b1 = Blog.objects.create(name="Dummy Blog", tagline= "I saved this data with create. No need to save()!")
>>> b1
<Blog: Dummy Blog>
```

<br>

### 오브젝트에 변경사항 저장 (Saving changes to objects)

데이터베이스에 이미 저장된 객체의 변경사항을 저장하기 위해서는 `save()`를 사용한다.

```python
>>> b5 = Blog(name="Will Change", tagline="hello world!")
# b5 객체 생성
>>> b5.save() # 저장
>>> b5
<Blog: Will Change>
>>> b5.name = "New Name"  # 이름을 변경
>>> b5.save() # 반드시 다시 저장
>>> b5
<Blog: New Name>
```

해당 쿼리문은 SQL의 UPDATE를 사용한 것과 같다.

**장고는 객체를 `save()`할 때까지 데이터베이스에 저장하지 않는다!!**

<br>

#### ForeignKey와 ManyToManyField 저장하기

**ForeignKey필드를 업데이트하는 것은 정상 필드를 저장하는 것과 똑같은 방식으로 작동**한다. 해당 필드에 올바른 유형의 객체를 할당하면 된다. Entry 및 Blog의 적절한 인스턴스가 이미 데이터베이스에 저장되었다고 가정하고 Entry 인스턴스 항목의 블로그 속성을 업데이트한다. (아래에서 해당 항목을 검색 할 수 있음).

**(1) ForeignKey 필드 수정하기**

```python
>>> e1 = Entry(blog=b, headline="Beatles is back!", body_text="Beatles, are they real legend?", pub_date=date(2017, 6, 7), mod_date=None) # Entry 인스턴스 생성
>>> e1
<Entry: Beatles is back!> 
>>> e1.save() # 저장하여 데이터베이스에 남기기
>>> b2 = Blog.objects.create(name="Cheddar Talk", tagline="Cheese Cheese")  # 변경해줄 Blog 인스턴스 생성
>>> b2 
<Blog: Cheddar Talk>
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk") 
>>> e1.blog = cheese_blog 
# ForeignKey로 받은 blog를 다른 것에 할당
>>> e1.save() # 저장!
```

<br>

**(2) ManyToManyField 수정하기**

```python
>>> joe = Author.objects.create(name="Joe")
>>> entry.authors.add(joe
... )
>>> entry.authors.all()
<QuerySet [<Author: Joe>]>
```

아래와 같이 `add()`는 한번에 많은 다대다필드의 객체를 저장할 수도 있다. 

```python
>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="george")
>>> ringo = Author.objects.create(name="ringo")
>>> entry.authors.add(john, paul, george, ringo)
# 한꺼번에 다수의 객체를 저장 가능
>>> entry.authors.all()
<QuerySet [<Author: Joe>, <Author: John>, <Author: Paul>, <Author: george>, <Author: ringo>]>
```

<br>

### 객체 검색 (Retrieving Objects)

데이터베이스에서 객체를 검색하려면 **모델 클래스의 Manager**를 통해 QuerySet을 생성하면 된다. 모델의 Manager를 사용하면 QuerySet을 얻을 수 있다. 각 모델에는 최소한 하나의 Manager가 있으며 기본형은 `objects` 이다.

QuerySet은 데이터베이스의 객체 컬렉션이다. 0개에서 여러 개의 필터를 가질 수 있는데 필터는 주어진 매개 변수를 기반으로 쿼리 결과의 범위를 좁힐 때 사용한다.

SQL 용어에서 **QuerySet은 SELECT 문과 같으며 필터는 WHERE 또는 LIMIT와 같은 제한절**이다. 

```python
>>> Blog.objects
<django.db.models.manager.Manager object at 0x1026aa588>
# Blog모델의 매니저 클래스를 출력한다.

>>> b2 = Blog(name='Foo', tagline='Bar')
>>> b2.save()
>>> b2.objects
Traceback (most recent call last):
AttributeError: Manager isn't accessible via Blog instances
# 모델의 객체로는 매니저를 사용할 수 없다!

>>> Blog.objects.all()
<QuerySet [<Blog: Beatles Blog>, <Blog: Dummy Blog>, <Blog: New Name>, <Blog: Cheddar Talk>, <Blog: Foo>]>
# 반드시 모델 클래스에서 매니저를 호출해야한다.
```

**테이블 수준의 작업 = Manager 사용!**

	관리자는 모델 인스턴스가 아닌 모델 클래스를 통해서만 액세스 할 수 있으므로 "테이블 수준"작업과 "레코드 수준"작업을 구분할 수 있다.

<br>

#### 모든 객체 검색하기

해당 테이블(모델클래스)의 모든 데이터를 가져오고 싶다면 `Manager의 all()`을 사용

```python
>>> all_entries = Entry.objects.all()
```

<br>

#### 필터하여 특정 데이터 검색하기

대부분의 경우 필터링을 통해 테이블 데이터 중 필요한 데이터만 가져와야할 때는 `Manager의 filter() 또는 exclude()`를 사용한다.

이러한 하위집합(subset)을 만들려면 필터 조건을 추가하여 초기 QuerySet을 구체화해야한다. QuerySet을 구체화하는 가장 일반적인 두 가지 방법은 다음과 같다.

**(1) `filter(**kwargs)`**

검사할 매개인자(키워드인자)를 만족하는 객체만 골라 새로운 쿼리셋(객체목록)을 반환한다.

<br>

**(2) `exclude(**kwargs)`**

검사할 매개인자(키워드인자)를 **제외한** 객체만 골라 새로운 쿼리셋(객체목록)을 반환한다.

<br>

검사시 사용되는 매개인자(**kwargs)들은 필드조회(Field Lookups)에서 사용되는 형식이어야 한다.

```python
# 예시
>>> Entry.objects.filter(pub_date__year=2017)
<QuerySet [<Entry: Beatles is back!>, <Entry: >, <Entry: Dummy>]>

# 위와 같은 의미이다.
>>> Entry.objects.all().filter(pub_date__year=2017)
```

<br>

##### Chaining filters

필터링을 통해 정제된 쿼리셋 자체도 쿼리셋이다. 따라서 필터함수를 계속해서 연달아 사용하는 것이 가능하다.

```python
Entry.objects.filter(
...     headline__startswith='B'
... ).exclude(
...     pub_date__year__lt=datetime.date.today().year
... ).filter(
...     pub_date__gte=datetime(2016, 1, 1)
... )
>>> <QuerySet [<Entry: Beatles is back!>]>
```

Entry 모델의 객체(데이터) 중에서 headline이 'B'로 시작하고 출간일이 오늘에 해당하는 년도보다 작은 것은 배제하며 2016년 1월 1일 이후로 출간된 것을 찾는다.

<br>

##### Filtered QuerySets are unique

QuerySet을 구체화할 때마다 이전 QuerySet에 바인딩된 새로운 QuerySet을 얻게된다. 각각의 검색은 저장, 사용, 재사용될 수 있는 별개의 고유한 QuerySet을 생성하게 된다.

각각의 쿼리셋은 모두 분리되어 있다. 2, 3번째 쿼리셋은 첫번째 쿼리셋을 정제한 새로운, 그러나 그 자체로 별개의 고유한 쿼리셋이다. 첫번째 쿼리셋도 후의 쿼리셋에 영향을 받지 않는다.

<br>

##### QuerySets are lazy

쿼리셋은 변수에 할당하고 그 변수를 실행하기 전까지는 쿼리셋을 평가하지 않는다.

**실행해야만 쿼리셋은 데이터베이스에 접근**하여 평가를 실시한다.

평가를 한다는 것은 데이터베이스에서 쿼리셋에 관련된 데이터를 가져온다는 뜻.

```python
>>> q = q.exclude(body_text__icontains="food")
# 쿼리셋을 생성하기만 하고 실행하지는 않는다.
>>> print(q)
<QuerySet [<Entry: Beatles is back!>]>
```

<br>

#### `get()`으로 하나의 객체 검색

get()은 반드시 1개의 객체를 검색한다..
ex_ 디테일 뷰 페이지

	get() != filter()[0]

`get()`은 값이 없을 때 `DoesNotExist`에러를 발생시킨다.

또한 `get()`은 값이 2개 이상일 때도 `MultipleObjectsReturned` 에러를 발생시킨다.

<br>

#### 다른 쿼리셋 메소드들

`all()`

`get()`

`filter()`

`exclude()`

#### 쿼리셋 제한하기

```python
	Entry.objects.all()[:10:2] # (o)
	Entry.objects.all().[:-1] # (x)
```

SQL문에는 음수 인덱싱을 처리하는 구문이 없으므로 쿼리셋에서는 음수 인덱싱을 쓸 수 없다.

#### 필드 lookups

```python
>>> Entry.objects.filter(blog_id=4)
# 하나의 예외
```

다른 객체는 필드명을 사용하여 필터링을 하지만 id만 `<필드명>_id` 로 사용한다.

<br>

#### 관계를 포괄하는 조회 (Lookups that span relationships)

```python
>>> Entry.objects.filter(blog__name='Beatles blog')
>>> Blog.objects.filter(entry__headline__contain='Lennon')
# entry 안의 headline 필드가 'Lennon'을 포함하느냐?
```

객체가 참조하는 모델의 어떠한 필드든지 계속해서 타고 들어가 원하는 데이터를 가져올 수 있다.

```python
>>> Blog.objects.filter(entry__authors__name__isnull=True)
# 내용이 없어도 빈값으로 치고 유효한 값을 출력해버린다.(에러 발생 x)
<QuerySet []> 
>>> Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)
# 이러한 차이는 관계를 필터링할 때 생긴다(DateField는 x)
```

<br>

##### 다중 값 관계 확장 (Spanning multi-valued relationships)

(1) `filter()`

```python
>>> Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
# 두 조건을 한번에 만족해야함.
<QuerySet [<Blog: This blog has (Lennon, 2008)>]>

>>> Blog.objects.filter(
... Q(entry__headline__contains='Lennon') &
... Q(entry__pub_date__year=2008)
... )
# 첫번째와 두번째는 같은 쿼리셋이다.

>>> Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008) 
# 헤드라인에 'Lennon'을 포함하는 entry를 모두 불러오고(2개의 블로그목록) pub_date의 년도가 2008인 엔트리의 블로그(다시 2개의 블로그목록)를 불러온다.
<QuerySet [<Blog: This blog has (Lennon, 2017) and (Other, 2008)>, <Blog: This blog has (Lennon, 2008)>]>
```

첫 번째 필터는 쿼리 세트를 헤드 라인의 "Lennon"항목과 연결된 모든 블로그로 제한한다. 세번째 필터는 헤드라인으로 필터링해서 나온 블로그 집합을 다시 2008년에 게시 된 항목과 연결된 블로그 집합으로 더 제한한다.


(2) `exclude()`

exclude()는 filter()와 달리 정확히 제외할 것을 명시해주어야한다. 

```python
>>> Blog.objects.exclude(
... entry__headline__contains='Lennon',
... entry__pub_date__year=2008,
... )
<QuerySet [<Blog: This blog has (Harry, 2008)>]>
# 하나만 해당되도 제외된다. 

>>> Blog.objects.exclude(
... entry__in=Entry.objects.filter(
...     headline__contains='Lennon',
...     pub_date__year=2008,
... ),
)
```

<br>

#### 필터는 모델의 필드를 참조할 수 있다.

`F()`를 사용하여 비교가 가능하다. 

```python
>>> from django.db.models import F
>>> Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
# Entry테이블에서 'n_comments' 값이 'n_pingbacks'보다 큰 값만 필터링하는 쿼리셋
```

`F()`는 덧셈, 뺄셈, 곱셈, 나눗셈 등의 연산이 모두 가능하다. F() 객체끼리 연산도 가능하다.

```python
>>> Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
>>> Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
```

또 언더스코어 2개를 사용하여 `F()`객체와의 관계를 확장할 수도 있다. 

```python
>>> Entry.objects.filter(authors__name=F('blog__name'))
```

date나 time 속성의 필드에서는 `timedelta`객체를 더하거나 뺄 수 있다. 즉, 시간연산이 가능하다.

```python
>>> from datetime import timedelta
>>> Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))
# pub_date날짜로부터 3일 이후에 수정된 mod_date 쿼리셋을 불러온다.
```

비트연산도 가능하다.

```python
>>> F('somefield').bitand(16)
# 이 밖에 .bitor(), .bitrightshift(), .bitleftshift() 가 있다.
```

<br>

#### pk 검색

pk, id 등으로 검사할 수 있다.
pk는 장고에서 가능.

```python
>>> Entry.objects.filter(blog__id__exact=3) # Explicit form
>>> Entry.objects.filter(blog__id=3)        # __exact is implied
>>> Entry.objects.filter(blog__pk=3)        # __pk implies __id__exact
```

<br>

#### Like 구문에서 `%` 와 `_` 를 이용한 이스케이핑

LIKE문 (iexact, contains, icontains, startswith, endswith 및 iendswith)과 같은 필드조회는 LIKE문에 사용된 두 개의 특수문자 (백분율 기호(`%`) 및 밑줄(`_`)를 자동으로 이스케이프한다.

```python
>>> Entry.objects.filter(headline__contains='%')
```

#### 쿼리셋 캐시하기

각 쿼리셋은 데이터베이스를 최소화하기 위해 캐시를 사용한다. 

새로 만들어진 쿼리셋의 캐시는 비어있다. 쿼리셋이 처음 평가될 때 쿼리결과를 쿼리셋의 캐시에 저장하고 결과를 요청한 그대로 저장한다. 그리고 해당 쿼리셋을 다시 쿼리할 때 캐시된 결과를 다시 사용한다.

다음은 2개의 쿼리셋을 만들고 평가한 다음 버린다.

```python
>>> print([e.headline for e in Entry.objects.all()])
>>> print([e.pub_date for e in Entry.objects.all()])
# Entry.objects.all()이 2번 사용되었다.
```

위처럼 사용하면 같은 데이터베이스 쿼리가 2번 평가되고 데이터베이스 로드가 2배로 늘어난다. 또 두 쿼리셋 사이에 Entry 모델이 바뀌거나 추가되면 동일한 데이터베이스 레코드를 포함하지 않을 수도 있다. (그때 그때 불러오므로)

또한 쿼리셋을 print()하는 것은 캐시를 생성하지 않는데, `__repr__()` 함수를 호출하여 전체 쿼리셋의 슬라이스를 반환하기 때문이다.  

따라서 아래와 같이 쿼리셋을 변수에 저장해두고 재사용한다. 

```python
>>> queryset = Entry.objects.all()
>>> print([p.headline for p in queryset]) # Evaluate the query set.
>>> print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation.
```

##### 쿼리셋이 캐시되지 않을 때.

전체 쿼리셋을 슬라이스하여 쿼리셋을 생성할 경우

```python
>>> [entry for entry in queryset]
>>> bool(queryset)
>>> entry in queryset
>>> list(queryset)
```

다음의 경우에는 반드시 캐시된다.

```python
>>> [entry for entry in queryset]
>>> bool(queryset)
>>> entry in queryset
>>> list(queryset) 
```

<br>

### Q 객체를 통한 복잡한 검색

` | ` : or 연산

```python
Q(question__startswith='Who') | Q(question__startswith='What')
```

` & ` : and 연산

```python
Q(question__startswith='Who') & Q(question__startswith='What')
```

` ~ ` : 부정 쿼리 

```python
Q(question__startswith='Who') | ~Q(question__startswith='What')
```

키워드 인수 (예 : filter (), exclude (), get ())를 사용하는 각 조회함수는 하나 이상의 Q 객체를 위치 지정되지 않은 인수로 전달할 수도 있다. 조회 함수에 여러 개의 Q 오브젝트 인수를 제공하면 인수가 "AND"된다.

```python
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
```
Q오브젝트를 반드시 앞에 사용한다.

```python
Poll.objects.get(
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    question__startswith='Who',
)

# or 연산을 하고나서 나머지 and 연산은 Q 오브젝트를 사용하지 않아도 된다.
```

다음과 같이 사용하지 않는다.

```python
# INVALID QUERY
Poll.objects.get(
    question__startswith='Who',
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)

# Q 오브젝트는 항상 키워드보다 앞에 와야한다.
```

<br>

### 객체끼리 비교

쿼리에서는 pk로 비교한다.

```python
>>> some_entry == other_entry
>>> some_entry.id == other_entry.id

# 모델의 primary key 필드명이 name인 경우
>>> some_obj.name == other_obj.name
```

<br>

### 객체 삭제

**(1) 인스턴스 수준의 삭제**

```python
`e.delete()`
```

**(2) 클래스 수준의 삭제**

여러 개를 지울 때는 쿼리셋에서 지운다.

```python
Entry.objects.filter(pub_date__year=2005).delete()
```


실수를 막기 위해 `<모델명>.objects.delete()`는 불가능하도록 막아놨다. 아래와같이 사용해야한다.

	>>> <모델명>.objects.all().delete()

<br>

### 모델 인스턴스 복사 

M2M필드의 인스턴스를 복사할 때는 관계에 대한 정보가 다른 테이블에 저장되어 있으므로 다시 관계를 집어넣어줘야한다. 

```python
entry = Entry.objects.all()[0] # some previous entry
old_authors = entry.authors.all()
# 원래 M2M필드가 가지고 있던 관계정보를 모두 old_authors에 저장
entry.pk = None
entry.save()
# 복사과정을 거친 뒤
entry.authors.set(old_authors)
# 다시 관계정보를 넣어준다.
```


### 객체 수정 

F() 오브젝트에서 객체를 타고 들어가는 것은 불가능

```python
# This will raise a FieldError
>>> Entry.objects.update(headline=F('blog__name'))
```


### 관계된 객체

장고에서는 한쪽 방향으로만 관계를 정의해놓고 정방향 참조, 역방향 참조를 통해 데이터를 가져온다.

정방향 참조는 필드명을 그대로 객체에 사용(`e.blog`)하는 방법이고, 역방향 참조는 해당모델명에 `_set`을 붙여 사용하는 방법이다.(`b.entry_set_all()`)

#### (1) 다대일 관계

ForeignKey 필드를 사용하는 모델에서 외래키 모델은 Manager에 접근할 수 있다. 기본값으로 Manager는 `FOO_set` 과 같이 사용된다. 

```python
>>> b = Blog.objects.get(id=1)
>>> b.entry_set.all() 
```

이러한 `FOO_set`은 ForeignKey필드에 `related_name`옵션을 주어 오버라이드 할 수 있다.

```python
blog = ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries')

>>> b = Blog.objects.get(id=1)
>>> b.entries.all()

# b.entries는 쿼리셋을 반환하는 Manager이다.
>>> b.entries.filter(headline__contains='Lennon')
>>> b.entries.count()
``` 

<br>

#### (2) 다대다 관계

다대다 관계의 끝에는 `automatic API access`가 자동으로 생성된다. API는 다대일 관계의 반대로 작동한다. 

다대다필드는 자기 자신의 필드명을 사용하여 정방향 참조한다.

```python
e = Entry.objects.get(id=3)
e.authors.all()  # 해당 Entry의 모든 Author 객체를 가져온다.
e.authors.count()
```

역참조 모델은 `<모델소문자명>_set`을 사용하여 본래 모델을 역참조한다.

```python
e = Author.objects.get(id=5)
e.entry_set.all()  # 이 Author의 모든 Entry 객체를 가져온다.
```

다대일필드, 다대다필드는 `related_name`을 정의할 수 있어 역참조명 대신 사용할 수 있다. 
역참조명을 정의하면 `_set`으로 끝나는 이름은 사용할 수 없다.

<br>

#### (3) 일대일 관계 

다대일 관계와 매우 비슷하다. 정방향 참조를 지원하며, 매니저 오브젝트를 사용할 수 있다. 

그러나 역참조 시 관계가 일대일이므로 매니저 오브젝트에서는 하나의 객체만 반환된다.

없는 객체가 요청되면 `DoesNotExist` 예외를 발생시킨다.

<br>

### 역참조 관계가 가능한 이유?

다른 객체 관계 매퍼들은 관계를 양쪽에서 정의하라고 요구하지만 장고는 이를 DRY(Don't repeat yourself) 개념을 위반한다고 생각한다. 따라서 장고는 한쪽에서만 관계를 정의하고 역참조를 통해 거꾸로 데이터를 가져올 수 있게끔 설계되었다.

장고가 시작할 때 INSTALLED_APPS의 각각의 앱과 그 안의 모델 모듈들을 불러오고 새로운 모델 클래스가 생성될 때마다 역참조 관계를 생성해둔다. 이를 포함하고 있는 것이 app_registry이며, 이를 import하여 사용하는 것이다.

<br>

