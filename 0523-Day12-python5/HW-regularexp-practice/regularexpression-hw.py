import re

story = '''Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.'''

# 1
result1 = re.findall(r'\ba\w{3}\b', story)

# 2
result2 = re.findall(r'\w+r\b', story)
# 단어경계로 r 뒤에 쉼표나 점이 와도 찾는다
result3 = re.findall(r'\w*r\b', story)
# r 한글자도 찾으므로 좀더 정확하다

# 3
result4 = re.findall(r'\w*[abcde]{3}\w*', story)

# 4
# 함수만들기
def re_change(m):
    return '{}{}[{}]'.format(
        m.group('before').upper(), m.group('center'), m.group('after'))


p = re.compile(r'(?P<before>\w+)(?P<center>\s*,\s)(?P<after>\w+)', story)
result5 = re.sub(p, re_change, story)
result6 = re.sub(p, '!!!\g<before>!!!\g<center>!!!\g<after>!!!')

result = re.sub(p, m.group('before').upper() and m.group('center') and m.group('after') if p, story)
