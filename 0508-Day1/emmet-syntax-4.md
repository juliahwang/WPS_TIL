## “Lorem Ipsum” 생성자
: “Lorem Ipsum” 더미 텍스트는 웹 개발자들이 실제 데이터를 가지고 HTML이 어떻게 보일 것인지 테스트하기 위해 사용된다.


### lorem [tab]
: lorem은 단순 스니펫이 아닌 생성자이다. 30자의 나눠진 문장으로 구성된 더미 텍스트를 생성하는 생성자이다.<br>

### lorem100 [tab]
: 필요한 단어수만큼 생성할 수도 있다.

~~~
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut laboriosam, non magnam illum dolor mollitia expedita esse, voluptatem debitis perspiciatis qui placeat totam commodi voluptatibus odio, itaque adipisci distinctio nam.
~~~

### lipsum [tab]

~~~
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel natus iure, ut sit dolores aspernatur veniam officiis temporibus obcaecati, repellat et aliquam delectus illo ratione harum assumenda nesciunt nihil excepturi.
~~~

### 반복된 "Lorem ipsum"
: 반복하는 요소 안에 lorem 생성자를 이용하여 더미 텍스트로 채워진 태그를 만들 수 있다.

~~~
p*4>lorem [tab]

결과 :
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ex, qui earum soluta illo sint quia eaque minima nisi omnis, distinctio. Iusto velit amet, enim hic incidunt expedita quod molestiae dignissimos.</p>
<p>Autem nemo quae labore veniam at, deleniti excepturi fuga ducimus nesciunt perspiciatis aperiam vitae porro illo aut ex recusandae, amet consectetur sunt alias. Similique, expedita porro laudantium tempore molestiae cumque!</p>
<p>Itaque expedita aperiam repellendus at, facere soluta excepturi et ducimus, ipsum pariatur alias dolorum quibusdam deleniti ipsam sit labore. Quisquam magnam officiis veniam dolorem vero quam, exercitationem inventore ea quod!</p>
<p>Eum consequuntur, quibusdam tempore. Repellat dignissimos enim veniam, sunt, suscipit ipsam nostrum soluta in molestias sint sequi voluptates, delectus temporibus iure aliquid deserunt necessitatibus eveniet fugit voluptas quam sed. Voluptas!</p>
~~~

: 또한 lorem 생성자는 내포된 태그이름의 규칙을 따른다.

~~~
ul.generic-list>lorem10.item*4 [tab]

<ul class="generic-list">
  <li class="item">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur, minus!</li>
  <li class="item">Temporibus dolorum mollitia nulla porro saepe, laudantium tenetur eius iste.</li>
  <li class="item">Vitae aspernatur sunt asperiores, dignissimos atque quidem quas dolore quibusdam.</li>
  <li class="item">Cupiditate, perspiciatis laborum possimus porro asperiores fuga perferendis fugit id?</li>
</ul>
~~~
