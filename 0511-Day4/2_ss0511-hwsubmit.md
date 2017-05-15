
==20170508 ~ 20170511==
> ## HTML / CSS / SASS 
HTML - 웹페이지의 구조를 다룬다.
CSS - HTML의 스타일을 지정한다.
SASS - 효율적인 CSS사용을 위한 것이다.


### 1. HTML (HyperText Markup Language)
 : 마크업을 이용해 월드와이드웹(www)의 페이지를 서로 오갈 수 있는 웹문서를 만드는 언어.
 - 마크업 언어 : 태그 등을 이용하여 문서나 데이터 구조를 명기하는 언어
 - 하이퍼텍스트 : 링크를 이용해 웹페이지를 서로 연결하는 것.


### 2. 웹 표준(W3C, World Wide Web Consortium) Standards
 : 월드와이드웹 컨소시엄의 약자. 웹표준과 가이드라인 개발을 목적으로 설립

 : World Wide Web을 서술하고 정의하는 공식 표준 및 규격
   서로 다른 브라우저 및 환경에서도 같은 결과를 보여줄 수 있도록
   웹사이트를 만들 때 지켜야 하는 규격을 정해놓은 것.

 : 웹표준이 등장하기 전까지는 브라우저별로 웹페이지를 제작.

 : 웹표준에 맞는 HTML과 CSS를 지켜야 어떠한 브라우저에서도 동일한 화면이 구현됨.
 - http://html5test.com/
   웹표준 지원에 대한 브라우저 점수를 확인하는 사이트.



> ## html의 기본 구조
<!DOCTYPE html> - html5를 사용하겠다는 선언과 태그로 구성

~~~
<!DOCTYPE html> <!--DOCTYPE: 문서유형을 지정 / html: HTML5형식의미-->
<html> <!--HTML문서의 시작과 끝-->
  <head>
    <title>Document</title> <!--브라우저의 제목표시줄에 출력-->
  </head>
  <body>
    <!--문서의 본문-->
  </body>
</html> <!--태그-->
~~~

<br />
### (1) 주석 Comment
<!-- 주석-->
주석은 화면에는 표시되지 않으며, 소스에서만 확인할 수 있다.<br>
개발기간이 길고 소스가 많을 수록 작업 내용을 주석으로 정리해야 디버깅할 때 효율적이다.

~~~
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document</title>
</head>
<body>
  <!--이 사이에 넣는 내용은 주석-->
</body>
</html>
~~~

<br />
### (2) 태그의 요소(Element)와 속성(Attribute)
**href** : Hyper Reference(참조)<br>
**src** : Source(출처) <br>
태그는 가급적 _소문자_로 쓴다.

~~~
<요소 속성 = "값">
 : 값을 주는 내용이 없을 경우 스스로 닫는 태그를 쓴다.

절대경로
 : http:// 나 https:// 로 시작하는 전체 주소
<img src="http://www.google.com/images/abc.png">

상대경로
 : 해당 HTML파일을 기준으로 이미지 파일의 위치를 나타내는 방식
<img src="images/abc.png">
~~~

~~~
<요소 속성 = "값">내용</요소>
: 값을 주는 내용이 있을 경우 <열리는태그>와 </닫히는태그>를 쓴다.
<a href="http://www.naver.com">네이버 바로가기</a>
~~~

<br />
### (3) head 태그
 : 문서의 메타데이터 집합<br>
 : 웹페이지에 직접적으로 보이지 않는 정보를 브라우저에게 제공
 
~~~
예시
<head>
  웹페이지의 인코딩 방식 정의
  <meta charset="utf-8">

  IE에서 렌더링 방식을 최신으로 설정
  <meta http-equiv="X-UA-Compatible" content="ie=edge">

  css파일을 연결하는 메타태그
  <link rel="stylesheet" href="style.css">

  javascript파일을 연결하는 메타태그
  <script src="script.js" charset="utf-8"></script>

  문서의 제목을 나타냅니다.
  <title>Document</title>
</head>
~~~
 : 이외에도 다양한 meta태그가 존재한다.<br>
 : 페이스북에 링크했을 때 제목/설명/커버이미지를 보여주는 meta태그나
   검색엔진에서 주로 사용할 내용, 모바일 확대/축소여부 등 설정값을 지정할 수 있다.<br>
 : CSS나 JS파일의 링크도 head요소 내부에 link, style, script 요소로 나타낸다.

<br />
### (4) body 태그
 : 브라우저에 표시될 내용, 사용자에게 보여진다.
 
~~~
<body>
  제목태그 : <h1>패스트캠퍼스 웹프로그래밍 스쿨</h1>
  문단태그 : <p>html을 배웁니다.</p>
  인용태그 : <blockq>처음으로 작성한 HTML문서입니다.</blockq>
</body>
~~~

|제목|예제||
|---|---|---|
|하이|하이|하이|

<br />
## 요소(element)의 형태 - ==🔥블록과 인라인==
### (1) 블록 요소
 : ==줄바꿈이 일어나는 형태<br>==
 : 기본적으로 width가 전체 너비의 값을 가진다.<br>
 : 해당 요소에 배경색(background color)를 지정하면 실제로 들어있는 글자 내용과는 별개로
   전체 너비 영역만큼을 차지한다는 것을 알 수 있다.
   
~~~
<h1>블록 요소</h1>
<p>p요소는 블록형태입니다.</p>
<div>div요소도 블록형태입니다.</div>
~~~

<br />
### (2)인라인 요소
 : ==줄바꿈이 일어나지 않는 형태<br>==
 : 줄바꿈 없이 기본적으로는 자신의 내용만큼의 가로 너비를 가진다.<br>
 : 블록 요소는 인라인 요소를 포함할 수 있지만, ==인라인 요소는 블록요소를 포함할 수 없다.==
 
~~~
<strong>strong요소</strong>
<a href="">a요소</a>
<span>span요소</span>
~~~


<br />
### (3) 레이아웃 요소
 div와 span요소는 오직 block과 inline방식의 레이아웃을 구현하는 데에 사용한다.
 
~~~
<div>
  <p>블록요소 내부에 <span>인라인요소를 사용합니다.</span></p>
</div> 
~~~


<br />
<br />
<br />
20170508_2
> ## Text와 관련된 태그


### (1) 헤드라인 h1~h6
 : 중요도 순으로 개요를 나타낼 때 사용<br>
 : 학술문서나 검색엔진에서 검색 시 중요하게 사용<br>
 : 실제 크기는 CSS에서 만들고자 하는 웹페이지에 맞춰 새로 설정하므로 단계별로 구별할 제목이 있다면 hn태그를 사용.

~~~
<h1>html</h1>
<h2>역사</h2>
<h3>개발</h3>
...
<h6>최초규격</h6>
~~~

<br>
### (2) 줄바꾸기(line breaks), p와 br태그

~~~p태그 (paragraph, 문단)
<p>안녕하세요. 패스트캠퍼스입니다. 오늘은 날씨가 화창하네요
  그렇지만 미세먼지가 많으니 마스크를 꼭 착용하세요. 내일봅시다</p>
~~~


결과 : <p>안녕하세요. 패스트캠퍼스입니다. 오늘은 날씨가 화창하네요
  그렇지만 미세먼지가 많으니 마스크를 꼭 착용하세요. 내일 봅시다</p>
___
<br>

~~~
br태그 (linebreak, 줄바꾸기)
안녕하세요. 패스트캠퍼스입니다.<br>
오늘은 날씨가 화창하네요<br>
그렇지만 미세먼지가 나쁘니 마스크를 꼭 착용하세요<br>
내일봅시다
~~~
결과 :<br>
안녕하세요. 패스트캠퍼스입니다.<br>
오늘은 날씨가 화창하네요<br>
그렇지만 미세먼지가 나쁘니 마스크를 꼭 착용하세요<br>
내일봅시다.
___


<br>
### (3) 그외 > hr, blockquote, pre태그
~~~
1. hr태그 (Horizontal rule, 수평선)
<hr>
~~~
결과 : <hr>
___
<br />

~~~
2. blockquote태그 (인용문)
<blockquote>인용문 내용</blockquote>
~~~
결과 : <blockquote>인용문 내용</blockquote>
____
<br />

~~~
3. pre태그 (Preformatted text, 이미 형식화된 텍스트)
<pre>
def pretag_test():
  val = 'pretag'
</pre>
~~~

결과 :
<pre>
def pretag_test():
  val = 'pretag'
</pre>
___

<br>
### (4) 줄바꿈 없는 텍스트 태그
~~~
1. strong, b태그 (강조, 굵게 표시)
	: 보이는 것은 같으나 오디오 청취시 다르게 발음한다. 
<strong>강조할 텍스트</strong>
<b>굵게 표시할 텍스트</b>```
~~~

<strong>strong hello</strong><br />
<b>b hello</b>
___
<br />

~~~
2. em, i태그 (문맥상 특정부분 강조, 이탤릭 표시)
	: i 태그의 경우 한글에는 지원되지 않는다.  
<em>강조할 텍스트</em>
<i>기울여 표시할 텍스트</i>
~~~

<em>em hello</em><br />
<i>i hello</i>
___
<br />

~~~
3. mark태그 (형광펜 효과)
	: 형광펜으로 그은 효과의 텍스트, 인라인요소이다.
<mark>형광펜으로 그은 효과텍스트</mark>
~~~
<mark>mark hello</mark>
___
<br />
<br>
<br>
><h2>이미지와 링크 태그</h2> image, hyperlink tag


### (1) 링크, anchor
**a 태그**<br>
**href** : 이동할 페이지주소<br>
**target** : 링크 걸린 페이지를 여는 법<br>
	(_self : 본래창에서 이동, _blank : 새창에서 열기)<br>
**title** : 마우스를 올렸을 때 보여줄 제목<br>

```
<a href="http://www.naver.com" target="_blank" title="네이버 열기">naver바로가기</a>
```
<br />
###(2) 이미지 삽입, image
**img 태그**<br>
**src** : 이미지의 경로<br>
**width, height** : 이미지의 가로/세로크기(px 단위)<br>
**alt** : 대체 텍스트<br>
alt 태그 역시 시각장애인에게 설명을 줄 만한 텍스트를 넣을 수 있다.

```
<img src="이미지의 경로" width="30" height="200" alt="이미지 설명">
```

<br>
><h2>데이터 태그</h2> data tags, 데이터를 나타내는 목록형 태그

### (1) 목록
: 목록 형태로 나타나는 요소는 ol이나 ul요소로 구현하고 css로 디자인한다.
> ordered list, ol<br>

~~~
<ol>
	<li>항목</li>
	<li>항목</li>
	<li>항목</li>
	<li>항목</li>
</ol>
~~~

> unordered list, ul

~~~
<ul>
	<li>항목</li>
	<li>항목</li>
	<li>항목</li>
	<li>항목</li>
</ul>
~~~

<br />
### 1) 목록 속성
**type=""** : 나열할 속성 정의 <br>

| 값 | 설명 |
|----|----------|
| 1 | 숫자(기본값) |
| a | 영문 소문자 |
| A | 영문 대문자 |
| i | 로마 숫자 소문자 |
| I | 로마 숫자 대문자 |

**start=""**: 시작할 숫자 지정

**reversed=""** : 역순으로 표시<br>

~~~
<ol type="A" start="3" reversed>
	<li>First</li>
	<li>First</li>
	<li>First</li>
</ol>
~~~

결과 : <br>
<ol type="A" start="3" reversed>
    <li>First</li>
    <li>First</li>
    <li>First</li>
</ol>

<br>
### 2) 정의목록
description list
: 목록과 정의목록은 서로 중첩하여 사용가능.

~~~
<dl> <!--정의목록 태그 -->
  <dt>dt는 목록 중 개념을 나타낸다.</dt>
  <dd>dd는 해당 개념의 정의를 나타낸다.</dd>
  <dd></dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheet</dd>
  <dd>HTML의 형태를 지정하는 언어이다.</dd>
</dl>
~~~
결과 : 
<dl>
  <dt>dt: 목록중 개념</dt>
  <dd>dd는 해당 개념의 정의를 나타낸다.</dd>
  <dd></dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheet</dd>
  <dd>HTML의 형태를 지정하는 언어이다.</dd>
</dl>

<br>
<br>
20170509_1
> ## 테이블 요소
표로 만들 수 있는 테이블 요소 


###(1) 테이블의 기본 구조
**table 태그** <br>
**thead / tbody / tfoot** : 행을 그룹화하는 태그 <br>
**tr** : 행 <br>
**th** : 헤더셀 <br>
**td** : 데이터셀 <br>

~~~
<table> : 테이블의 시작
 <thead> : 열의 제목, 한번만 선언 가능
  <tr> : 행을 나타냄
   <th>이름</th> : 테이블의 헤더셀
   <th>나이</th>
   <th>성별</th>
  </tr>
 </thead> 
 <tbody> : 본문, 여러번 선언하여 행을 그룹화하기도 한다.
  <tr> : 다음 행
  	<td>철수</td> : 테이블의 일반셀
   <td>23세</td>
   <td>남성</td>
  </tr>
 </tbody>
 <tfoot> : 도표 하단, 전체의 합계 또는 결과를 표시, 한번만 선언가능
  <tr>
   <td>평균</td>
  </tr>
 </tfoot>
</table>
~~~

**colspan** : 행 병합<br/>
**rowspan** : 열 병합

~~~
<table>
 <tr>
  <td rowspan="2">이름</td>
  <td>성별</td>
  <td>취미</td>
 </tr>
 <tr>
  <td colspan="2">나이</td>
 </tr>
</table>
~~~
결과 : 
<table>
 <tr>
  <td rowspan="2">이름</td>
  <td>성별</td>
  <td>취미</td>
 </tr>
 <tr>
  <td colspan="2">나이</td>
 </tr>
</table>

<br>
> ## Form 요소
데이터를 입력하거나 전송할 떄 사용하는 HTML 요소

**method 속성** : 폼에서 서버로 데이터를 전송하는 방식을 설정<br>

**GET** : URL에 데이터를 담아 전달 <br>
* 검색어 등이 URL에 담겨 출력된다. <br>
**POST** : URL과 별도로 데이터를 전달 <br>
* 아이디/패스워드 같은 중요정보는 POST방식으로 전달한다.

**action** : form에서 데이터를 전송할 URL

####(1) 라벨태그
~~~
<form action="입력한 값을 전송할 URL" method="get">  	<label for="username">ID</label> : 입력값에 대한 라벨을 붙여준다.
	<input type="text" name="username" placeholder="대소문자 구별"> : 입력창</form>
~~~
결과: 

<form action="" method="get">  	<label for="username">ID</label>
	<input type="text" name="username" placeholder="대소문자 구별"></form>

<input type="text" id="username" placeholder="대소문자 구별">  
* 라벨태그를 붙이지 않으면 어떤 입력창인지 모른다.<br>
* placeholder : 창 내부에 안내 텍스트를 쓸 수 있다.
___
<br/>

~~~
label 내부에 표현
<label>ID <input type="text"></label>

label과 별도로 표현 - for 속성과 id값을 연결
<label for="username">Username</label> 
<input type="text" id="username">
~~~
__라디오버튼__<br /><input type="radio" id="radio" name="check">  
<input type="radio" id="radio" name="what">  
<input type="radio" id="radio" name="what">  * 같은 name 아래에서, 라디오 요소를 복수로 사용하면 중복선택을 할 수 없다. 

__체크박스__<br /><input type="checkbox" id="checkbox" name="check">  
<input type="checkbox" id="checkbox" name="what">  
<input type="checkbox" id="checkbox" name="what" checked="checked">  * name 속성에 상관없이 복수 개 있을 때 중복 선택이 가능하다. <br>
* name 태그는 input태그에서 입력된 값을 전송할 때 담는 그릇이다 <br>
* checked : 이미 체크된 상태로 나온다.
___<br />~~~
<input type="button" value="button"><br/><input type="file" id="file"><br/>  <input type="submit"><br/>  <input type="reset"><br/>  
~~~
<input type="button" value="button">  <input type="file" id="file">  <input type="submit">  <input type="reset">  
*데이터 전송 폼 초기화~~~<input type="hidden" id="hidden" value="hiddenValue">
* 사용자에게 보여지지 않지만 관리상 전송해야하는 값이 있을 때 사용한다. 
~~~

<br>
####(2) select 태그 
: 여러개의 주어진 값 중 일부를 선택한다. 드롭다운!

> 기본형

<select name="number" id="select-id">
	<option value="1">First</option>
	<option value="2">Second</option>
	<option value="3">Third</option>
	<option value="4">Fourth</option>  </select>
___
<br />

> multiple형

<select name="number" id="select-id" multiple="multiple">
	<option value="1">First</option>
	<option value="2">Second</option>
	<option value="3">Third</option>
	<option value="4">Fourth</option>  </select>
*multiple 속성을 가질 경우 cmd키로 선택하므로 불편하여 잘 쓰지 않는다. 
___

<br/>
> size 지정

<select size="2">  	<option value="apple">Apple</option>
	<option value="banana">Banana</option>
	<option value="orange">Orange</option>  </select>
* 한번에 몇개의 option을 보여줄지 정할 수 있다.
___
<br />
> optgroup

<select name="" id="">
  <optgroup label="Fruits">
    <option value="apple">apple</option>
    <option value="banana">banana</option>
    <option value="orange">orange</option>
  </optgroup>
  <optgroup label="Colors">
    <option value="red">red</option>
    <option value="blue">blue</option>
    <option value="purple">purple</option>
  </optgroup>
</select>
* option을 그룹화하는 태그

~~~
<select name="number" id="select-id" multiple="multiple" size=2>
	<option value="1">First</option>
	<option value="2">Second</option>
	<option value="3">Third</option>
	<option value="4">Fourth</option>  </select>
~~~

<br>
#### (3) button 태그
`<button type="button">button type button</button>`

<button type="submit">submit type button</button>
<button type="reset">reset type button</button>
<button type="button">button type button</button>
*input태그의 type을 사용할 수 있다. 

<br>
#### (4) fieldset, legend 태그
~~~
<fieldset>  	<legend>Login</legend>  	<label>username : <input type="text"></label>
	<label>password : <input type="password"></label>  </fieldset>
~~~

<fieldset>  	<legend>Login</legend>  	<label>username : <input type="text"></label>
	<label>password : <input type="password"></label>  </fieldset>
* 영역을 나누고 싶을 때 사용한다.
* legend라는 하위 태그 첫번째로 사용해야한다.
* 다른 fieldset과도 중첩 가능하다.

<br>
+++

###클래스와 아이디의 차이 
네이밍 : 첫글자는 알파벳으로, 대소문자 구분


> id : 페이지에서 딱 한번만 선언할 수 있다. 요소의 unique한 특성을 나타낼 때 사용<br>
> class : 여러번 중복 사용가능하다. 범용적인 부분.

<br />
+++
### 색상
`<p style="color=#333;">Color</p>`
`<p style="color: DarkGreen;">Color DarkGreen</p>`

<p style="color=#333;">Color</p>
<p style="color: DarkGreen;">Color DarkGreen</p>

* 16진수를 이용할 수도 있고 색상이름을 쓸수도 있다.
* 또는 rgb(255, 255, 255)로 써도 가능하다.

<br>
<br>
20170509_2
> ## CSS
마크업 언어(HTML)가 실제 표시되는 방법을 기술하는 언어.<br>
레이아웃과 스타일을 정의할 때 사용한다.


###(1) 기본구조
```
선언블럭
selector선택자 {
	property속성: value값;
}

ex_
#body title {
	font-size : 14px;
}
```
<br>
🌝 ==HTML에는 스타일을 제외한, 문서의 구조만 명확히 나타나야한다!!<br>==
~~취소선~~
	html 내부에 작성하는 법은 권장되지 않는다!
> 1. 내부 스타일시트 (Internal StyleSheet)
>
>>head 안쪽, style태그 내부에 작성한다.


> 2. 인라인 스타일시트(Inline StyleSheet)
>>사용할 요소의 style속성에 정의한다.
>>내용과 스타일이 분리되지 않으므로 너무 길어지는 단점이 있음.


#### 3. 외부 스타일시트 (External StyleSheet)
`<link rel="stylesheet" href="style.css">`<br>

* css 파일과 html 파일을 분리하여 관리한다.<br>
* head 안에 link 태그를 작성하여 두 파일을 서로 연결한다.


<br>
<br>
> ## CSS 선택자
CSS의 속성을 부여할 HTML 요소를 선택하는 선택자의 종류들

###(1) 전체 선택자, Universal Selector, "==*=="

~~~
  <style>
    div * {
      padding: 0;
      margin: 0;
    }
  </style>
  
html
<h1>hello!</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto fuga aperiam accusantium illum adipisci impedit!</p>

~~~

* HTML 페이지 내부의 모든 요소에 CSS속성 적용
* 문서 전체에 적용하므로 로딩시간이 길어질 수 있다. 사용권장x
* 전체 기본값 초기화할 때 주로 사용한다.

<br>
####(2) 태그 선택자, Tag Selector, "요소이름"

~~~
h1 p {
      margin: 10px;
      text-align: center;
      color: #ccc;
    }
~~~

* p, h1같은 해당하는 모든 html요소에 적용한다.

<br>
####(3) 클래스 선택자, Class Selector, "."

~~~
/*클래스 선택자*/
 	.section {
      color: #333;
      margin-bottom: 40px;
    }
    /*p를 써도되고 생략해도 된다*/
    p.section-title {
      font-size: 30px;
    }
    
html 
<div class="section">
    <p class="section-title">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sit, iste.</p>
    <p class="section-content">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis, asperiores.</p>
  </div>
~~~

* 선택자 앞에 마침표 기호를 사용한다.
* 앞에 태그명을 입력하여 HTML에서는 주어진 값을 class속성값으로 가진 요소를 선택할 수도 있다.
* 클래스는 연달아 써서 동시에 여러개의 클래스에 속성을 부여할 수도 있다.

<br>
####(4) ID 선택자, ID Selector, "#"

~~~
css
#id-selector a {
      color: lightblue;
      text-decoration-line: none;
    }
    
html
<div id="id-selector">
    <a href="">출처</a>
    <span>lorem</span>
    <span>copyright@</span>
  </div>
~~~

* 선택자 앞에 # 기호를 사용한다.
* HTML에서 id값은 오직 하나만 존재해야한다.
* 앞에 태그명을 입력할 수 있다.
* **id선택자의 우선순위가 class선택자보다 높으므로 2개의 값을 지정했을 때는 id선택자의 값이 적용된다.**

<br>
####(5) 체인 선택자, Chain Selector

~~~
/*체인선택자 : 복수 개의 선택자 사용*/
    #index-title {
      font-size: 18px;
    }

    #index-title.header-title {
      font-weight: bold;
    }

    .body-text.descrip {
      color: #999
    }
    
 
html
<h3 id="index-title" class="header-title">Lorem ipsum dolor sit amet.</h3>
<p class="body-text descrip">Lorem ipsum dolor sit amet.</p>
~~~
   
 
결과:
<h3 id="index-title" class="header-title">Lorem ipsum dolor sit amet.</h3>
<p class="body-text descrip">Lorem ipsum dolor sit amet.</p>
___
* ==한 요소에 아이디와 클래스들 또는 복수의 클래스가 적용되어 있을 경우 사용==한다.
* 아이디 선택자의 우선순위가 높으므로 아이디와 클래스 선택자를 동시에 적용한 경우 중복되는 속성은 아이디 선택자의 값을 따른다.


<br />
**!! 체인선택자를 사용하는 예시**<br>

* 주로 공통속성과 특별히 적용할 속성이 있을 경우 여러 클래스를 써서 속성을 나누어 배정한다.

~~~
css
    .nomargin {
      font-size: 0;
    }

	.inline-block {. <!--공통적인 클래스 속성-->
      display: inline-block;
      width: 50%;
      height: 50px;
      /*margin: 10px;*/
      box-sizing: content-box;
      box-sizing: border-box;
      border-width: 3px;
      border-style: solid;
      font-size: 0.9rem;
    }
    .box-red {  <!--다른 값을 줄 클래스-->
      border-color: red;
    }
    .box-blue {  <!--다른 값을 줄 클래스-->
      border-color: blue;
    }
    
html
<div class="nomargin">
    <div class="inline-block box-red">
      ASDFASDF
    </div>
    <div class="inline-block box-blue">
      SEFSEF
    </div>
  </div>
~~~

<br>
<br>
####(6) 그룹 선택자, Group Selector

~~~
/*그룹선택자*/
    #index-title {
      font-size: 18px;
    }
    p#index-title, #description {
      text-align: center;
    }

html
<p id="index-title" class="header-title">Lorem ipsum dolor sit amet.</p>
<p id="description" class="body-text descrip">Lorem ipsum dolor sit amet.</p>
~~~

결과 :

<style>
    #index-title {
      font-size: 18px;
    }
    p#index-title, #description {
      text-align: center;
    }
</style>
<div>
	<p id="index-title" class="header-title">Lorem ipsum dolor sit amet.</p>
	<p id="description" class="body-text descrip">Lorem ipsum dolor sit amet.</p>
</div>
---
* 여러 선택자에 같은 스타일을 적용하는 경우
* 쉼표로 구분하여 선택자를 나열한다.

<br>
<br>
####==(7) 복합 선택자, Combinator Selector==

**하위선택자와 자식선택자<br>(descendant / child selector)**
<br>* 포함관계를 가지는 태그 중 포함: 부모요소 / 포함되는 : 자식요소

#####- 하위 선택자(descendent)
==section ul {}==

~~~
section ul {
	 border: 1px solid black;
	}
~~~
하위 선택자는 부모요소에 포함된 "모든" 하위요소를 지정
<br>
___
#####- 자식 선택자(Child)
==section > ul {}==

~~~
section > ul {
	border: 1px solid black;
}
~~~
자식 선택자는 부모요소의 "바로 아래" 자식요소만을 지정
___
___
<br>


**인접형제 선택자와 일반형제 선택자 <br>(Adjacent / General Sibling)**

* 같은 부모요소를 가지는 요소들은 "형제관계"
* 먼저 나오는 요소 : 형요소 / 나중의 요소 : 동생요소

##### - 인접 형제 선택자(Adjacent Sibling)
==h1 + ul {}==

~~~
h1 + ul {
	background: Azure;
	color : blue;
}
~~~
조건을 충족하는(바로 다음에 나오는) "첫번째" 동생요소만을 지정
<br>_형 요소에는 적용되지 않는다._

##### - 일반 형제  선택자(General Sibling)
==h1 ~ ul {} <br>==

~~~
h1 ~ ul {
	background: Azure;
	color : blue;
}
~~~
조건을 충족하는 "모든" 동생요소를 지정
<br>_형 요소에는 적용되지 않는다._


<br>
#### (8) 속성 선택자 (Attribute Selector)
태그 내의 속성에 따른다.

|패턴|의미|
|---|---|
|`p [attr]`|'attr'속성이 포함된 요소 E|

~~~
`<E attr>lorem</E>`
~~~
<br>

|패턴|의미|
|---|---|
|`E[attr="val"]`|'attr'속성의 값이 "val"인 요소 E|

~~~
`<E attr="val">lorem</E>`
~~~
<br>

|패턴|의미|
|:---:|:---:|
|`E[attr~="val"]`|'attr'속성의 값에 "val"이 포함되는 요소 E<br>==공백으로 분리된 값이 일치해야한다!==|
~~~
<E attr="val">lorem</E>
<E attr="val-num3">lorem</E>
<E attr="value">lorem</E>`는 적용안됨.
~~~
<br>

|패턴|의미|
|:---:|:---:|
|`E[attr|="val"`|'attr'의 값에 "val"이 포함되거나(공백으로 분리되어있는)<br>"val"로 시작하는 요소 E<br>value같이 들어있으면 인식하지 않는다.|
~~~
<E attr="val">lorem</E>
<E attr="val-num3">lorem</E>
<E attr="value">lorem</E>는 적용 안됨`
~~~
<br>

|패턴|의미|
|:---:|:---:|
|`E[attr^="val"`|'attr'속성의 값이 "val"로 시작하는 요소 E|

~~~
<E attr="val">lorem</E>
<E attr="val-num3">lorem</E>는 안됨
<E attr="value">lorem</E>
~~~
<br>

|패턴|의미|
|:---:|:---:|
|`E[attr$="val"`|'attr'속성의 값이 'val'로 끝나는 요소 E|

~~~
<E attr="val">lorem</E>
<E attr="item-val">lorem</E>
<E attr="eval">lorem</E>은???
~~~
<br>

|패턴|의미|
|:---:|:---:|
|`E[attr*="val"`|'attr'속성의 값에 "val"이 포함되는 요소 E<br>==공백이나 Dash(-)에 영향을 받지 않는다!==|

~~~
<E attr="val">lorem</E>
<E attr="val-num3">lorem</E>
<E attr="value">lorem</E>
~~~

<br>
<br>
#### (9) 가상클래스 선택자 (Pseudo-Classes Selector)
HTML소스에는 존재하지 않지만 필요에 의해 가상의 선택자 지정 가능
* 이 경우 드래그 해도 잡히지 않음. 

|패턴|의미|
|:---:|:---:|
|`E:link`|방문하지 않은 링크 E|
|`E:visited`|방문한 링크 E|
|`E:active`|E요소에 마우스 클릭 또는 키보드 엔터가 눌린 동안 보이는 효과지정|
|`E:hover`|E 요소에 마우스가 올라가있는 동안 보이는 효과 지정|
|`E::focus`|E 요소에 포커스가 머물러있는 동안 보이는 효과 지정|
|`E::first-line`|E의 첫번째 라인에 효과지정|
|`E::first-letter`|E의 첫번째 문자에 효과지정|
|`E::before`|E요소의 시작지점에 생성된 요소|
|`E::after`|E요소의 끝지점에 생성된 요소|

---
<br>

## CSS 우선순위

**특정도** : css구문에서 해당하는 스타일 수 * 특정도 값을 더한 값

특정도 계산식 

|스타일|특정도|특정도값|
|:----:|:----:|:-----:|
|`!important`|absolute|-|
|Inline(인라인 스타일)|A|1000|
|ID 선택자|B|100|
|Class 선택자|C|10|
|Tag 선택자 |D|1|

**!important** : 어떤 특정도도 무시하고 가장 우선순위로 적용하게 해준다. 
==유지보수에 부적절. 잊어버리면 끝장! 절대로 쓰지 말 것.==
