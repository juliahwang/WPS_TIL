###### 20170523 - [11.class]

## 상속

- 객체지향 프로그래밍에서는 클래스에 상속 기능을 지원한다.
- 다른 클래스에 이미 구현된 메서드나 속성을 상속받은 클래스에서 그대로 사용가능하다.
- 부모 클래스의 능력은 그대로 전달받는 것과 같다.


#### 상속받는 법

- 상속받은 클래스 옆에 괄호로 상속받고자 하는 클래스의 이름 지정

~~~pyhton
class Parent:  # 부모클래스
    def can_sing(self):
        print("Sing a song")


class LuckyChild(Parent):  # 상속 사용
    pass


class UnluckyChild:  # 상속 안한 클래스
    pass


class LuckyChild2(Parent):  # 상속도 받고, 자기 메소드도 있는 클래스
    def can_dance(self):
        print("Suffle Dance")


print('=======실행문=======')
father = Parent()
father.can_sing()  # Sing a song
print('===================')

child1 = LuckyChild()
child1.can_sing()  # Sing a song
"""부모 클래스를 상속받은 LuckyChild 클래스로 인스턴스를 생성했고 생성된 인스턴스는 can_sing()함수를 사용할 수 있다"""
print('===================')

child2 = UnluckyChild()
#child2.can_sing()  # AttributeError: 'UnluckyChild' object has no attribute 'can_sing'
print('===================')

child3 = LuckyChild2()
child3.can_sing()  # Sing a song
child3.can_dance() # Shuffle Dance 
print('===================')
~~~

<br>

#### 상속하는 이유 

- 코드 중복을 피할 수 있다.

<br>
<br>
## 메서드 오버라이딩

- 상속받을 대상인 클래스의 메서드와 이름은 같지만 그 행동을 다르게 해야할 때.
- 아래 김씨 클래스는 박씨 클래스를 상속받았지만 travel 메서드를 이름만 같고 다른 기능을 하는 함수로 선언하여 메서드 오버라이딩을 하였다. 

~~~python 
class HousePark:
	lastname = '박'
	def __init__(self, name):
		self.fullname = self.lastname + name
	def travel(self, where):
		print('{}, {}여행을 가다.'.format(self.fullname, where))


class HouseKim(HousePark):
	lastname = "김"
	def travel(self, where, day):
		print('{}, {}여행 {}일 가네'.format(self.fullname, where, day))
~~~

<br>

## 연산자 오버로딩

- 연산자( `+, -, *, /,...`)를 객체끼리 사용할 수 있게 하는 기법

~~~python 
class HousePark:
	lastname = '박'
	def __init__(self, name):
		self.fullname = self.lastname + name
	def travel(self, where):
		print('{}, {}여행을 가다.'.format(self.fullname, where))
	def __add__(self, other):
		print('{}, {} 결혼했네'.format(self.fullname, other.fullname))


class HouseKim(HousePark):
	lastname = "김"
	def travel(self, where, day):
		print('{}, {}여행 {}일 가네'.format(self.fullname, where, day))
		
		
# -----실행문------
pey = HousePark("로미오")
key = HouseKim("줄리엣")
pey + key

## 결과
# 박응용, 김줄리엣 결혼했네
~~~


##### (1) 다른 연산자들

~~~python
def __add__(self):  # 더하기 연산자
	pass
	
def __sub__(self):  # 빼기 연산자
	pass
	
def __mul__(self):  # 곱하기 연산자
	pass
	
def __truediv(self):  # 나누기 연산자
	pass 
~~~