#! /usr/bin/env python3
#coding=utf-8
import urllib.parse
import urllib.request
import json
import time

#url = 'http://api.open.baidu.com/pae/channel/data/asyncqury?cb=jQuery110209612188022583723_1405057078072&appid=4001&com=shentong&nu=768936885065&_=1405057078095'
url = 'http://api.open.baidu.com/pae/channel/data/asyncqury'
#url="http://www.sina.com";



tNum=50003251804803;

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
          #'cb' : 'jQuery110209612188022583723_1405057078072',
          'cb' : '',
          'appid' : '4001',
          'com' : 'huitongkuaidi',
          '_' : '1405057078095',
          'nu' : tNum
         }

values['nu']=tNum;
qqID="595912947";
headers = {
    #'Accept' : 'application/json, text/javascript, */*',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
            'Connection' : 'keep-alive',
            'Cookie' : 'BAIDUID=7170C3CF8F0F6FD2C332BD18B3A3788A:FG=1; BDUSS=mhWY2ljOWkwZFEzVUh4QmFoT3BRUmtSazl0eG1JWkt3UHZORXYtSk9iNm8wV0ZUQVFBQUFBJCQAAAAAAAAAAAEAAAAPP~YDtaXX1sH3w6UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKhEOlOoRDpTd; MCITY=-%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=7556_7509_1466_7571_5223_6997_7599_7540_7532_7443_6506_7592_6017_7203_6930_7468_7253_7133_7584_7415_7475',
            'Host' : 'api.open.baidu.com',
            'Referer' : 'http://www.baidu.com/s?wd=%E5%BF%AB%E9%80%92%E5%8D%95%E5%8F%B7%E6%9F%A5%E8%AF%A2&rsv_spt=1&issp=1&rsv_bp=0&ie=utf-8&tn=baiduhome_pg&rsv_sug3=10&rsv_sug4=525&rsv_sug1=10&oq=%E5%BF%AB%E9%80%92%E5%8D%95%E5%8F%B7&rsv_sug2=1&f=3&rsp=0&inputT=4158',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
            'X-Requested-With' : 'XMLHttpRequest'
            }


def getInfo(tNum):
    values['nu']=tNum;
    data = urllib.parse.urlencode(values)
    turl=url+"?"+data;
    req = urllib.request.Request(turl, None, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    #f=open("qq.data","wb");
    #f.write(the_page);
    #f.close();
    tStr=the_page.decode("utf8")
    #print(tStr)
    jsonData=json.loads(tStr);
    tStatu=jsonData["status"];
    #print(tStatu);
    if(tStatu!="0"):
        print("fail:",tStatu);
        print(jsonData);
        return

    #print(jsonData['data']['info']['context'])
    ways=jsonData['data']['info']['context']
    for datas in ways:
        print(datas)

for i in range(0,20):
    print("info:",i)
    getInfo(tNum+i)
    time.sleep(10)



