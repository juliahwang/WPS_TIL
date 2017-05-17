## 내포된 태그 이름들 (Implicit Tag Names)
: tag 이름을 쓰는 것조차 반복적일 수 있다.<br>
: 따라서 id나 class 속성을 부여할 때 부모 태그 내에서 작성하면 자연스레 그 계층구조를 따르고 tag 이름을 따로 사용하지 않아도 되도록 하는 기능을 소개한다.

~~~
축약어를 사용할 때 에멧은 부모의 컨텍스트를 따와서 축약형 문법을 확장한다.

<body>
  <div>
    .item [tab]
  </div>
  <span>.item [tab]</span>
  <ul class="nav">
    .item [tab]
  </ul>
</body>

결과 :
<body>
  <div>
    <div class="item"></div>
  </div>
  <span><span class="item"></span></span>
  <ul class="nav">
    <li class="item"></li>
  </ul>
</body>

~~~
<pre>
에멧은 부모의 태그이름을 참조하여 내포이름을 확장한다.

- **li** : ul and ol
- **tr** : table, tbody, thead, tfoot
- **td** : tr
- **option** : select, optgroup
</pre>

~~~
.wrap>.content [tab]
div.wrap>div.content [tab]
<div class="wrap">
  <div class="content"></div>
</div>
~~~

~~~
em>.info [tab]
em>span.info [tab]
<em><span class="info"></span></em>
~~~

~~~
ul.item*3 [tab]
<ul class="item"></ul>
<ul class="item"></ul>
<ul class="item"></ul>

ul>li.item*3 [tab]
<ul>
  <li class="item"></li>
  <li class="item"></li>
  <li class="item"></li>
</ul>
~~~

~~~
table>#row$*4>[colspan=2] [tab]
<table>
  <tr id="row1">
    <td colspan="2"></td>
  </tr>
  <tr id="row2">
    <td colspan="2"></td>
  </tr>
  <tr id="row3">
    <td colspan="2"></td>
  </tr>
  <tr id="row4">
    <td colspan="2"></td>
  </tr>
</table>

table>tr#row$*4>td[colspan=2] [tab]
<table>
  <tr id="row1">
    <td colspan="2"></td>
  </tr>
  <tr id="row2">
    <td colspan="2"></td>
  </tr>
  <tr id="row3">
    <td colspan="2"></td>
  </tr>
  <tr id="row4">
    <td colspan="2"></td>
  </tr>
</table>
~~~
