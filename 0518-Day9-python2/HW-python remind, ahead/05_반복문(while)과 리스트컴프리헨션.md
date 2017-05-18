###### 20170518 - [python basic]

## 05_ 반복문 /리스트 컴프리헨션 

#### wps 수업노트 [github 수업자료][1]
[1]:https://github.com/Fastcampus-WPS-5th/Python/blob/master/08.%20%EC%A0%9C%EC%96%B4%EB%AC%B8.md

~~~
while 조건:
	조건이 참이면 실행
	거짓이면 계속 반복
~~~

- 파이썬의 공백과 탭은 섞어쓰지 않는다.
- 탭은 4칸

<br>

## 2. 컴프리핸션 (comprehension)

=함축, 내포

- iterable
- 튜플은 컴프리헨션이 없다.

~~~python
# for문과 range 사용
numbers = []
for item in range(1, 6):
    numbers.append(item)
numbers
# [1, 2, 3, 4, 5]

# 리스트 컴프리헨션 사용
numbers = [x for x in range(1, 6)]
numbers
# [1, 2, 3, 4, 5]
~~~

<br>

#### format 함수와 print문의 차이

~~~
print((x, y)) : 튜플 타입
'({}, {})'.format(x, y) : str 타입
~~~


#### 리스트 컴프리헨션 실습

~~~python
# 실습 
# 구구단 리스트를 만들고 단이 바뀔 때마다 줄바꿈하라.  
l = ['{} * {} = {}'.format(x, y, x*y if y != 9 else '{}\n'.format(x*y)) for x in range(1, 10) for y in range(1, 10)]

or 

l = ['{} * {} = {}'.format(x, y, x*y if y != 9 else str(x*y) + '\n') for x in range(1, 10) for y in range(1, 10)]

# 실습 2
# 1~6까지 리스트를 만들고 각 item의 2배의 값을 할당하고 싶다면?
double_item = [item * 2 for item in range(1, 6)] 

# 실습 3
# 1~5중 짝수만 해당하는 리스트를 만들고 싶다면?
even_item = [item for item in range(1, 6) if item % 2 == 0]
even_item
~~~


<br>

#### 리스트 컴프리헨션 [ 중첩  ]

~~~python
# 실습 1
# for문을 2개 중첩하여 (0,0), (0,1), (0,2), (0,3), (1,0), (1,1)..... (6,3)까지 출력되는 반복문을 구현한다.

# for문
for x in range(0, 7):
    for y in range(0, 4):
        print((x, y))

# list-comprehension
aa = [(x, y) for x in range(0, 7) for y in range(0, 4)]
~~~

<br>

#### 리스트 안의 요소는 for문으로 출력

~~~python
for items in l:
	print(items)
~~~

~~~python
# 실습 6 
l2 = [x for x in range(100) if x % 7 == 0 or x % 9 == 0]

l2 = [x for x in range(100) if not x % 7 or not x % 9]

# if not x % 7 or not x % 9
# `x % 7 == 0` 는 `x % 7 == False`
# not x % 7  = x % 7 이 False이면
~~~

<br>

#### not 은 거짓인지 검사.

- 0은 bool 값이 False이므로 not 0은 bool값이 True
- False 값을 가지는 요소는 0, None, 빈 시퀀스 타입과 딕셔너리, 셋 등이 있다.

요소 | False
:---:|:---:
null | None
정수 0 | 0
부동소수점 수 | 0.0
빈 문자열 | ''
빈 리스트 | []
빈 튜플 | ()
빈 딕셔너리 | {}
빈 셋 | set()

<br>

#### 셋 컴프리헨션

~~~python
aa = {a for a in range(1, 100) if a % 2 == 0}
~~~

<br>

#### 제네레이터 컴프리헨션

~~~python
a = (x for x in range(100))
a
# <generator object <genexpr> at 0x111cb8468>
# 괄호로 되어있으나 튜플을 생성하지 않는다.
# 튜플은 컴프리헨션이 없다.
# 순회가능한 제너레이터 객체를 생성하며 리스트형태로도 만들 수 있다.

list(a)
# 리스트로 만들어 출력가능하다.
# range, zip함수와 같이 한번 데이터가 출력되면 다음에 중복으로 출력할 수 없다.
# 05_ 제어문-조건문, 반복문.md 참고! 
~~~

