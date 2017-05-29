###### 20170529 [알고리즘 문제풀이]

#### level1

## x만큼 간격이 있는 n개의 숫자

number_generator함수는 x와 n을 입력 받습니다.
2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.
[2,4,6,8,10]

4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.
[4,8,12]

이를 일반화 하면 x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트를 리턴하도록 함수 number_generator를 완성하면 됩니다.

**내 코드**

~~~python
def number_generator(x, n):
    return [i for i in range(x, x*n+1, x)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(3,5))
~~~

<br>

**다른 사람 코드**

~~~python
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))
~~~


<br>

#### level2

## 핸드폰번호 가리기

별이는 헬로월드텔레콤에서 고지서를 보내는 일을 하고 있습니다. 개인정보 보호를 위해 고객들의 전화번호는 맨 뒷자리 4자리를 제외한 나머지를 "*"으로 바꿔야 합니다.

전화번호를 문자열 s로 입력받는 hide_numbers함수를 완성해 별이를 도와주세요.

예를 들어 s가 `"01033334444"`면 `"*******4444"`를 리턴하고, `"027778888"`인 경우는 `"*****8888"`을 리턴하면 됩니다.

**내 코드**

~~~python
def hide_numbers(s):
    s_list = list(s)
    s_list[:-4] = "*" * (len(s_list)- 4)
    s = "".join(s_list)
    return s

    #함수를 완성해 별이를 도와주세요

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
~~~

<br>

**다른 사람 코드**

- 한 줄로 작성한 코드

~~~python
def hide_numbers(s):
    #함수를 완성해 별이를 도와주세요
    return "*"*(len(s)-4) + s[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
~~~

<br>

**다른 사람 코드**

- 정규표현식을 사용하여 컴파일한 후 sub()함수로 문자를 바꿈. 

~~~python
import re

def hide_numbers(s):
    p = re.compile(r'\d(?=\d{4})')
    return p.sub("*", s, count = 0)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
print("결과 : " + hide_numbers('027778888'));
~~~

