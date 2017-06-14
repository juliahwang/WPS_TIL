###### 20170611 [Django documentation]

# QuerySet API reference

### When QuerySets are evaluated

쿼리셋은 실제 평가할 때까지 데이터베이스에 액세스하지 않는다. 그리고 내부적으로 쿼리셋은 실제 데이터베이스에 도달하지 않고 구성, 필터링, 슬라이스 등을 할 수 있다.

다음과 같은 방법을 통해 쿼리셋을 평가할 수 있다.
	
#### (1) Iteration

- 쿼리셋은 순환가능하다.

```python
for i in Entry.objects.all():
	print(e.headline)
```

<br>

#### (2) Slicing

- 쿼리셋은 파이썬의 슬라이싱 문법을 통해서 슬라이스될 수 있다. 
- 평가되지 않은 QuerySet을 슬라이스하면 다른 평가되지 않은 QuerySet가 반환되지만 `슬라이스 구문의 "step" 매개 변수`를 사용하면 데이터베이스 쿼리를 실행하고 목록을 반환한다.
- 평가된 QuerySet을 슬라이스하면 목록도 반환된다.

<br>

#### (3) Pickling/Caching

- QuerySet을 pickle하면 pickling 전에 메모리에 모든 결과가 로드된다. 
- pickling은 일반적으로 캐싱의 선구자로 사용되며 캐싱된 쿼리셋이 다시 로드될 때 결과가 이미 사용되고 사용할 준비가 되기를 원한다.

<br>

#### (4) repr()

쿼리셋 내에서 `repr()`을 호출할 때 쿼리셋이 평가된다. 파이썬 대화형 인터프리터에서 편의를 위해 바로 결과를 볼 수 있도록 API가 내부에서 작동된다.

<br>

#### (5) len()

- 쿼리셋 내에서 `len()`을 호출할 때 쿼리셋이 평가된다. 그리고 길이를 반환한다.
- 만약 평가하지 않고 길이값만 반환하고 싶다면 `count()`를 사용하는 것이 더 효율적이다. 

<br>

#### (6) list()

list()를 사용함으로써 쿼리셋을 강제 평가한다.

```python
entry_list = list(Entry.objects.all()
``` 

#### (7) bool()

- 쿼리셋을 불린 문맥에서 평가한다. 
- bool(), or, and, if문은 모두 쿼리셋을 평가한다.

```python
if Entry.objects.filter(headline="Test"):
   print("There is at least one Entry with the headline Test")
```

만약 단순히 데이터가 존재하는 지만 알고 싶다면 `exists()`를 사용한다.

<br>
<br>

### Pickling QuerySets

쿼리셋을 pickle할 경우, 결과를 피클링하기 전에 메모리에 결과를 저장할 것이다. 

즉, 쿼리셋을 unpickle할 때 현재 데이터베이스에 있는 결과가 아닌 피클된 순간의 결과를 포함한다.

만약 필요한 정보만을 피클하여 새로운 쿼리셋을 데이터베이스로부터 생성하고 싶다면 쿼리 속성을 피클하면 된다.그리고 결과가 저장되지 않은 쿼리셋을 이용하여  원래 쿼리셋을 새로 생성해낼 수 있다. 

```python
>>> import pickle
>>> query = pickle.loads(s) 
# s는 피클링된 데이터를 지니고 있다.
>>> qs = MyModel.objects.all()
>>> qs.query = query 
```
query 속성은 불투명한 객체이다. 쿼리를 만드는 내부를 보여주기도 하고 공개 API의 일부도 아니다. 그러나 속성의 내용을 picke/unpickle하는 것은 안전하고 완벽하게 지원하고 있다.

`+참고`

장고 버전이 높아지면 피클링이 호환되지 않을 수 있다.

<br>
<br>

# QuerySet API

### Methods that return new QuerySets

filter()

exclude()

annotate()

order_by()

reverse()

distinct()

values()

values_list()

dates()

datetimes()

none()

all()

union()

intersection()

difference()

select_related()

prefetch_related()

extra()

defer()

only()

using()

select_for_update()

raw()

<br>

### Methods that do not return QuerySets

get()

create()

`get_or_create()`

	- get_or_create(defaults=None, **kwargs)
	- 키워드인자를 받아서 객체가 있으면 찾아주고 없으면 생성하는 메서드
	- (object, created)라는 튜플을 반환한다.
		object는 생성된, 혹은 반환된 객체를 일컫는다.
		created는 새로운 객체가 생성되었는지 여부를 boolean(True or False)로 반환한다.
		
일반적으로 다음과 같이 써야한다. 

```python
try:
	obj = Person.objects.get(
		first_name='John',
		last_name='Lennon',
		)
except Person.DoesNotExist:
	obj = Person(
	first_name='John',
	last_name='Lennon',
	birthday = date(1999,9,9),
	)
	obj.save()
```

위를 `get_or_create()`로 다음과 같이 사용할 수 있다.

```python
obj, created = Person.objects.get_or_create(
	first_name='John',
	last_name='Lennon',
	defaults={'birthday': date(1940, 10, 9)},
	)
```
옵션 인자를 제외한 키워드 인자는 모두 `get()` 메서드를 사용하여 가져오고, **객체를 찾으면** `('찾은객체', False)` 튜플을 반환한다. 

**만약 여러 개의 값을 찾으면** `get()` 메서드의 속성으로 인해 `MultipleObjectsReturned` 예외를 발생시킨다. 

**객체를 찾지 못하면** 새로운 객체를 인스턴스화하여 저장하고 `('찾은객체', True)`를 반환한다.

<br>

update_or_create() 

bulk_create()

count()

in_bulk()

iterator()

With server-side cursors

Without server-side cursors

latest()

earliest()

first()

last()

aggregate()

exists()

update()

delete()

as_manager()



<br>

### Field lookups

exact

iexact

contains

icontains

in

gt

gte

lt

lte

startswith

istartswith

endswith

iendswith

range

date

year

month

day

week

week_day

time

hour

minute

second

isnull

search

regex

iregex

<br>

### Aggregation functions

expression

output_field

**extra

Avg

Count

Max

Min

StdDev

Sum

Variance

<br>

### Query-related tools

#### Q() objects

#### Prefetch() objects

#### prefetch_related_objects()
