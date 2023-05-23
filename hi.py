import re
a="张明98分"
ret=re.sub(r"\d+","100",a)
print(ret)