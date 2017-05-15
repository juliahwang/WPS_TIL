2017-05-08 homework

# **Emmet documentation** -Abbreviations Syntax
축약형 문법 Abbreviations Syntax

~~~
요소생성 (elements)
  : 요소를 생성하려면 요소를 쓴 후 tab을 누른다.

div + [tab] -> <div></div>
foo + [tab] -> <foo></foo>
~~~

<br>
## 둥지 연산자 (Nesting Operators)
  : 생성된 트리 구조 안에 축약형 요소들을 만들어내기 위해 사용 <br>
  : 문맥 요소 가까이 있거나 안에 있을 때.

### (1) child : >
~~~
div>ul>li [tab]
: ">" 연산자를 사용하여 연산자 둥지를 구성할 수 있다.

결과:
<div>
  <ui>
    <li></li>
  </ui>
</div>
~~~

### (2) Sibling: +
~~~
div+p+blockquote [tab]
: "+" 연산자를 사용하여 등위 요소들을 나열할 수 있다.

결과 :
<div></div>
<p></p>
<blockquote></blockquote>
~~~


### (3) Climb-up: ^
~~~
div+div>p>span+em [tab]
: ">"를 쓰면 생성된 sibling 요소의 트리와 포지션을 가장 깊은 요소로 내린다.

결과 :
<div></div>
<div>
  <p><span></span><em></em></p>
</div>
~~~
~~~
div+div>p>span+em^bq [tab]
: "^"연산자를 사용하면 ^다음에 사용할 요소는 트리의 한 층을 올라간다.

결과 :
<div></div>
<div>
  <p><span></span><em></em></p>
  <blockquote></blockquote>
</div>
~~~
~~~
div+div>p>span+em^^^bq [tab]
: "^"연산자 개수만큼 트리의 층을 거슬러 올라간다.

결과 :
<div></div>
<div>
  <p><span></span><em></em></p>
</div>
<blockquote></blockquote>
~~~


### (4) Multiplication: *
~~~
ul>li*5 [tab]
: "*" 연산자를 사용하여 사용하고 싶은 요소 개수만큼 곱하여 출력할 수 있다.

결과 :
<ul>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
</ul>
~~~

<br>
### (5) Grouping: ()
~~~
div>(header>ul>li*2>a)+footer>p [tab]
: 복잡한 축약형 문법을 사용할 때 하위 트리를 그룹핑하여 삽입어구를 사용한다.

결과 :
<div>
  <header>
    <ul>
      <li><a href=""></a></li>
      <li><a href=""></a></li>
    </ul>
  </header>
  <footer>
    <p></p>
  </footer>
</div>
~~~
~~~
(div>dl>(dt+dd)*3)+footer>p [tab]
: 벌써 그룹핑한 요소들을 또다시 그룹핑할 수 있으며, 그룹핑에 * 연산자를 사용할 수도 있다.

결과 :
<div>
  <dl>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
  </dl>
</div>
<footer>
  <p></p>
</footer>
~~~
