import re  # re 모듈 불러오기


class Node(object):
    """
    HTML 태그 하나를 입력변수로 받는 클래스
    내부에 다른 클래스를 가질 수 있다.
    가장 큰 범위는 <html></html>
    """

    _pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'
    # 공백 문자를 준 이유는 html의 구조가 인덴테이션으로 되어있기 때문이다.
    # 문자열은 그룹지어 내용을 가져올 수 있게 하였고, 단어 및 비단어를 모두 가져온다.
    # 인스턴스 메소드 find_tag에서 tag라는 번수를 줄 때 위의 정규표현식에 대입할 수 있도록 했다.

    _pattern_tag_content = r'^<.*?>([.\w\W]*)<.*?>'
    # ^와 $는 문장의 시작과 끝을 명시해줘야할 단어를 찾을 때 적용한다
    # 이 경우 내용에 ?를 안썼기 때문에 끝까지 찾으므로 $를 사용하지 않아도 된다.
    # 내용에 ?를 쓰지 않으면 마지막 <.*?>를 만족하는 곳까지 모두 찾는다

    _pattern_tag_class = r'class="(.*?)"'


    def __init__(self, source):
        self.source = source

    def __str__(self):
        return '{}\n{}'.format(
            super().__str__(),
            self.source)
    """
    Node클래스를 실행하면 자동으로 초기화메서드(__init__())과 (__str__())함수가 실행된다.
    Node클래스는 객체를 생성할 때 source를 기본 인자로 주어야한다.
    __str__()함수는 Node 클래스의 객체정보와 결과같을 출력한다.
    
    """

    def find_tag(self, tag):
        """
        주어진 tag의 내용을 리턴한다.
        :param tag: 검색을 원하는 태그 - div, p, html 등등
        :param source: 태그를 검색할 전체 문자열 (example.html)
        :return: 검색할 결과가 1개이면 tag의 문자열을 오프셋 [0]으로 리턴.
        2개 이상이면 tag문자열의 리스트로 반환
        """

        pattern = re.compile(self._pattern_tag_base.format(tag=tag))
        """
        # self._pattern_tag_base.format(tag=tag)는 아래와 같다.
        r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'.format(tag=tag)
        """
        m_list = re.finditer(pattern, self.source)
        """
        finditer()함수는 re모듈의 내장함수이며, 일치한 패턴을 이터레이터(반복자)로 반환해준다.
        즉 <callable_iterator object at 0x...> 이러한 값을 호출한다.
        m_list에는 미리 컴파일한 pattern을 소스에서 찾은 결과값을 이터레이터 타입으로 할당했다.
        """
        if m_list:
            return_list = [Node(m.group()) for m in m_list]
            """
            _pattern_tag_base에서 매치되는 값들을 이터레이터로 반환한 m_list에 값이 있으면
            return_list에는 m_list의 값을 group()함수로 출력하고 Node class에 source로
            반환하여 리스트 인자로 값을 할당한다.            
            """
            return return_list if len(return_list) > 1 else return_list[0]
            """
            그리고 return_list에는 값이 1개일 경우 오프셋으로 값을 반환하고 1개 이상일 경우에는
            return_list 전체를 반환한다.
            """
        return None
        """만약 값이 없으면 None을 반환한다"""

    @property
    def content(self):
        """
        tag 문자열이 주어졌을 때 해당 tag 안의 내용을 리턴하는 메소드
        :return: 태그 안의 내용부분 
        property속성을 준 이유는 정규표현식을 할당한 클래스 변수가 protected 속성을 가지기 때문.
        """
        pattern = re.compile(self._pattern_tag_content)
        """
        pattern이라는 변수에 태그 안의 내용을 리턴하는 패턴을 미리 컴파일하여 참조한다.
        """
        m = re.search(pattern, self.source.strip())
        """
        m에는 스트링에 공백을 제거하고 pattern과 일치하는 문자열을 찾아서 반환한다. 
        """
        if m:
            return m.group(1)
        return None
        """
        만약 m값이 있으면 group함수를 사용하여 1번째 값을 찾는다.
        """

    @property
    def class_(self):
        """
        해당 Node가 가진 태그 class속성의 value를 리턴(문자열)
        ex_ <div class="content">의 'content'만 출력되게 하는 메소드
        :return: 태그 내 class속성의 value를 문자열로 리턴.
        """
        pattern = re.compile(self._pattern_tag_class)
        c = re.search(pattern, self.source.strip())
        if c:
            return c.group(1)
        return None

# ----- 실행문 --------
# source에 할당할 파일을 열고 끝나면 바로 닫는 with를 사용한다.
with open('example.html') as f:
    html = Node(f.read())    # class Node의 기본 매개변수로 source인 f.read()를 할당


node_div = html.find_tag('div')  # Node의 인스턴스인 html에 find_tag 메소드를 사용하여 tag='div'인 값을 node_div에 반환한다.
node_p_list = node_div.find_tag('p') # node_p_list는 find_tag 메소드를 사용하여 node_div에 tag='p'인 값을 가진다.
for node_p in node_p_list:     # node_p_list에 반환된 값들을 content 메소드로 반복문을 사용해 모두 출력한다.
    print(node_p.content)

print('----- class_ -----')
node_div = html.find_tag('div')
print(node_div.class_)