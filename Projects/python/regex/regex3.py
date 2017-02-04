import re

s = '<html><body><h1>HTML</h1></body></html>'
m = re.match(r'<.*?>', s)
print(m.group())
