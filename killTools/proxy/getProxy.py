import re
import urllib.parse
import urllib.request
import http.cookiejar

headers = {
    #'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   #         'Accept-Encoding' : 'gzip,deflate,sdch',
  #          'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Host': 'www.cz88.net',
    #'Origin': 'http://www.ss911.cn',
    #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection' : 'keep-alive',
    'Cookie' : 'Hm_lvt_cc658daf205377fb870d72f7c9f2b59f=1409363613; Hm_lpvt_cc658daf205377fb870d72f7c9f2b59f=1409363613',
    #'Cookie' : 'RK=J5FrJKalWu; pt2gguin=o0484641127; ptcz=e9fe4398eb29335c4dd918e3326fc04dd2e294f2a7331a7abd6f39bd5faeee92; pgv_pvid=2092053654; o_cookie=484641127; uin=o484641127; skey=ZzqCm70ICM; itkn=1928745486',
    'Pragma' : 'no-cache',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153'
            }
cj = http.cookiejar.CookieJar()
#tProxy="122.232.226.195:80"
#tProxy="127.0.0.1:8080"
iprecord=0
#proxy_handler = urllib.request.ProxyHandler({'http':tProxy})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

proxyList=[]

def getProxyTxt():
    f=open("pdata.txt","r",encoding="utf-8");
    txt=f.read();
    f.close()
    return txt
def getProxyHttp(url):
    req=urllib.request.Request(url,None,headers)
    cdata=opener.open(req).read()
    #print(cdata)
    data=cdata.decode('GB2312')
    return data
def getProxyList(pTxt):
    pre=re.compile(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>whois</td><td><div class="addr_style">(.*?)</div></td></tr>')
    matches=pre.findall(pTxt)
    global proxyList
    for tP in matches:
        #print(tP)
        tip=tP[0].strip();
        tport=tP[1].strip()
        proxyList.append(tip+":"+tport)
        print(tip,":",tport)

def getProxyByUrl(url):
    print('tryget:'+url)
##    ptxt=getProxyHttp(url)
##    getProxyList(ptxt)
##    return
    try:
        ptxt=getProxyHttp(url)
        getProxyList(ptxt)
    except:
        print("fail:"+url)
    
def saveProxyFile(pList):
    f=open("pList.txt","w",encoding="utf-8");
    data="\n".join(pList)
    txt=f.write(data);
    f.close()

getProxyByUrl('http://www.cz88.net/proxy/index.aspx')

for i in range(2,11):
    getProxyByUrl('http://www.cz88.net/proxy/http_'+str(i)+'.aspx')
saveProxyFile(proxyList)
