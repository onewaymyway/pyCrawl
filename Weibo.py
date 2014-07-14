#! /usr/bin/env python3
#coding=utf-8
import urllib.parse
import urllib.request
import json
import time
from bs4 import BeautifulSoup

#url = 'http://api.open.baidu.com/pae/channel/data/asyncqury?cb=jQuery110209612188022583723_1405057078072&appid=4001&com=shentong&nu=768936885065&_=1405057078095'
url = 'http://api.open.baidu.com/pae/channel/data/asyncqury'
url="http://m.weibo.cn/page/pageJson";



tNum=50003251804803;

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
          #'cb' : 'jQuery110209612188022583723_1405057078072',
          'containerid' : '100103type=2&q=我去啊',
          'format' : 'json',
          'page' : '1',
          'wm' : 'ig_1002',
          'from' : 'home',
          'rl' : '50',
          'uicode' : '10000011',
          'fid' : '100103type=2&q=我去啊',
          'ext' : 'sourceType:'
       #   'nu' : tNum
         }

values['nu']=tNum;
qqID="595912947";

headers = {
    'Accept' : 'application/json',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
            'Connection' : 'keep-alive',
            'Cookie' : '_T_WM=9e383d2d3eb5730f460f71f7e880a642; USER_LAST_LOGIN_NAME=danziliumang%40sina.com; SUB=AWqPqpkbilGkxSzkTRYXMVKNVizyLexr0%2FAfAVE3f57AitHfTIKLNsrbGtvt8DCiT0%2B5lxC5F9J7hPZnMIprG1RQ6JlMpAyyDaeA%2BaJZw4QbGk57hJ2MRQUOCamCelcW%2B7K%2F%2FVTkH8cLaYDhKMBoRk8%3D; gsid_CTandWM=4uX227761VP22c9sRwqKL595gdJ; _TTT_USER_CONFIG_H5=%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A10%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D; WEIBOCN_WM=ig_1002',
            'Host' : 'm.weibo.cn',
            'Referer' : 'ttp://m.weibo.cn/main/pages/index?containerid=100103type%3D2%26q%3D%E6%88%91%E5%8E%BB%E5%95%8A&queryVal=%E6%88%91%E5%8E%BB%E5%95%8A&type=wb&wm=ig_1002&from=home&rl=12&title=%E6%88%91%E5%8E%BB%E5%95%8A',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153',
            'X-Requested-With' : 'XMLHttpRequest'
            }

displayed={};

def getInfo(words):
    values['containerid']='100103type=2&q='+words;
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
    #tStatu=jsonData["status"];
    #print(jsonData);
    soup=BeautifulSoup(jsonData['tpl'])
    #print(soup)
    tests=soup.findAll('article','wrapper-wb BgCLev5 BCLev5 J-feed')
    print('results:')
    #print(tests)

    for tTxt in tests:
       print('id：'+tTxt['data-id'])
       
       did=tTxt['data-id']
       if did in displayed:
          continue

       print('uid:'+tTxt['data-uid'])
       tname=tTxt.find('span','FCLev6 nikename-wb')
       print(tname.string);
       contents=tTxt.find('section','content-wb')
       #print(contents.p)
       tp=contents.p;
       for kk in tp:
           #
           print(kk.string)

       displayed[did]=did



for i in range(0,1000):
    print("info:",i)
    getInfo('大姨妈')
    time.sleep(30)



