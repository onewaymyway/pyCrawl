import re
import urllib.parse

f=open("indextp.txt","r",encoding="utf-8");
txt=f.read()
f.close()
p=re.compile(r'fv.userip="(.*?)";')
msp=p.search(txt)
tip=msp.group(1)
tip=urllib.parse.unquote(tip)
print(tip)

