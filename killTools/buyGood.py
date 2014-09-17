import urllib.parse
import urllib.request
import json
import time
import socket
import http.cookiejar
import random
import re

url="http://t1.ss911.cn/Shop/Buy.ss";

socket.setdefaulttimeout(19.0)
values = {
          'u' : 'xiKB1WCdEeOlklg+dKsBw8yndrMGjgFN',
          'tu' : '1549754',
          'b' : 'tool:167:1'
         }


headers = {
    'Accept' : 'application/json',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Host': 'www.ss911.cn',
    'Origin': 'http://www.ss911.cn',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection' : 'keep-alive',
    'Cookie' : 'lzstat_uv=27536272562782932456|264585; lzstat_ss=2912218113_0_1409145144_264585;ASP.NET_SessionId=sbskuxue4ljgl2552xvm5b55',
    #'Cookie' : 'RK=J5FrJKalWu; pt2gguin=o0484641127; ptcz=e9fe4398eb29335c4dd918e3326fc04dd2e294f2a7331a7abd6f39bd5faeee92; pgv_pvid=2092053654; o_cookie=484641127; uin=o484641127; skey=ZzqCm70ICM; itkn=1928745486',
    'Referer' : 'http://t1.ss911.cn/killonline.swf',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
    'X-Requested-With' : 'XMLHttpRequest'
            }
cj = http.cookiejar.CookieJar()
tProxy="222.66.115.233:80"
#tProxy="127.0.0.1:8080"
iprecord=0
proxy_handler = urllib.request.ProxyHandler({'https':tProxy})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)

def buy():
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    turl=url;
    req = urllib.request.Request(turl,data)
    #response = urllib.request.urlopen(req)
    response = opener.open(req)
    the_page = response.read().decode('utf-8')
    print(the_page)
def buyN():
    valuess={
        'u' : 'xiKB1WCdEeOlklg+dKsBw8yndrMGjgFN',
        'tid' : '966402',
        'gp' : '',
        'gn' : '1'
        }
    data = urllib.parse.urlencode(valuess)
    data = data.encode('utf-8')
    turl="http://t1.ss911.cn/Trade/BuyGoods.ss";
    req = urllib.request.Request(turl,data)
    #response = urllib.request.urlopen(req)
    response = opener.open(req)
    the_page = response.read().decode('utf-8')
    print(the_page)
buyN();
