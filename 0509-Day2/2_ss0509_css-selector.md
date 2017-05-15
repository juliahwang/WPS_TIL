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
