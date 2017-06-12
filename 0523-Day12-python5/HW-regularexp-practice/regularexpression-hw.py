"""
문제 1. {m}패턴지정자를 사용해서 a로 시작하는 4글자 단어를 전부 찾는다.

문제 2. r로 끝나는 모든 단어를 찾는다.

문제 3. a,b,c,d,e중 아무 문자나 3번 연속으로 들어간 단어를 찾는다.

ex) b[eca]me


문제 4.re.sub를 사용해서 ,로 구분된 앞/뒤 단어에 대해 앞단어는 대문자화 시키고,
뒷단어는 대괄호로 감싼다. 이 과정에서, 각각의 앞/뒤에 before, after그룹 이름을 사용한다.

"""

import re


story = '''Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.'''

# 1

result1 = re.findall(r'\ba\w{3}\b', story)

"""
# 1 해설
re 임포트하여 findall함수를 사용하면 패턴에 해당되는 문자열을 리스트로 반환한다

r'\ba\w{3}\b'
단어경계(\w와 \W의 경계)를 사용하여 
a로 시작하고 \w(문자)가 {3}으로 3번 문자가 나열된다
\b는 단어 경계로, 문자와 비문자 사이, 즉 단어 끝을 말한다.
따라서 \ba가 되면 a로 시작하는 모든 단어를 찾는다
마지막에도 \b를 써서 a로 시작하는 4글자 단어만 찾도록 한다.
"""

# 2
result2 = re.findall(r'\w+r\b', story)
"""
# 2-1 해설
\w 문자가 오고 + 를 쓰면 단어 다음 공백이 올때까지 모두 선택된다
이 경우, r로 끝나는 문자를 찾으므로 r\b를 써주면 찾을 수 있다.
# 단어경계로 r 뒤에 쉼표나 점이 와도 찾는다.

"""

result3 = re.findall(r'\w*r\b', story)
"""
# 2-2 해설
위의 정규표현식과 다른 점은 *를 썼다는 것이다. 
*은 0회 이상의 최대라는 뜻인데 \w,즉, 문자열이 없는 것도 포함한다.
따라서 story 텍스트에 r 한 글자가 있다면 이것도 포함하므로 좀더 정확하다

"""


# 3
result4 = re.findall(r'\w*[abcde]{3}\w*', story)
"""
# 3 해설

\w* 은 위에서 했듯이 문자가 0~문자열끝까지 선택한다
[abcde]{3}은 a, b, c, d, e 중 1개를 선택한다는 의미이며
다시 \w*를 써줌으로써 문자열 끝까지 출력한다.

"""

# 4
# 함수만들기
def re_change(m):
    return '{}{}[{}]'.format(
        m.group('before').upper(), m.group('center'), m.group('after'))


p = re.compile(r'(?P<before>\w+)(?P<center>,\s*)(?P<after>\w+)')
result5 = re.sub(p, re_change, story)
result6 = re.sub(p, '!!!\g<before>!!!\g<center>!!!\g<after>!!!', story)
result7 = re.sub(p, lambda m: '{}, [{}]'.format(
    m.group(1).upper(),
    m.group(3)), story)

"""
# 4 해설
콤마를 기준으로 앞단어를 대문자화, 뒷단어를 대괄호로 감싸기 위해서는
그룹 이름을 붙여 패턴을 먼저 찾는다.
(?P<before>\w+)는 \w+, 즉, 문자로 구성된 문자열 1개를 찾고 before라는 이름을 붙인다.

(?P<center>,\s*)는 단어경계 다음에 오는 콤마 그리고 공백 1개를 모두 찾아 center라고 이름붙인다.
\s에 *을 쓴 이유는 공백이 1개가 아닐 경우에 다음 단어를 찾지 못하기 때문이다!!

(?P<after>\w+)는 다시 문자로 구성된 문자열 1개를 찾아 after라는 이름을 붙인 것이다.
이 3개를 동시에 나열하면 (문자열과 콤마와 공백, 그리고 문자열)로 구성된 패턴을 찾는다.
방법 1. 이 경우 함수에 그룹이름을 넣어 속성을 지정해주고 사용할 수 있다.

방법 2. sub()함수에서 패턴을 변수로 주고 인자에 g<그룹이름>형식을 사용하면 그룹이름을 매치하여 불러와 쓴다.

방법 3. sub()함수에서 lambda식을 써서 바로 구현할 수도 있다.
"""

print('========')
print(result1)
print('========')
print(result2)
print('========')
print(result3)
print('========')
print(result4)
print('========')
print(result5)
print('========')
print(result6)
print('========')
print(result7)