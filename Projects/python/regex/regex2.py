import re
story = '''Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.'''


r = re.findall('Lux', story)
r = re.findall('Lux|her|she', story)
#r = re.findall('[Ll]ux|[Hh]er|[Ss]he', story)
r = re.findall('^Born', story)
r = re.findall('^Lux', story)
r = re.findall('Demacia$', story)
r = re.findall('Demacia\.$', story)
r = re.findall('was', story)
r = re.findall('\w+(?<=she) was', story)
r = re.findall('\w+\s?was', story)
r = re.findall('\w+(?<![Ss]he) was', story)
r1 = re.findall('\bwas\b', story)
r2 = re.findall(r'\bwas\b', story)
#print(r1)
#print(r2)

source1 = 'no class at all'
source2 = 'the declassified algorithm'
p1 = re.compile(r'\bclass\b')
p2 = re.compile(r'\w*\Bclass\B\w*')

#print(re.search(p1, source1))
##print(re.search(p1, source2))

#print(re.search(p2, source1))
#print(re.search(p2, source2))

s = re.search(r'\w+\s*(was)', story)
print(s.groups())
print(s.group(0))
print(s.group(1))

s = re.findall(r'(\w+)\s*was', story)
print(s)

m_list = re.finditer(r'(?P<before>\w+)\s+(?P<was>was)\s+(?P<after>\w+)', story)

for m in m_list:
    print(m.groups())
    print(m.group('before'))
    print(m.group('was'))
    print(m.group('after'))
    print('--')



