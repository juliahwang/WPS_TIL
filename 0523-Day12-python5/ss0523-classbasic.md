###### 20170523 - [11.class]

## 객체, 클래스의 개념

#### 클래스 

- 모양을 찍어낼 수 있는 틀 
- class는 연관된 변수와 함수를 모아서 패키징한 그릇이다.
- class를 복제해서 instance를 만든다.
- instance마다 실제 저장되어 있는 데이터의 값이 다르고, 값에 따라 동작이 달라진다.

<br>

#### 객체 = 클래스의 인스턴스 

- 인스턴스는 객체와 같은 의미
- 클래스의 의해 만들어진 객체를 인스턴스라고 한다.
- 클래스가 모양자라면 인스턴스는 모양자 대고 그린 그림.
- 클래스를 통해서 인스턴스를 무한정으로 만들어낼 수 있다.

<br>

#### 클래스 변수 

- 클래스의 네임스페이스에 선언된 변수이다.
- 변수, 필드, 상태라고도 하며 값을 지정하는 데 사용한다.
- 여러 인스턴스가 공유할 변수이다.

<br>

#### 인스턴스 변수 

- 인스턴스 변수는 self가 붙는 변수이다.
- 생성한 각각의 인스턴스가 가지고 있는 고유한 데이터값이다.


##### 클래스 변수와 인스턴스 변수 이해

![variables_classandinstance]() 

~~~python
class Account:
    """계좌 개설, 삭제하기"""
    num_accounts = 0   # 클래스 변수, 클래스의 네임스페이스에 위치
    def __init__(self, name):
        self.name = name    # 인스턴스 변수, 인스턴스의 네임스페이스에 위치
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1


kim = Account("kim")   # 인스턴스 생성
lee = Account('lee')

print('=============')
print(kim.name) # 'kim'
print(lee.name) # 'lee', 인스턴스 변수 호출

print('=============')
print(kim.num_accounts) # 2
print(lee.num_accounts) # 2, 클래스 변수 호출

print('=============')
print(Account.num_accounts)  # 2, 여러 인스턴스 간 공유해야 하는 값은 클래스 변수를 통해 바인딩

"""
파이썬은 인스턴스의 네임스페이스에 없는 이름은 클래스의 네임스페이스에서 찾는다
이를 통해 클래스 변수를 인스턴스에 공유한다
클래스 변수에 직접 접근할 때는 <클래스명>.<클래스변수명> 으로 찾기도 한다
"""
~~~

<br>

#### 메소드 = 클래스의 함수 

- 객체지향 프로그래밍에서는 메소드로 칭한다.
- 행위를 나타낸다.

<br>

#### 속성 = 클래스의 변수 + 함수

- 속성(attribute)은 클래스 안에 사용된 모든 변수와 함수를 일컫는다.

<br>

#### self 

- 인스턴스와 함수에 반드시 첫 매개변수로 사용해줘야 한다.

##### self가 없다면...

~~~python 
class Dog:
    name = "멍멍이"
    def cry(self):
        print(self.name + '왈왈!')


dog1 = Dog()
print('================')
dog1.cry()
print('================')
Dog.cry(dog1)

# 여기서 인스턴스 메소드인 dog1.cry()과 스테틱 메소드인 Dog.cry(dog1)은 같다.
# self가 없다면 name변수를 불러올 수 없다. 
~~~ 

