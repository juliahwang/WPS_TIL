###### 20170516

## CSS Abbreviations

#### vendor prefixes - 브라우저용 접두사 

- bdrs 앞에 하이픈(-)을 붙이면 브라우저에 최적화된 스타일을 지정할 수 있다. 
- bdrs 앞에 하이픈은 snippets.json에서 해당 명령어에 대한 스니펫 정의를 찾아본다. 이에 따라 border-radius로 정의되어 출력되는 것. 
- 그 후 css로 정의된 카탈로그들을 알아본다. {vendor}Properties는 사용자에 의해 덧씌워질 수 있으며, {vendor}는 브라우저별로 최적화된 값을 지정할 수 있는 webkit이나 moz 등이 있다. 

ex>
`-bdrs` 

~~~
-webkit-border-radius: ; -chrome
-moz-border-radius: ; -firefox
border-radius: ; -IE
~~~

bdrs는 css webkit과 moz 속성에 정의되어 있으므로 두 개의 스타일 속성이 출력되지만, `foo`는 등록되어 있지 않은 속성이므로 모든 브라우저의 prefix 속성이 출력된다. 

ex>
`-foo`

~~~
-webkit-super-foo: ;
-moz-super-foo: ;
-ms-super-foo: ;
-o-super-foo: ;
super-foo: ;
~~~

<br>
#### prefixed properties를 디폴트로 등록하기 

- emmet에서 css.autoInsertVendorPrefixes를 활성화해놓으면 하이픈(-)을 쓰지 않아도 축약문법을 썼을 때 vendor-prefixed 속성을 출력할 수 있다. 

ex> `bdrs` or `trf`

~~~
* when css.autoInsertVendorPrefixes is activated

-webkit-border-radius: ;
-moz-border-radius: ;

-webkit-transform: ;
-moz-transform: ;
~~~


<br>
#### Explicit vendor prefixed - 좀더 분명하게 명령어 입력하기

- 축약문법은 브라우저별로 1글자의 접두사(prefix)를 제공한다.
 
~~~
w : webkit
m : moz
s : ms
o : o
~~~

`-wm-trf: ;`

