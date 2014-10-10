import urllib.parse
import urllib.request
import json
import time
import re

url = 'http://www.ss911.cn/Pages/admin/userinfo.aspx'

headers={
    'Connection' : 'keep-alive',
    'Cookie' : 'UserId=111700964; ',
    'Host' : 'www.ss911.cn',
    'Referer' : 'http://www.ss911.cn/Pages/login/login2.htm?v=6',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
    "":""
    }
values={}
def getInfo(uid):
    headers['Cookie']='UserId='+uid+'; '
    data = urllib.parse.urlencode(values)
    turl=url+"?"+data;
    req = urllib.request.Request(turl, None, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf8')

    
    #print(the_page)
    p=re.compile(r'<span id="bbsNickName" style="color:#f60;">(.*?)</span>')
    msp=p.search(the_page)
    tip=msp.group(1)
    print(tip)


<<<<<<< .mine
getInfo("113491719")
=======
getInfo("112594100")
>>>>>>> .r35
