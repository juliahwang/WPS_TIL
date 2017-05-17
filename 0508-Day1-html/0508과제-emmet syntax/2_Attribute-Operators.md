## 속성 연산자 (Attribute Operators)
: 속성 연산자들은 출력된 요소들의 속성들을 수정하기 위해 사용된다. <br>
: HTML과 XML에서는 class속성을 손쉽게 생성된 요소에 적용할 수 있다.

### (1) ID # and Class .
: CSS에서는 **elem#id**나 **elem.class** 표기법을 사용하여 특정 id나 class 속성을
요소와 연결한다. emmet에서도 매우 유사한 문법을 사용하여 특정 요소에 속성을 부여한다.

~~~
div#header [tab]
: div 요소에 header id 부여

div.page [tab]
: div 요소에 page class 부여

div#footer.class1 [tab]
: id,class 동시에 부여할 수도 있다.

결과 :
<div id="header"></div>
<div class="page"></div>
<div id="footer" class="class1 class2 class3"></div>
~~~

<br>
### (2) Custom attributes: [attr]
~~~
td[title="Hello World" colspan=3] [tab]
: []안에 쓰고 싶은 속성을 추가하여 사용한다.
: []안에 들어가는 속성의 수에는 제한이 없다.

td[colspan title] [tab]
: 속성값을 써주지 않아도 작성해준다.

td[title=hello colspan=3]
: 속성값에 띄어쓰기가 없다면 인용첨자("")를 쓰지 않아도 작성된다.


결과 :
<td title="Hello World" colspan="3"></td>

<td colspan="" title=""></td>

<td title="hello" colspan="3"></td>
~~~

<br>
### (3) Item Numbering: $


`ul>li.item$*5 [tab]`<br>
: "$" 연산자를 사용하여 요소에 넘버링을 부여할 수 있다.
: "$" 연산자는 요소의 이름, 속성이름 또는 속성값에 넘버링을 부여한다.

~~~
결과 :
<ul>
  <li class="item1"></li>
  <li class="item2"></li>
  <li class="item3"></li>
  <li class="item4"></li>
  <li class="item5"></li>
</ul>
~~~

~~~
ul>li.item$$$*5 [tab]
: $를 1개 이상 쓰면 0으로 인식하여 패딩을 줄 수 있다.

결과 :
<ul>
  <li class="item001"></li>
  <li class="item002"></li>
  <li class="item003"></li>
  <li class="item004"></li>
  <li class="item005"></li>
</ul>
~~~

<br>
### (4) Changing Numbering Base and Direction : @

~~~
ul>li.item$@-*5 [tab]
: "$" 뒤에 "@-" 연산자를 붙이면 역순으로 넘버링을 부여한다.

결과 :
<ul>
  <li class="item5"></li>
  <li class="item4"></li>
  <li class="item3"></li>
  <li class="item2"></li>
  <li class="item1"></li>
</ul>
~~~

~~~
ul>li.item$@3*5 [tab]
: "@" 뒤에 넘버링을 시작하는 숫자를 쓰면 그 숫자부터 넘버링을 부여한다.

결과 :
<ul>
  <li class="item3"></li>
  <li class="item4"></li>
  <li class="item5"></li>
  <li class="item6"></li>
  <li class="item7"></li>
</ul>
~~~

~~~
ul>li.item$@-3*5 [tab]
: 역순, 넘버링시작지정을 함께 쓸 수도 있다.

결과 :
<ul>
  <li class="item7"></li>
  <li class="item6"></li>
  <li class="item5"></li>
  <li class="item4"></li>
  <li class="item3"></li>
</ul>
~~~

<br>
## Text : {}
: 중괄호를 사용하여 요소에 텍스트를 추가할 수 있다.

~~~
a{click me} [tab]
: a라는 요소에 "click me" 텍스트를 추가한다.

결과 :
<a href="">click me</a>
~~~

**중요 : {text}는 분리된 요소에서만 파싱(분석)된다.**
{text} 연산자는 요소 바로 뒤에 쓰여졌을 때 부모의 맥락을 해치지 않는다.

~~~
a{click} = a>{click}
결과 :
<a href="">click</a>
<a href="">click</a>

a{click}+b{here} 와
a>{click}+b{here} 는 다르다.

결과 :
<a href="">click</a><b>here</b>
<a href="">click<b>here</b></a>
~~~

중요한 다른 예

~~~
p>{click }+a{here}+{ to continue} [tab]
결과 :
<p>click <a href="">here</a> to continue</p>

p{click }+a{here}+{ to continue} [tab]
결과 :
<p>click </p>
<a href="">here</a> to continue
~~~

<br>
## 축약문법에는 띄어쓰기가 필요없다~!
: 축약문법은 템플릿 언어가 아니라 빨리쓰고 지우기 위한 것이므로 띄어쓰기를 적용하면 작동하지 않는다.
