## BeautifulSoup

### 설치 

`pip install BeautifulSoup4`


### 불러오기

`from bs4 import BeautifulSoup`

### html 해석기 -lxml 설치

`pip install lxml`


### 수프 만들기

- 문서를 해석하기 위해 문서를 BeautifulSoup 구성자에 전달하는 과정.

~~~python 
soup = BeautifulSoup(<parsing할 html파일 또는 html코드 >)
tag = soup.<가져올태그>
type(tag) # class 'bs4 element.Tag'
~~~

#### 이름 가져오기

~~~python 
tag.name = 'blockquote'
tag
# <bq>kfjdskfj</bq>
~~~

#### 속성 가져오기

- 태그 내 속성의 값을 딕셔너리처럼 불러올 수 있다. 

~~~python
tag['class']
# 'comicinfo'
~~~


#### 태그 속성추가, 제거, 변경

- 마찬가지로 딕셔너리처럼 원래 태그 속성을 변경할 수 있다.

~~~python 
<div></div>

# 추가
tag['class'] = 'webtoon'
print(tag)
# <div class='webtoon'></div>

# 제거 
del tag['class']
# <div></div>

# 변경
tag['class'] = 'comicinfo'
print(tag)
# <div class='comicinfo'></div>
~~~


#### 태그 내 문자열

- 태그 내의 문자열은 `NavigableString`을 사용한다.
- 문자열 안에 태그가 포함된 경우가 있으므로  문자열은 `.contents`, `.string`, `find()` 을 지원하지 않는다.

~~~python
soup = BeautifulSoup('<p>hello?</p>', 'lxml')
print(soup.p.string)
# hello?
~~~


#### 태그 이름으로 찾기

~~~python
tag.head. # head태그만 찾기
tag.title # title 태그 찾기
tag.body.b # body 안에 b태그 찾기
soup.a # a 태그 찾기
soup.find_all('a') # a태그가 쓰인 줄 모두 찾기 
~~~


#### `.contents`

- 태그의 직속 하위 태그를 찾아 리스트로 만들어준다.
- 하나만 뽑고 싶으면 리스트의 오프셋 기능을 사용한다.

~~~python
head_tag = soup.head
head_tag.contents

<head>
	<title>hello?</title>
	<title>hello?</title>
	<title>hello?</title>
	<title>hello?</title>
</head>

# [<title>hello?</title>, <title>hello?</title>, <title>hello?</title>, <title>hello?</title>
]

head_tag.contents[0]
# <title>hello?</title>
~~~

~~~python
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# [u'The Dormouse's story']
~~~

- 리스트로 얻는 대신 `.children` 제너레이터를 사용하여 결과값만 출력할 수도 있다. 

~~~python 
for child in title_tag.children:
	print(child)
~~~

<br>

#### `.decendants`

- `.contents`와 `.children`이 태그의 직속 자식만 고려한다면 `.decendants`는 모든 자식을 리스트로 반환해주는 제너레이터이다.

~~~python
for child in head_tag.descendants:
    print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story
~~~

<br>

#### `.string`

- 태그가 1개의 자식만 가지고 NavigableString이라면 자식은 `.string`으로 꺼낼 수 있다.
- 만약 태그 안에 많은 자식태그들이 있으면 `.string`은 무얼 꺼낼 지 몰라 `None`을 반환한다. 

~~~python
title_tag.string
# u'The Dormouse's story'
~~~

- 태그의 하나밖에 없는 자식이 다른 태그이고 안에 .string이 있다면 부모태그도 .string을 자식으로 간주한다.

~~~python
head_tag.contents
# [<title>The Dormouse's story</title>]

head_tag.string
# u'The Dormouse's story'
~~~


#### `.strings`

- 태그 안에 1개 이상의 자식이 있을 때는 s를 붙여 사용하면 그대로 출력해준다. 
- 이 때 줄바꿈을 없애기 위해서는 `.stripped_strings`를 사용한다.


<br>

#### `.find_all('<찾을 태그>')`

- 다음에 만족하는 모든 타입을 반환한다.
	- 태그
	- 리스트
	- 정규표현식
	- 불린타입

	
#### `.find()`

- find_all()은 빈 리스트를 출력
- find()는 None을 출력

