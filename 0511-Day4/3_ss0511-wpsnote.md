######20170508 - 0511
##필기내용 정리 
> 
작성자 : 황선정

<br>
######20170508
### (1) 모르는 개념
**API** -
API(Application Programming Interface, 응용 프로그램 프로그래밍 인터페이스)는 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다.<br>

**RESTful** -<br>
[위키피디아 바로가기][1]
[1]: https://ko.wikipedia.org/wiki/REST
**Markdown** - 문서에 양식을 쉽게 적용할 수 있으며 양식과 텍스트를 물흐르듯이 작성할 수 있게 해주는 문법. HTML을 모르는 사람도 쉽게 쓸 수 있는 간단한 문법을 가진다.<br>
[문법 보기][2]
[2]: https://learn.getgrav.org/content/markdown 
<br>
<br>
###(2) 기초이론
##### # html과 css
* 웹표준이 등장하기 전까지는 브라우저별로 웹페이지를 제작.<br>
* 웹표준에 맞는 html과 css를 지켜야 브라우저에서 모두 동일한 화면이 구현됨.<br>
* 웹표준 지원에 대한 브라우저 점수 확인하는 사이트
[바로가기][1]
[1]:http://html5test.com/


##### # html 
* <!DOCTYPE html> - html5를 사용하겠다는 선언

*	주석표시 : <!— 주석 —>
* ==절대경로== : 
`<img src = "https:// ~">`
 - http:// 또는 https://로 시작. 
 - 해당 주소로 들어가서 이미지를 띄움.

* ==상대경로== : 
`<img src = "images/sample.png">`
 - 컴퓨터 내에 저장되어 있는 경로
 - <요소 속성="값">내용</요소>

___
<br>
 
###### 20170509
 
##### # Form 
* hiddenValue: 사용자에게 보여주지 않으나 서버에 접속할 때 필요한 값을 넣는다. 

* radio버튼
 - 같은 name하에 있는 버튼은 중복선택이 불가능하다. 
<br>


##### # Color code
* Hex code
	-16진수로 색을 나타낸다
	- 0부터 15까지 16진수로 3가지(RGB, 빛의 3원색) 색상의 혼합값을 나타낸다. 
* `Color: rgb(128, 30, 25);` <br> 이렇게 십진수로 쓸수도 있다.
Rgba - 투명도(alpha)까지 조절 가능
<br>

##### # name태그
* input내에서 입력된 값을 전송할 때만 사용한다. 즉, 전송된 값을 담는 그릇인 것


##### # 개발자도구<br> 
* Fliter에서 `<p>`태그는 기본 24px의 padding을 가진다.<br>
* 테스트해보고 싶을 때는 `element.style {}` 안에 적용해본다.
* `'+'`를 눌러서 css를 추가 적용할 수도 있다.
* colsole창에서는 에러파일이 뜬다.
* 모든 웹브라우저는 자바스크립트를 탑재하고 있다. 이는 콘솔에서도 간단하게 적용해볼 수 있다. 


**input태그의 type값은 검색해보기**

___
<br>
###### 20170510
##### # slack 사용법 
* Wps-random에서 주로 소통<br>
 * slackbot소환 가능
 * 다양한 슬랙봇이 있음.<br>
	ex_ 투표할 수 있는 슬랙봇<br>
	/poll "질문?" "1번" "2번" "3번"
	/ : 슬랙봇 검색 가능

|기능|의미|
|:--:|:--:|
|?list|검색할 수 있는 정보들이 뜬다.|
|*굵게*|볼드표시|
|\`메세지강조`|메세지강조| 
|\```구분블럭```|영역| 
|~취소선~|취소선| 
|_기울기_|이탤릭|
|shift + enter|줄바꿈| 
|입력창오른쪽 이모티콘|커스텀 이모티콘 등록가능|
|@아이디|호출|
|@channel|모든 사람 호출| 
|cmd+ctrl+/|단축키모음|  
<br>
##### # 마크다운 문법
Github사이트에서만 보이는 마크다운 문법이 있음.
체크박스 이모지 등은 로컬에디터에서는 보이지 않지만 깃헙에 올리면 보인다. 
<br>

##### # 인라인요소의 특성
==인라인 요소는 블록 요소를 내부에 가질 수 없다.==

~~~html5
<span> 
	<p>'hello'</p>
</span>	(x)
~~~

##### # css파일연결 - 상대경로에 대하여
경로 = ./경로
/경로 :  전체 루트폴더로 이동
~/경로 : 사용자폴더(home으로)로 이동


##### # 요소 간 수직정렬
: 인라인 요소 간의 정렬을 의미함

* Sub, super는 잘 안쓴다.
* Top, bottom, Text-top, text-bottom은 자주 쓰지만 브라우저별로 다르게 보일 수 있다. 

##### # 배경이미지 

* 상대/절대경로 모두 사용가능하다.
* 상대경로의 경우에는 css파일에 대한 상대경로 주소를 넣어줘야 한다!(external방식이라 가정하고) 따라서 이미지파일이 따로 있는 경우에는 연결에 유의해야한다.

* 절대경로면 상관없음.
* 인라인방식인 경우에는 html기준으로 이미지 위치를 적어준다.
* sass에서는 변수형태로 바꿔서 넣거나 절대경로로만 넣는 경우도 있다. 


##### # 배경이미지 반복
그라데이션 효과 - 요즘은 css 속성으로 만든다.

##### # Linux

* 미리보기
 * 도구-크기조절에서 바로 이미지 크기를 조절할 수 있다.
 * cmd+k : 이미지 잘라쓰기 가능


##### # border의 속기법 

`Border : 1px solid red;` <br>
각 변에 다른 값을 주고 싶을 때는 4가지 값을 입력하거나 특정 요소를 지정하여 값을 입력해야한다. 


##### # Html:5 입력시 언어 설정
아톰 settings(cmd+,)에서 emmet 패키지 설정으로 가면 아래 settings에서 따로 사용자파일을 등록하여 원하는 설정을 커스텀한 상태로 만들 수 있다. 

* Keybindings 
	* your keymap files - keymap.json 에 저장된 커스텀 코드 

~~~
'atom-text-editor':
  'cmd-i': 'editor:auto-indent'
  'cmd-left': 'emmet:prev-edit-point'
  'cmd-right': 'emmet:next-edit-point'
~~~


##### # Spotlight 단축키 설정변겅
Ctrl + space 는 대부분의 개발 툴에서 자동완성기능을 제공한다. 
중복을 피하기 위해 spotlight는 `ctrl + ``로 바꿔준다.



##### # CSS 스타일
###### (1) 마진
 - 바깥여백, 중복 안됨(겹침x)
 - 배경색이 적용되지 않는다.

###### (2) 패딩
 - 내부여백, 중복 가능(겹침)
 - 배경색 적용됨

###### (3) width와 height

* width와 height는 content의 크기만을 의미함

###### (4) box-sizing 선택자
`Box-sizing : border-box;` <br>

* 원하는 전체 px크기에 맞추어 이미지 크기가 줄어든다. <br>
* 기본 설정 - `content-box;`<br>
* 가로 세로크기가 원하는 컨텐츠크기에 맞춰진다.<br>


###### (5) 리스트 스타일/이미지 

- 잘 쓰지 않는다.
- 블릿타입은 이미지를 못찾을 경우 대신나온다.(엑박)


###### (6) IDE (integrated Dev Environ)
통합개발환경 ex_아톰, 편집기, idle ...

<br>
___
######20170511

##### # Float 
	- 블록속성을 없앤다.
블록은 생성시 한 줄을 차지하는 요소이다. 이특성을 비활성화하여 다음 요소가 같은 줄 바로 옆이나 오른쪽에 정렬되도록 해준다. 
<br>ele2에 float:right;를 적용하면 원래있던 줄의 오른쪽으로 이동하고 ele3은 올라온다

##### # Clear <br>
	- float 속성을 없앤다.
<br>
##### # Position
(1) relative는 top/bottom, left/right 속성을 사용하여 위치를 지정할 수 있다.

(2) apsolute는 top/bottom, left/right값을 주면 root값까지 거슬러 올라가서 적용되므로 fixed를 사용한 것과 다를 바가 없게 된다. 이를 방지하기 위해서는 인접 부모요소에 position: relative;값을 준다.

<br>
##### # Sass
- css전처리기: css확장언어의(sass)의 파일을 웹브라우저에서 해석할 수 있는 css파일로 만들어주는 처리기.
- 함수, 변수 지정 사용가능<br>
- 확장자: ".scss"
- 주석 : "//" 또는 "/**/"

<br>
##### # sass파일을 저장할 경우 
(1) Compressed style

- 클라이언트에게 제공할 때 최대한 파일크기를 줄여줘야하므로 공백,엔터값을 없앤 컴프레스드(compressed) 스타일로 서빙.

(2) Expanded style

- sass스타일로 div 아래 꺽쇠를 쓰면 자식선택자.
css스타일로 변환되면 꺾쇠가 사라진다.(같은 요소를 공유하므로)

<br>
##### # Sass문법 
p.190 부모 참조 선택자(&)

~~~
.link-container & {
	font-size: 30px;
}
~~~
&를 역순으로 쓰면 관리하기 힘듦. 따라서 안쓰는 것이 좋다. 

p.191 선택자 상속 (@extend)

~~~
.btn { 
 font-size: 12px
 background-color: red;
 color: white;
 padding: 5px 20px;
}

.bth-ok {
 @extend .btn;
 background-color: blue;
}
~~~
@extend - btn에도 적용됨.

p.192 대체 선택자 (%)

~~~
%btn { 
 font-size: 12px
 background-color: red;
 color: white;
 padding: 5px 20px;
}

.bth-ok {
 @extend .btn;
 background-color: blue;
}
~~~
%와 결과는 같으나 btn은 변수로 사용된다.
대체 선택자로 선언된 구문은 실제 btn이라는 요소가 있어도 btn에 적용되어 출력되지 않는다.

<br>
##### # _variables.scss
_로 시작하는 파일은 컴파일되지 않는다. 
변수명을 저장하는 파일로 사용.
import할 때 _는 써주지 않아도 동작한다.
변수 예시> $변수명: 변수값;
 

##### # css파일을 브라우저별로 최적화해주는 사이트!

[홈페이지][3]
[3]: https://necolas.github.io/normalize.css/
[최적화코드][4]
[4]: https://necolas.github.io/normalize.css/7.0.0/normalize.css


