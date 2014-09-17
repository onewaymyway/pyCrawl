import urllib.parse
import urllib.request
import json
import time
import re

url = 'http://t1.ss911.cn/User/TradeBuyLog_p.ss'
url = 'http://t1.ss911.cn/User/TradeSaleLog_p.ss'
url = 'http://t1.ss911.cn/User/TradeBack_p.ss'
url='http://t1.ss911.cn/User/UserBuylog_p.ss'

urls=[
    'http://t1.ss911.cn/User/TradeBuyLog_p.ss',
    'http://t1.ss911.cn/User/TradeSaleLog_p.ss',
    'http://t1.ss911.cn/User/TradeBack_p.ss',
    'http://t1.ss911.cn/User/UserBuylog_p.ss',
    'http://t1.ss911.cn/User/UseToollog_p.ss',
    'http://t1.ss911.cn/User/UseTome_p.ss'
      ]
headers={
    'Connection' : 'keep-alive',
    'Cookie' : 'uservalues=;  ',
    'Host' : 't1.ss911.cn',
    'Referer' : 'http://www.ss911.cn/Pages/login/login2.htm?v=6',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
    "":""
    }
values={
    'beginDate':'2013-09-10',
    'endDate':'2014-09-17'
    }
def getInfo(uid):
    headers['Cookie']='uservalues='+getGoodUV(uid)+'; '
    for url in urls:
        getInfoR(url)


def getInfoR(typeUrl):
    try:
        data = urllib.parse.urlencode(values)
        turl=typeUrl+"?"+data;
        req = urllib.request.Request(turl, None, headers)
        response = urllib.request.urlopen(req)
        the_page = response.read().decode('utf8')
        print(the_page)
    except:
        print('fail:'+typeUrl)
##    p=re.compile(r'<span id="bbsNickName" style="color:#f60;">(.*?)</span>')
##    msp=p.search(the_page)
##    tip=msp.group(1)
##    print(tip)

def getGoodUV(value):
    return urllib.parse.quote_plus(value)

while 1:
    uv=input('uvalue:')
    getInfo(uv)

