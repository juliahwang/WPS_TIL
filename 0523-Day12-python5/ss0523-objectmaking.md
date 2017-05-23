###### 20170523 - [11.class]

## 객체 생성

참고 : https://wikidocs.net/28

#### 객체와 인스턴스 

~~~python
kim = Programmer()
park = Programmer()
~~~

- 클래스에 의해 만들어진 객체를 인스턴스라고도 한다.
- 위 코드에서 kim은 객체이다.
- kim이라는 객체는 Programmer클래스의 인스턴스이다.
- 인스턴스는 특정객체가 어떤 클래스의 객체인지 관계위주로 설명할 때 사용한다.
- 따라서 `'kim은 객체'`라는 표현이 더 어울린다.
- 또, `kim은 Programmer의 인스턴스`라고 표현한다.

<br>

#### 클래스 변수 

~~~python 
class Service:
	secret = "영구는 배꼽이 2개다"
~~~

##### (1) class Service의 인스턴스 생성

~~~python
pay = Service()
~~~


##### (2) 객체로 클래스 변수 사용하기

~~~python
pey.secret
# "영구는 배꼽이 2개다."
~~~

- <객체>.<클래스변수>
- 객체 간 서로 공유하는 변수를 클래스 변수라 한다.
- 따라서 Service의 모든 인스턴스들은 클래스변수를 사용할 수 있다.

~~~python 
Service.secret = "영구는 배꼽이 없다."
print(pey.secret)
# '영구는 배꼽이 없다.'
~~~

- 클래스에서 클래스 변수의 값을 바꾸면 모든 인스턴스들이 바뀐 값의 클래스 변수를 반환한다.

<br>

#### 클래스 함수

~~~python
class Service:
	secret = "영구는 배꼽 2개".  # 클래스 변수
	def sum(self, a, b):    # 더하기 메소드
		result = a + b
		print('{} + {} = {}입니다.'.format(a, b, result))
~~~

##### (1) 클래스 Service의 인스턴스 생성 

- 먼저 객체를 생성한 후,
- 클래스 함수를 사용한다.

~~~
pey = Service()
pey.sum(1, 1)
~~~


#### Self

- class의 인스턴스들만 함수를 사용하게 하기 위해서는 반드시 self를 써준다.
- self를 쓰면 객체가 함수를 호출하여 이용할 때 따로 객체이름을 알려주지 않아도 자동으로 전달된다.

~~~python
pey.sum(pey, 1, 1) # (x)
pey.sum(1, 1). # (o)
~~~

- 함수로 메서드를 호출할 경우 self에 객체명을 써줘야한다.
- 자주 쓰는 방법은 아니다.

~~~python
FourCal.setdata(a, 4, 2)
~~~

> 위와 같이 "클래스명.메서드" 형태로 호출할 때는 객체 a를 입력 인수로 꼭 넣어 주어야 한다. 반면에 앞에서 보았듯이 "객체.메서드" 형태로 호출할 때는 첫 번째 입력 인수(self)를 반드시 생략해야 한다.

<br>

#### 객체 변수 
~~~python 
class Service:
	secret = "영구 배꼽 2개"
	def setname(self, name):
		self.name = name
	
	def sum(self, a, b):
		result = a + b 
		print('{} + {} = {}입니다'.format(a, b, result))
~~~

##### (1) 클래스 Service의 인스턴스 생성 후 이름 부여

- pey라는 객체를 생성한 후,
- setname 메서드를 이용하여 pey 객체의 이름은 "홍길동"이라는 것을 전달한다.
 
~~~python
pey = Service()   # 객체 생성 = 클래스의 인스턴스 생성
pey.setname("홍길동")   # 객체변수를 이용하여 이름 지정
pey.sum(1, 1)   # 홍길동님  1 + 1 = 2입니다. 
~~~

##### (2) 객체변수 생성 

- `객체.객체변수 = 값` 을 전달하면 객체변수를 생성한다.
- setname함수의 `self`는 pey의 이름을 "홍길동"으로 저장한다.
- 따라서 `print(pey.name)`을 실행해보면 "홍길동"이 반환된다.

~~~python 
kim.name = "홍길동"
park.name = "김가나"
~~~

<br>

#### `__init__`

- 객체를 만들 때 항상 실행되는 초기화 함수이다.

~~~python 
class Service:
	def __init__(self, name):
		self.name = name
		
	def sum(self, a, b):
		result = a + b 
		print('{} + {} = {}입니다'.format(a, b, result))
~~~

##### (1) 객체생성

- 초기화함수에서 항상 이름을 주도록 지정했으므로 아래 코드와같이 써서 객체를 생성한다. 

~~~python
pey = Service("홍길동")
pey.sum(1, 1) 
~~~