#! /usr/bin/env python3
#coding=utf-8
import urllib.parse
import urllib.request
import json
import time
import socket
import http.cookiejar
import random
#from bs4 import BeautifulSoup

#url = 'http://api.open.baidu.com/pae/channel/data/asyncqury?cb=jQuery110209612188022583723_1405057078072&appid=4001&com=shentong&nu=768936885065&_=1405057078095'
url = 'http://api.open.baidu.com/pae/channel/data/asyncqury'
url="http://www.ss911.cn/pages/reg/regUser.aspx";

socket.setdefaulttimeout(9.0)

tNum=50003251804803;

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#district=0&hcountry=0&hprovince=0&hcity=0&hdistrict=0&online=1&ldw=360759066
values = {
          #'cb' : 'jQuery110209612188022583723_1405057078072',
          '__EVENTTARGET' : '',
          '__EVENTARGUMENT' : '',
          '__VIEWSTATE' : '/wEPDwUJMTI5NzM2MzEyZGTJPT63mQRdkB1lF1rIOYc827SVEw==',
          '__EVENTVALIDATION' : '/wEWBwLS2pi9BwLEhISACwLKw/ZKAsrDurkGAoTz/f8JApL76rYEAoznisYGfZmBFjtVdOiQx0MaX2wNedGs+4k=',
          'txtname' : 'kill011',
          'txtpass1' : 'deathnote123',
          'txtpass2' : 'deathnote123',
          'txtemail' : 'guiyank@126.com',
          'txtyzm' : 'ucva',
          'Button1' : '提交注册'
         }

values['nu']=tNum;
qqID="595912947";

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
    'Referer' : 'http://www.ss911.cn/pages/reg/regUser.aspx',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
    'X-Requested-With' : 'XMLHttpRequest'
            }
cj = http.cookiejar.CookieJar()
proxy_handler = urllib.request.ProxyHandler({'http':'183.224.1.115:80'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
displayed={};
ISOTIMEFORMAT='%Y-%m-%d %X'
def regCount(uname,sex,udName):
    getYzm()
    print('keyword:',uname)
    values["txtname"]=uname;
    yzm = input('Enter yzm: ')
    values["txtyzm"]=yzm
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    turl=url;
    req = urllib.request.Request(turl,data,headers)
    #response = urllib.request.urlopen(req)
    response = opener.open(req)
    the_page = response.read()
    rstTxt=the_page.decode('utf-8')
    
    print(cj)
    if rstTxt.find('常见问题解答')>=0:
        for cks in cj:
                print(cks.name+" "+urllib.parse.unquote(cks.value))
                if(cks.name=="uservalues"):
                  tUserValue=urllib.parse.unquote(cks.value)
        print('注册成功')
        print(uname," ",tUserValue)
        setName(udName,tUserValue,sex)
    elif rstTxt.find('IP超过了注册上限，不能注册！')>=0:
        print('IP超过了注册上限')
    else:
        print(rstTxt)
        print('注册失败')



def getYzm():
    value={"dt":"Wed Aug 27 2014 16:33:02 GMT 0800 (中国标准时间)"}
    purl="http://www.ss911.cn/pages/yzm.aspx?"+urllib.parse.urlencode(value)
    req=urllib.request.Request(purl,None,headers)

    #urllib.request.urlretrieve(req,"yzm.jpg")
    pd=opener.open(req)
    pic=pd.read()
    f=open("yzma.png","wb")
    f.write(pic);
    f.close()


def setName(tUname,uvalue,sex):
    nameValue={
        "username":tUname,
        "sex":sex,
        "uv":uvalue,
        "rd":""
        }
    nameValue['rd']=9999*random.random()
    nameValue['rd']='8468.362554495223'
    tnameUrl="http://t1.ss911.cn/User/Register.ss?"+urllib.parse.urlencode(nameValue)
    req=urllib.request.Request(tnameUrl,None)
    pd=opener.open(req)
    dd=pd.read().decode('utf-8')
    print(dd)
    if dd.find('OK')>=0:
        print('改名成功')
    else:
        yzm = input('Enter cName: ')
        setName(getNewName(tUname),uvalue,sex)
    
def getNewName(oname):
    return oname+"s"
tsname="potaa"


regCount('hhm014','0','嘿嘿')

##while(1):
##    try:
##        getInfo('630097838');
##        #break
##    except:
##        print('error')
##    time.sleep(10)





