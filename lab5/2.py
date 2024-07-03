import re
file=open("row.txt","r",encoding="utf8")
text=file.read()
x=re.findall("a[b]{2,3}",text)
print(x)