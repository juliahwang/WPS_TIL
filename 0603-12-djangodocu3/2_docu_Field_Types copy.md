
###### 20170606 [Django Documentation_models]

# Field Options

### null

	- True일 때 장고는 데이터베이스에 빈값(Null)을 넣는다.
	- 기본값은 False이다.
	- CharField나 TextField에는 사용하지 않는 것이 좋다. "no data"를 뜻하는 Null과 빈 문자열 ""이 모두 가능해지기 때문이다.
	- CharField가 unique=True, blank=True를 모두 갖고 있는 경우에는 예외로 null을 써서 여러 개의 빈 문자열 값을 저장할 때 unique 제한을 받지 않도록 한다.
	- null옵션은 데이터베이스 저장에만 영향을 미치므로 문자열/비문자열 필드 모두 빈 값을 허용하고 싶을 때는 blank=True를 쓰는 것이 좋다. 
	- BooleanField에 null을 사용하고 싶다면 NullBooleanField를 사용한다.

<br>

### blank

	- True일 때 빈 값을 허용한다.
	- 기본값은 False이다.
	- null은 데이터베이스와 관련있는 옵션이고 blank는 유효성과 관련있다.
	- blank=True이면 유효성검사 시 빈 값을 허용한다.
	- blank=False이면 필수 입력 필드가 된다.

<br>

### choices 

	- 필드에 선택사항을 주고 싶을 때 순환가능한 객체가 있는 순환가능한 객체(이중튜플,이중리스트)를 사용하여 선택지를 만들 수 있다.
	- 기본값은 기본텍스트 필드 대신 셀렉트박스를 생성한다.
	- 튜플의 첫 값은 데이터베이스에 저장되는 값이다.
	- 튜플의 두번째 값은 사용자에게 보여지는 값으로 저장될 내용과 달리 설정할 수 있다.

```python
from django.db import models

class Student(models.Model):
	YEAR_IN_SCHOOL = (
		('FR', 'Freshman'),
		('SO', 'Sophomore'),
	)
	name = models.CharField(max_length=20)
	year_in_school = models.CharField(
		max_length = 2,
		choices = YEAR_IN_SCHOOL,
		default = FRESHMAN,
	)
```

모델 클래스 밖에서 리스트를 만들수도 있지만 chice옵션을 사용하면 클래스 내에서 정보를 불러와 사용가능하고 해당 모델을 import했다면 언제나 사용가능하다.

가능한 선택지들을 이름붙인 그룹으로 만들어 광범위하게 사용할 수도 있다. 

<br>

#### `get_FOO_display()`

choice 셋이 있는 모델필드에서는 장고가 데이터베이스이름(튜플첫값)으로 사용자정의이름(튜플두번째값)을 검색할 수 있는 메소드인 `get_<choice필드명>_display()`를 추가해놓는다.

이 메소드로 현재 필드의 값을 찾을 수 있다. 

```python
>>>p = Student(name= "Julia" year_in_school="FR")
>>>p.save()
>>>p.get_year_in_school_display()
'Freshman'
```

<br>

#### ForeignKey의 사용

choice는 어떠한 순환가능한 객체라도 가능하다. 즉, 리스트나 튜플에 국한되는 것은 아니다. choice는 원래 정적인 데이터인데 만약 이를 동적으로 다루고 싶다면 `ForeignKey` 필드를 사용해야한다.

<br>

#### blank=False

choice 옵션이 주어진 필드에 blank=False가 주어지지않는 한 기본값은 `-------`로 표시된다. 

만약 `선택하지 않음`을 선택지로 만들고 싶다면 choice 튜플 안에 `(None, 'Not choosing anything')` 을 추가한다. 첫번째 값은 `None` 또는 `''`, 빈 값을 넣어도 된다. 두번째 값은 적고싶은 어떤 것이라도 가능하다. 

<br>

### db_column

	- 데이터베이스에서 해당 필드(=컬럼)에 사용할 이름을 지정해줄 수 있다. 
	- 이 값이 주어지지않으면 장고는 필드명을 컬럼명으로 사용한다.
	- 데이터베이스 컬럼명을 SQL예약어나 파이썬 변수명으로 사용할 수 없는 단어로 하고 싶을 때 db_column으로 주면 장고가 알아서 처리해준다.(특히 하이픈)

<br>

### db_index

	- True이면 해당 필드에 데이터베이스 인덱스(색인)가 생성된다. 

<br>

### db_tablespace

	- 필드에 색인이 있는 경우,이 필드의 색인에 사용할 데이터베이스 테이블 공간의 이름을 지정하는 옵션이다.
	- 기본값은 프로젝트의 DEFAULT_INDEX_TABLESPACE 설정이 설정된 경우나 모델의db_tablespace가 있는 경우다.
	- 백엔드가 인덱스를 위한 테이블공간을 지원하지 않으면 이 옵션은 무시된다.

<br>

### default

	- 기본값은 새 모델 인스턴스가 만들어지고 값이 필드에 제공되지 않을 때 사용된다.
	- 필드에 기본값을 설정하는 옵션으로, 값이 될 수도 있고 함수가 올 수도 있다.
	- 함수가 디폴트로 주어지면 객체가 생성될 때마다 함수가 실행된다.
	- 람다(lambda)는 마이그레이션으로 직렬화가 불가능하여 기본값 옵션에 사용할 수 없다.
	- 모델 인스턴스에 매핑되는 ForeignKey 필드의 경우에는 기본값이 참조하는 필드값(pk)여야 한다.
	- 필드가 primary key인 경우 필드가 None일 때 기본값 옵션을 줄 수 있다.

새 모델에 대한 인스턴스들이 모두 해당 객체의 기본값을 따르게 되므로 디폴트는 변하는 객체(인스턴스, 리스트, 셋)가 올 수 없다.

대신 함수를 사용하면 아래와 같이 사용할 수 있다. 

```python
def contact_default():
	return {'email': 'tol@example.com'}
	
contact_info = JSONField("ContactInfo", default=contact_default)
```

<br>

### editable

	- False일 때 해당 필드는 관리자페이지, 모델폼에 표시되지 않는다.
	- 또, False일 때 모델 유효성검사도 넘어간다.
	- 기본값은 True이다.

<br>

### error_messages

	- 해당 필드에서 발생하는 기본 메세지를 원하는 메세지로 덮어쓸 수 있다. 
	- 덮어 쓰려는 오류 메시지와 일치하는 키로 딕셔너리를 만들면 된다.
	- 에러메세지 키는 null, blank, invalid, invalid_choice, unique, uniques_for_date 등을 넣을 수 있다.
	
<br>

### help_text

	- 필드가 폼위젯으로 표시될 때 함께 표시하는 도움말을 설정할 수 있다.
	- 해당 모델을 폼을 쓰지 않더라도 모델을 문서화하는 데 도움이 된다.
	- help_text 안에 HTML양식을 사용할 수 있다.

```python
help_text = "Follow this format : <em>YYYY-MM-DD</em>."
```

또, 이 방법 대신에 일반 텍스트와 `django.utils.html.escape()`를 사용하여 HTML 특수문자를 이스케이프처리할 수 있다. 사이트간 스크립팅 공격을 피하기 위해 신뢰할 수 없는 사용자로부터 온 help_text는 이스케이프 처리해야한다.

<br>
	
### primary_key

	- 별도의 설정이 없으면 장고는 'id'라는 IntegerField를 모델에 자동으로 추가한다.
	- 그리고 그 필드에 'primary_key=True' 옵션이 자동으로 설정된다.
	- 디폴트 primary_key옵션을 덮어쓰고 싶을 경우에는 원하는 필드에 'primary_key=True'을 주면 된다. 
	
	- primary_key 필드는 읽기 전용이다.
	만약, primary_key가 적용된 값을 변경하고 저장하면 값이 바뀌는 게 아니라 복사가 되며, 해당데이터 다음에 새로 생긴다.
	- primary_key=True는 null=False와 unique=True를 준 것과 같다.
	- 하나의 객체에는 하나의 primarykey를 부여받기 때문이다.
	
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

<br>

### unique

	- True이면 해당 필드값은 해당 테이블 안에서 유일한 값을 가져야한다.(unique 제약)
	- 만약 unique 속성이 있는 필드를 복사하면 모델의 save() 메서드에 의해서django.db.IntegrityError(통합성에러)가 난다.
	- ManyToManyField와 OneToOneField를 제외한 필드에서 사용가능하다.
	- unique가 True이면 인덱스를 생성하므로 db_index를 정해주지 않아도 된다.
	
	
### unique_for_date

	- DateField나 DateTimeField의 이름으로 설정하여 날짜 필드의 값이 고유한 필드를 생성
	예를 들어 title이라는 필드를 만들고 unique_for_date="pub_date"를 주면 장고는 같은 필드를 생성하지 못하게 한다.
	- DateTimeField에 설정할 경우 date에만 이 옵션이 적용되고, USE_TZ=True이면 객체를 저장할 때 현재 시간대를 고려한다.
	- 해당 옵션은 모델 검증 중 Model.validate_unique()에 의해 수행되지만 데이터베이스 수준에서는  이루어지지 않는다. 모델폼에 속하지 않는 필드(예를 들어 exclude, editable=True가 적용된 필드)에 해당 옵션이 적용되면 모델 검증을 하지 않는다.
	
#### USE_TZ

	-이것이 True로 설정되면 Django는 내부적으로 시간대를 인식하는 datetime을 사용한다.
	
<br>

### unique_for_month

	- unique_for_date와 유사하나, 달에 특정하여 옵션이 적용된다.
	
<br>

### unique_for_year

	- unique_for_date와 유사하나, 년도에 특정하여 옵션이 적용된다.

<br>

### verbose_name

	- 사용자 편의에 맞게 필드명을 정할 수 있는 옵션.
	- 주어지지 않으면 장고는 필드변수명을 사용하여 _를 스페이스로 바꾼 뒤 적용한다.
	- ManyToManyField나 ForeignKey 필드는 첫 인수로 모델을 받으므로 verbose_name을 키워드 인자로 지정해줘야한다.

<br>

### validators

	- 필드에 대한 유효성 검사기 목록. ex_ 이메일, URL, 정규표현식 등등

<br>
<br>

# Field Types

### AutoField

	- 가능한 ID에 따라 자동으로 증가하는 IntegerField.
	- primary_key 필드가 자동으로 모델에 추가되므로 바로 쓸 일은 없다.

<br>

### BigAutoField

	- 64비트 정수. AutoField보다 더 많은 범위의 수를 제공한다.

<br>

### BigIntegerField

	- 64비트 정수. IntegerField와 비슷하지만 음수부터 양수까지 더 많은 범위의 수를 제공한다.
	- 해당 필드의 기본 폼 위젯은 TextInput이다
	TextInput = Renders as: <input type="text" ...>

<br>

### BinaryField

	- 이진 데이터를 저장하는 필드.
	- byte 할당만 지원하기 때문에 쿼리셋을 필터링한다거나 모델폼과 연결하는 것은 불가능하다. 
	- 해당 필드는 또한 정적파일을 처리하지 못하므로 데이터베이스에 파일을 저장하는 것은 잘못된 방법이다. 
	
<br>

### BooleanField

	- True/False를 반환하는 필드
	- Field.defalut가 주어지지 않았을 때 기본값은 None이다.
	- 기본 폼위젯은 CheckboxInput이다. 
	- null 값을 넣고 싶다면 NullBooleanField를 사용한다.

<br>

### CharField

	- 작은 ~ 큰 범위를 포괄하는 문자열 필드.
	- 매우 큰 문자열은 TextField를 사용한다.
	- 기본 폼위젯은 TextInput이다.
	- 데이터베이스와 장고 유효성 검증에 필요하므로 max_length를 반드시 써줘야 한다. 

<br>

### DateField

Python에서 datetime.date 인스턴스로 표현되는 날짜.

`+옵션`  `DateField.auto_now`

```python
modified_date = DateField(auto_now=True)
```

DateField의 옵션으로, True 개체이면 저장(save())될 때마다 현재 시간을 업데이트한다. 

"마지막으로 수정된" 타임 스탬프에 유용해서, 주로 수정일 필드에 사용되는 옵션이다. 

해당 필드는 원하는 값으로 수정할 때 사용할 수는 없고 단순히 수정일을 지금 현재의 시간으로 업데이트할 때만 사용된다. 

**또, 쿼리셋에서 해당 필드 값에 원하는 값을 재입력하여 수정하고 싶을 때는 auto_now 옵션을 사용해봤자 입력한 커스텀 시간이 아닌 수정된 시각이 저장되기 때문에 이 때는 `auto_now_add`를 써야 원하는 값으로 등록된다.**

이 필드는 `Model.save()`를 호출할 때 자동으로 업데이트 되며, `QuerySet.update()`로는 저장이 불가능하다. 

<br>

`+옵션` `DateField.auto_now_add`

```python
created_date = DateField(auto_now_add=True)
```

객체를 생성할 때 자동으로 필드의 시간을 현재로 설정한다. 이는 타임 스탬프 생성에 매우 유용하다.

현재 날짜는 항상 사용된다. 재정의할 수있는 기본값이 아니기 때문에 객체를 생성할 때 이 필드의 값을 설정하더라도 무시된다.

**또, 쿼리셋에서 해당 필드 값에 원하는 값을 재입력하여 수정하고싶을 때는 auto_now_add 옵션을 사용해야 원하는 값으로 등록된다.**

이 필드를 수정하려면 `auto_now_add=True` 대신 다음과 같이 설정하면 된다.

```python
# DateField일 때 
created_date = models.DateField(default=date.today)

# DateTimeField일 때
created_date = models.DateTimeField(default=timezone.now)
```

auto_now_add, auto_now 및 default 옵션은 상호 배타적이다.(함께 쓰일 수 없다) 이러한 옵션을 조합하면 오류가 발생합니다.

##### 참고 

	현재 구현된 것처럼 auto_now 또는 auto_now_add를 True로 설정하면 해당 필드는 editable = False 및 blank = True로 설정된다.
	즉, 반드시 모델에 등록되고, 빈 값을 입력할 수 있다.
	
<br>

#### DateTimeField

Python에서 datetime.datetime 인스턴스로 표현되는 날짜와 시간을 입력하는 필드

DateField와 동일한 추가 인수를 사용하며, 이 필드의 기본 폼위젯은 단일 `extInput`이다.

<br>

### DecimalField

	- 고정 소수점 이하의 십진수를 파이썬에서 Decimal 인스턴스로 나타낸다. 
	- 2개의 필수 인수가 있다.
	- 기본 폼위젯은 localize=False일 때 NumberInput, 아닐 때 TextInput이다.

`+옵션` `DecimalField.max_digits`

	숫자에 사용되는 최대 자릿수를 정할 수 있다. 
	`decimal_places`보다 크거나 같아야 한다.
 
`+옵션` `DecimalField.max_places`
	
	숫자와 함께 저장할 소수 자릿수를 정할 수 있다.
	999까지의 수를 소수점 2째자리 수까지 저장하려면 다음과 같이 사용한다.
	
```python
models.DecimalField(..., max_digits=5, decimal_places=2)
```

#### DecimalField와 FloatField의 차이

DecimalField는 파이썬의 Decimal 타입으로 숫자를 나타내고 FloatField는 파이썬의 float 타입을 사용하여 나타낸다. 따라서 보이는 형태는 같지만, 그 타입을 다르게 쓰는데 차이가 있다.
	
<br>

### FloatField

	- 파이썬의 float 인스턴스로 표시되는 부동소수점 숫자.
	- 기본 폼위젯은 NumberInput이며, localize=False일 때는 TextInput이다.
	(DecimalField와 반대)

<br>

### DurationField

	- 시간연산에 사용되는 timedelta 파이썬 내장함수를 사용하여 연산한 시간주기를 저장하는 필드
	- DurationField를 사용한 산술은 대부분의 경우에 작동하지만 DateTimeField의 산술인스턴스와 비교하는 것은 작동하지 않는다.

> Timedelta가 Python으로 모델링 한 시간주기 저장 필드. PostgreSQL에서 사용되는 데이터 유형은 간격이며 Oracle에서는 데이터 유형이 INTERVAL DAY (9) TO SECOND (6)입니다. 그렇지 않으면 마이크로 초의 bigint가 사용됩니다.

<br>

### EmailField

	- 유효한 전자메일 주소인지 확인하는 CharField.
	- EmailValidator를 사용하여 입력 유효성을 검사함.

<br>

### ImageField

```python
class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
```

	- FileField로부터 속성과 메서드뿐만 아니라 업로드된 객체가 유효한 이미지파일인지 확인하는 유효성 검사도 상속받는다.
	- 데이터베이스에는 varchar로 기본 길이가 100인 열을 생성한다. (길이 오버라이드 가능)
	- 기본 폼위젯은 ClearableFileInput이다.
	- 사용하기 위해서는 Pillow 라이브러리가 필요하다. 
	- FileField와 동일하게 ImageField도 높이(height)와 width(너비) 옵션을 정할 수 있다.
	- 아래 두 필드 옵션을 사용한다.

`+옵션` `ImageField.height_field`

모델 인스턴스가 저장될 때마다 자동으로 이미지 높이값이 채워지는 모델필드.

`+옵션` `ImageField.width_field`

모델 인스턴스가 저장될 때마다 자동으로 이미지 너비값이 채워지는 모델필드.

<br>

### IntegerField

	- 음수 -2147483648 에서 2147483647 까지는 장고에 의해 데이터베이스에 안전하게 저장된다.
	- 기본 폼위젯은 localize=False일 때 NumberInput이고, True이면 TextInput이다.
	
<br>

### GenericIPAddressField

	- class GenericIPAddressField(protocol=’both’, unpack_ipv4=False, **options)

	
`+옵션` `GenericIPAddressField.protocol`

지정된 프로토콜에 대한 유효한 입력을 제한한다. 

허용되는 값은 'both'(기본값), 'IPv4'또는 'IPv6' 

대소문자를 구분하지 않아도 일치하는 값을 찾는다.

`+옵션` `GenericIPAddressField.unpack_ipv4`

`::ffff:192.0.2.1`과 같은 IPv4 매핑된 주소의 압축을 푼다. 이 옵션을 사용하면 주소가 `192.0.2.1`로 압축 해제된다.

기본값은 사용하지 않는다. 프로토콜이 'both'로 설정된 경우에만 사용할 수 있다.

<br>

### NullBooleanField

	- BooleanField와 비슷하지만 옵션으로 Null값을 지원한다.
	- BooleanField에 null=True를 사용하는 대신 해당 필드를 사용한다.
	- 기본 폼위젯은 NullBooleanSelect이다.

<br>

### PositiveIntegerField

 	- IntegerField와 비슷하지만 양수이거나 0인 값만 들어갈 수 있다.
 	- 즉, 0 에서 2147483647까지의 숫자는 장고에 의해 안전하게 저장된다.
 	- 0은 이전 버전과 호환성을 위해 허용한 값이다.

<br>

### PositiveSmallIntegerField

	- 데이터베이스 종류에 따라 정한 일정한 범위의 양수까지만 저장되는 필드이다.
	- 즉, 0 에서 32767까지의 숫자는 장고에 의해 안전하게 저장된다.

<br>

### SlugField

	- class SlugField(max_length=50, **options)
	- Slug는 신문에서 사용하던 짧은 색인 개념으로 문자, 숫자, 언더스코어와 하이픈만 사용한다.
	- slug는 보통 URL에 사용되며, Field.db_index가 True로 저장되어 있다.
	- max_length가 필수 옵션으로 사용된다. max_length를 정해 주지 않으면 장고는 50으로 정해버린다.
	- 다른 값의 값을 기반으로 SlugField를 자동으로 미리 채울 수 있다. 	prepopulated_fields를 사용하여 관리자가 자동으로 이 작업을 수행할 수 있다.

<br>

### SmallIntegerField

	- IntegerField와 같지만 데이터베이스에 따라 -32768 에서 32767까지의 데이터를 장고가 안전하게 저장하는 필드이다.

<br>

### TextField

	- 큰 범위의 텍스트를 저장하는 필드이다.
	- max_length 옵션을 설정하면 자동생성 폼 필드의 Textarea 위젯에 반영된다.
	그러나 모델, 데이터베이스 레벨에서 강제된 조항은 아니므로 CharField를 대신 사용할 수 있다.
<br>

### TimeField

	- class TimeField(auto_now=False, auto_now_add=False, **options)
	- 파이썬의 datetime.time 인스턴스를 통해 보여지는 시간 입력 필드.
	- DateField의 자동 생성 옵션을 사용할 수 있다.(auto_now, auto_now_add)
	- 기본 폼위젯은 Textinput이다.

<br>

### URLField

	- class URLField(max_length=200, **options)
	- URL을 위한 CharField이다.
	- 기본 폼위젯은 Textinput이다.
	- 모든 CharField의 서브클래스처럼, URLField도 max_length를 사용할 수 있고, 만약 주어지지 않으면 장고가 200으로 설정한다.

<br>

### UUIDField

	- 보편적으로 유일한 식별자를 저장하기 위한 필드로 파이썬의 UUID 클래스를 사용한다.
	- PostgreSQL에서 사용되면 uuid 데이터 유형에 저장되고, 그렇지 않으면 char (32)에 저장된다.
	- 범용 고유 식별자는 primary_key에 대한 AutoField 대신 사용할 수 있는 좋은 방법이다. 
	- 데이터베이스에서 UUID를 생성하지 않으므로 기본값을 사용하는 것이 좋습니다.

```python
# 사용 예시
import uuid
from django.db import models

class MyUUIDModel(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
		)
```

<br>

# Relationship Fields

### ForeignKey

	- class ForeignKey(othermodel,on_delete, **options)
	- 다대일 관계에서 관계있는 모델을 연결하기 위해 위치인자가 필요하다.
	- 객체가 자기 자신과 다대일 관계를 가지는 경우(재귀적 관계) 
	models.ForeignKey('self', on_delete=models.CASCADE) 를 사용
	- 아직 정의되지 않은 모델과의 관계를 형성하는 경우에도 그 모델의 이름을 스트링으로 변환하여 사용 가능하다.

```python
from django.db import models

class Car(models.Model):
	manufacturer = models.ForeignKey(
		'Manufacturer',
		# Car에서는 Manufacturer모델이 아래에 있으므로 아직 정의되지 않은 모델이다.
		# 이 경우 스트링으로 관계지을 모델명을 써준다.
		on_delete=models.CASCADE,
		)
		# ...
	
class Manufacturer(models.Model):
	pass  
```

추상 모델에서 해당 관계가 정의된 경우에는 모델이 구체적인 모델의 서브클래스이고 추상모델의 app_label과 관련없는 경우 사용가능.

```python
# products/models.py
from django.db import models

class AbstractCar(models.Model):
	manufacturer = models.ForeignKey(
		'Manufacturer',
		on_delete=models.CASCADE
		)
		
		class Meta:
			abstract = True
```

```python
# production/models.py
from django.db import models
from products.models import AbstractCar

class Manufacturer(models.Model):
	pass
	
class Car(AbstractCar):
	pass
	
# Car.manufacturer는 production.Manufacturer를 가리킬 것이다.
```
다른 앱에 정의된 모델을 참조할 경우 전체 앱라벨을 명시해주어 어디서 불러오는지 알려준다. 

```python
class Car(models.Model):
	manufacturer = models.ForeignKey(
		'production.Manufacturer',
		on_delete=models.CASCADE,
		)
```

데이터베이스의 색인(index)은 ForeignKey에 자동으로 생성된다. 이를 끄는 방법은 `db_index=False`를 옵션으로 주는 것이다. join을 위해서라기보다 일관성을 위해서, 또는 대체 인덱스를 생성하기 위해서 ForeignKey를 넣는다면 `db_index=False`를 설정한다.

<br>

#### Database Representation

장고는 데이터베이스 컬럼이름을 처리할 때 필드명에 `_id`를 붙인다. 예를 들어 위의 Car모델은 데이터베이스에서 `manufacturer_id` 컬럼을 생성할 것이다. 이를 커스터마이징하고 싶다면 `db_column='<원하는 필드명>'`으로 주면 된다. 

만약 커스텀 SQL문을 작성하는 것이 아니라면 필드명으로 컬럼명을 작성하게 놔두는 것이 좋다.
 
<br>

#### ForeignKey 필드의 사용가능한 인자

`+옵션` `ForeignKey.on_delete`

ForeignKey로 참조된 객체가 삭제되면 장고는 on_delete 인자에 명시해준 SQL 제약조건을 모방한다. 예를 들어, nullable ForeignKey가 있고 참조된 객체가 지워질 때 null값으로 표시되게 하고 싶다면 다음과 같이 on_delete값을 준다.

**on_delete 인자는 장고 2.0에서 필수인자로 사용될 예정. 기본값은 CASCADE**

```python
user = models.ForeignKey(
	User,
	models.SET_NULL,
	blank=True,
	null=True,
	)
```

**CASCADE**
	
	- ForeignKey로 참조한 객체를 지우면 ForeignKey를 보유하고 있는 객체도 모두 지워진다.

**PROTECT**

	- 장고에서 ProtectedError를 일으켜 참조된 객체로부터 ForeignKey 필드가 지워지는 것을 방지한다.

**SET_NULL**
	
	- 삭제시 ForeignKey를 null로 바꿔준다.
	- 이는 반드시 null=True 옵션과 함께 사용한다.
	
**SET_DEFAULT**
	
	- ForeignKey를 기본값으로 설정한다.
	- ForeignKey에 default 옵션이 설정되어 있어야 한다.

**SET()**

	- ForeignKey를 SET()으로 전달한 값이 반환된다.
	- SET()의 매개변수가 함수인 경우 함수를 호출한 결과가 반환된다.
	- 대부분의 경우 models.py를 불러올 때 쿼리를 실행하지 않으려면 함수를 전달한다.
	
```python
from django.conf import settings
from django.contrib.auth import get_user_model
from django_db import models

def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]
	
class MyModel(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET(get_sentinel_user)
		)
```

**DO_NOTHING**

	- 어떠한 행위도 실행하지 않는다. 
	- 데이터베이스 백엔드가 참조 무결성(값이 유일해야함)을 적용할 때 데이터베이스 필드에 SQL ON DELETE 제약 조건을 수동으로 추가하지 않으면 IntegrityError가 발생한다.

<br>

`+옵션` `limit_choices_to`

	- 필드가 모델폼이나 어드민페이지를 사용하는 경우 필드에 입력가능한 선택항목을 줄 때 사용한다.
	- 딕셔너리, Q오브젝트나 호출가능한 딕셔너리, Q 객체가 사용될 수 있다.
	
```python
staff_member = models.ForeignKey(
	User,
	on_delete = models.CASCADE,
	limit_choices_to = {'is_staff': True},
)
```
위와 같이 설정하면 모델폼이나 어드민에서 Users 중에 `is_staff=True`인 row의 리스트만 가져오게 된다. 

함수형태의 폼도 유용하게 사용될 수 있다. 예를 들어 파이썬의 `datetime` 모듈을 사용하면 날짜 범위를 제한하여 그 기준을 만족하는 row만 가져올 수도 있다.

```python
def limit_pub_date_choices():
	return {'pub_date__lte': datetime.date.utcnow()}

limit_choices_to = limit_pub_date_choices
```

limit_choices_to가 Q 오브젝트를 반환하는 경우에는 좀더 복잡한 옵션을 적용할 수도 있다.

<br>

`+옵션` `ForeignKey.related_name`

	- 관련된 객체로부터 해당 객체의 관계에 사용하는 이름.
	- related_query_name의 기본값이기도 하다.
	- 추상모델에 다대일 관계를 정의할 때 해당 값을 정의하면 사용자 지정명을 사용하여 구문을 만들 수 있다.
	- 장고가 역방향 참조 관계를 생성하지 않게 하려면 related_name='+' 옵션을 지정한다.
	
```python
user = models.ForeignKey(
	User,
	on_delete=models.CASCADE,
	related_name='+',
)
```

<br>

`+옵션` `ForeignKey.related_query_name`

	- 대상 모델에서 역방향 필터링에 사용할 이름.
	- 설정된 경우 related_name, default_related_name이 기본값으로 설정된다.
	- 설정되지 않은 경우 기본값은 모델명으로 설정된다. 

```python
class Tag(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag_example",
    )
    name = models.CharField(max_length=255)

# 역필터링에 사용하는 이름이 tag로 바뀌었다.
Article.objects.filter(tag_example__name='important')
```

이외에도 앱라벨이름과 클래스명을 조합한 동적인 이름을 부여할 수도 있다.

```python
related_name="%(app_label)s_%(class)s_related",
related_query_name="%(app_label)s_%(class)ss",
```

<br>

`+옵션` `ForeignKey.to_field`

	- 관계가되는 관련객체의 필드를 지정할 수 있다.
	- 기본적으로 Django는 관련 객체의 primary_key를 사용한다. 
	- 다른 필드를 참조하는 경우 해당 필드는 unique=True이다.

<br>

`+옵션` `ForeignKey.db_constraint`

	- 데이터베이스에서 foreign key에 대한 제약조건을 걸지 말지 정하는 옵션
	- 대부분의 경우 True로 지정하며, False로 지정할 경우 관련 객체가 없을 때 DoesNotExist 예외를 발생시킨다. 

<br>

### ManyToManyField

	- class ManyToManyField(othermodel, **options)
	- ForeignKey 와 동일하게 어떤 모델과 연결될 것인지를 알려주는 위치인자를 가진다.
	- 관계된 객체가 RelatedManager를 통해 추가, 삭제, 생성될 수 있다. 

`+옵션` `ManyToManyField.symmetrical`

자기자신과의 다대다관계를 정의할 때만 사용된다.

```python
from django.db import models

class Person(models.Model):
	friends = models.ManyToManyField("self")
```

장고가 Person모델을 처리할 때 다대다필드를 식별하고 person_set 속성을 추가하지 않는다. 대신 다대다필드는 대칭이므로 정방향 참조를 사용하도록 한다.

자기자신은 참조하고 싶지 않다면 `symmetrical=False` 옵션을 준다. 

<br>

`+옵션` `ManyToManyField.through`

장고는 다대다필드의 관계를 정의하는 테이블을 자동으로 생성한다. 그러나 중간자 모델을 직접 정의해줄 경우에는 `through` 옵션을 통해 어떤 모델이 중간자 모델로 기능할 것인지 알려줘야 한다.

중간자 모델은 2개 모델의 다대다 관계에서 추가적으로 필드를 생성하고 싶은 경우 정의해준다.

through 모델을 정의해주지 않은 경우에도 through 모델 클래스는 존재하며, 이를 통해 자동으로 다대다 테이블이 생성된다.

소스모델과 타겟모델이 다를 경우 다음이 생성된다. 

	id : 관계의 primary_key를 자동으로 생성
	<포함하는모델>_id : 다대다필드가 정의된 모델의 테이블 데이터가 가지고 있는 id
	<다른 모델>_id : 다대다필드가 가리키고 있는 모델의 데이터 id
	
다대다필드가 같은 모델을 가리킬 경우(재귀, 자기자신의 다대다필드 설정) 다음이 생성된다.

	id : 관계의 primary_key를 자동으로 생성
	from_<모델명>_id : 소스모델을 가리키는 인스턴스의 id
	to_<모델명>_id : 관계가 가리키는 인스턴스의 id (타겟모델의 인스턴스)
	
해당 클래스(테이블)는 일반 모델처럼 주어진 모델 인스턴스에 대해 쿼리 관련 레코드로 사용할 수 있다.

<br>

`+옵션` `ManyToManyField.through_fields`

직접 정의한 중간자 모델이 있을 경우 사용한다. 장고는 보통 중간자 모델에서 다대다필드 관계를 성립시키기 위해 필드를 자동으로 찾는다. 그러나 복수의 ForeignKey를 선언한 중간자 모델에서는 어떤 필드를 다대다필드 관계로 정해줄 지 찾지 못하므로 다대다 필드를 정의한 모델에 직접 정의해준다.

```python
from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=50)
	
class Group(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(
		Person,
		through='Membership',
		through_fields=('group', 'person'),
	)
	
class Membership(models.Model):
	group=models.ForeignKey(Group, on_delete=models.CASCADE)
	person=models.ForeignKey(Person, on_delete=models.CASCADE)
	inviter=models.ForeignKey(
		Person,
		on_delete=models.CASCADE,
		related_name="membership_invites",
	)
	invite_reason=models.CharField(max_length=64)
```

Membership 모델에는 Person 모델과 연결된 ForeignKey필드가 2개 있기 때문에 `through_fields` 옵션을 통하여 ForeignKey 필드를 명시적으로 지정해준다. 이는 재귀적인 관계에서도 중간자 모델에 외래키가 여러 개일 경우 반드시 지정해줘야 한다.

`through_fields`에는 2-튜플 ('field1', 'field2')를 허용한다. 
	
	- field1은 다대다필드가 정의된 모델의 외래키 이름이다.
	- field2는 타겟 모델의 외래키의 이름이다.
	- 중간 모델을 사용하는 재귀 관계는 항상 nonsymmetrical로 정의된다. 즉, symmetrical=False로 정의되므로 "원본"과 "대상"이라는 개념이 있다. 이 경우 'field1'은 관계의 '소스'로 취급되고 'field2'는 '타겟'으로 취급된다.

<br>

`+옵션` `ManyToManyField.db_table`

	- 다대다 데이터를 저장하기 위해 작성할 테이블의 이름을 직접 지정할 수 있다. 
	- 정해주지 않으면 장고는 모델명과 필드명을 기반으로 이름을 만들어 쓴다.

<br>

### OneToOneField

	- class.OneToOneField(othermodel, on_delete, parent_link=False, **options)
	- 일대일 관계를 정의하는 필드로, ForeignKey와 비슷하지만 unique=True가 정의된다.
	- 역참조 하는 경우 1개의 객체만이 반환된다.(일대일모델이므로)
	- othermodel을 확장하여 다른 주제의 필드테이블을 생성하고 싶은 경우 유용하다.
	- 다대일 필드와 마찬가지로 관계를 확장할 모델명을 위치인자로 받는다.
	- 일대일필드에 related_name을 정해주지 않으면 장고는 해당 모델의 소문자이름을 사용한다.

```python
from django.conf import settings
from django.db import models

class MySpecialUser(models.Model):
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)
	supervisor = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='supervisor_of',
	)
```
User 모델은 다음과 같은 속성을 가질 것이다. 

```python
>>> user=User.objects.get(pk=1)
>>> hasattr(user, 'myspecialuser')
True
>>> hasattr(user, 'supervisor_of')
True
```

관련된 테이블에 항목이 존재하지 않을 경우 역방향 참조를 할 때 DoesNotExist 예외가 발생한다. 예를 들어 user 항목에 MySpecialUser모델에 의해 지정된 supervisor 값이 없을 경우..

일대일필드는 ForeignKey 가 가지는 모든 옵션을 수용하고 추가적으로 하나의 옵션을 더 갖는다.

`+옵션` `OneToOneField.parent_link`

	- True이고 비추상모델로부터 상속받은 경우 해당 필드는 부모 클래스로의 링크로 사용된다.
	- 일반적으로는 서브클래싱에 의해 암묵적으로 OneToOneField가 생성되지만 이 옵션을 사용하면 부모클래스로의 링크로써 작동한다.

<br>
