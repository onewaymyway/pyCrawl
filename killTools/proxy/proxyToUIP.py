import urllib.parse
import urllib.request
import json
import time
import socket
import http.cookiejar
import random
import re

socket.setdefaulttimeout(10.0)

headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Host': 'www.ss911.cn',
    'Origin': 'http://www.ss911.cn',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection' : 'keep-alive',
    'Cookie' : 'lzstat_uv=27536272562782932456|264585; lzstat_ss=2912218113_0_1409145144_264585;ASP.NET_SessionId=sbskuxue4ljgl2552xvm5b55',
    #'Cookie' : 'RK=J5FrJKalWu; pt2gguin=o0484641127; ptcz=e9fe4398eb29335c4dd918e3326fc04dd2e294f2a7331a7abd6f39bd5faeee92; pgv_pvid=2092053654; o_cookie=484641127; uin=o484641127; skey=ZzqCm70ICM; itkn=1928745486',
    'Referer' : 'http://www.ss911.cn/Pages/login/login2.htm',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
    'X-Requested-With' : 'XMLHttpRequest'
            }
values = {
          'user' : 'shade372',
          'pass' : 'shade372',
          'code' : ''
         }
cj = http.cookiejar.CookieJar()
tProxy="222.66.115.233:80"
#tProxy="127.0.0.1:8080"
iprecord=0
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def setProxy(proxy):
    global opener
    global tProxy
    tProxy=proxy
    cj = http.cookiejar.CookieJar()
    proxy_handler = urllib.request.ProxyHandler({'http':tProxy})
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)

def login():
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request("http://www.ss911.cn/Pages/login/login2.aspx",data,headers)
    opener.open(req)
    
def getUIP():
    turl="http://t1.ss911.cn/Index.ss"
    req=urllib.request.Request(turl,None)
    pd=opener.open(req)
    dd=pd.read().decode('utf-8')
    getIPV(dd)

def getIPV(txt):
    p=re.compile(r'fv.userip="(.*?)";')
    msp=p.search(txt)
    tip=msp.group(1)
    tip=urllib.parse.unquote(tip)
    print("ip:"+tip," "+tProxy)
    f=open("ips.txt","a",encoding="utf-8")
    f.write(tip+","+tProxy+"\n")
    f.close()

def getUipByProxy(proxy):
    setProxy(proxy)
    login()
    getUIP()

def getProxys():
    f=open("pList.txt","r",encoding="utf-8")
    proxyList=[]
    for line in f.readlines():
        line=line.strip()
        if line.find(':')>=0:
            proxyList.append(line)
    return proxyList

def beginWork():
    proxys=getProxys()
    print('proxys:',len(proxys))
    for proxy in proxys:
        print('try:',proxy)
        try:
            getUipByProxy(proxy)
            print('success')
            f=open("goodProxy.txt","a",encoding="utf-8")
            f.write(proxy+"\n")
            f.close()
        except:
            print('fail')
        
beginWork()
