#! /usr/bin/env python3
#coding=utf-8
import urllib.parse
import urllib.request
import json
import time
import socket
#from bs4 import BeautifulSoup

#url = 'http://api.open.baidu.com/pae/channel/data/asyncqury?cb=jQuery110209612188022583723_1405057078072&appid=4001&com=shentong&nu=768936885065&_=1405057078095'
url = 'http://api.open.baidu.com/pae/channel/data/asyncqury'
url="http://wpa.qq.com/pa?p=2:484641127:51";

socket.setdefaulttimeout(9.0)

tNum=50003251804803;

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#district=0&hcountry=0&hprovince=0&hcity=0&hdistrict=0&online=1&ldw=360759066
values = {
          #'cb' : 'jQuery110209612188022583723_1405057078072',
          'num' : '20',
          'page' : '0',
          'sessionid' : '0',
          'keyword' : '1073810002',
          'agerg' : '0',
          'sex' : '0',
          'firston' : '1',
          'video' : '0',
          'country' : '0',
          'province' : '0',
          'city' : '0',
          'district' : '0',
          'hcountry' : '0',
          'hprovince' : '0',
          'hcity' : '0',
          'online' : '1',
          'ldw' : '360759066'
        #  'ext' : 'sourceType:'
       #   'nu' : tNum
         }

values['nu']=tNum;
qqID="595912947";

headers = {
    'Accept' : 'application/json',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Host': 'cgi.find.qq.com',
    'Origin': 'http://find.qq.com',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection' : 'keep-alive',
    'Cookie' : 'uin=o484641127; skey=ZzqCm70ICM;',
    #'Cookie' : 'RK=J5FrJKalWu; pt2gguin=o0484641127; ptcz=e9fe4398eb29335c4dd918e3326fc04dd2e294f2a7331a7abd6f39bd5faeee92; pgv_pvid=2092053654; o_cookie=484641127; uin=o484641127; skey=ZzqCm70ICM; itkn=1928745486',
    'Referer' : 'Http://find.qq.com/index.html?version=1&width=910&height=610&search_target=0',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
    'X-Requested-With' : 'XMLHttpRequest'
            }

displayed={};
ISOTIMEFORMAT='%Y-%m-%d %X'
def getInfo(words):
    print('keyword:',words)
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') 
    turl="http://wpa.qq.com/pa?p=2:"+words+":51";
    req = urllib.request.Request(turl)
    response = urllib.request.urlopen(req)
    the_page = response.read()

    print(response.url)
    tRstUrl=response.url;
    if(tRstUrl=='http://pub.idqqimg.com/qconn/wpa/button/button_111.gif'):
        tStata='在线'
    elif(tRstUrl=='http://pub.idqqimg.com/qconn/wpa/button/51_stop.gif'):
        tStata='未启用'
    else:
        tStata='离线'
    print(time.strftime( ISOTIMEFORMAT, time.localtime()))
    print(tStata)
    if(tStata=='在线'):
        print('状态：',tStata)
        f=open("qqNew.txt","a");
        f.write('\n'+'qq:{0}'.format(words));
        f.write('\n'+time.strftime( ISOTIMEFORMAT, time.localtime()));
        f.write('\n'+'状态：{0}'.format(tStata));
        f.close();
 
        

    
   
#getInfo('484641127')

while(1):
    try:
        getInfo('630097838');
        #break
    except:
        print('error')
    time.sleep(10)





