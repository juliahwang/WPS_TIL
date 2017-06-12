#### 예제코드

~~~
class Car:
	def __init__(self, name, price):
		self.name = name
		self._price = price
~~~

<br>
### 프라이빗 지정자

`print(a._Car__price)`

> 프라이빗 지정자도 출력할 수 있다.

~~~
@property
def price(self):
    return self.__price

# 읽기전용이 된다.
~~~

<br>

@property를 사용하는 경우

1. 프라이빗 지정자의 값에 접근하고자 할 때 사용
2. ==속성처럼 접근 가능==
ex_ print(a.price)



~~~
@price.setter
def price(self, new_price):
    self.__price = new_price
~~~

<br>

### 프로텍티드 지정자

- 상속을 받을 때 같은 속성을 사용할 때 사용

~~~
class Kia:
    __init__(self, name, price, speed):
    	super().__init__(self, name, price)
    	self.speed = speed
~~~