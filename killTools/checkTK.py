import urllib.parse
import urllib.request
import json
import time
import re


def getUName(uid):

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
    return tip

def getPlace(ip):
    turl='http://ip.taobao.com/service/getIpInfo.php?ip='+ip
    req = urllib.request.Request(turl)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf8')
    #print(the_page)
    data=json.loads(the_page)
    #print(data)
    if data['code']==0:
        place=data['data']
        rst=place['country']+place['region']+place['city']+place['county']+','+place['isp']
    else:
        rst='unknown'
    return rst

def getDataFromWeb(start,end):
    turl='http://sogasoga.sinaapp.com/killOnline/getCKS.php?start='+str(start)+'&end='+str(end)
    req = urllib.request.Request(turl)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf8')
    #print(the_page)
    data=json.loads(the_page)
    #print(data)
    return data

def getCookie(ckStr):
    #print(ckStr)
    cks=ckStr.split(';')
    rst={}
    for ck in cks:
        ckl=ck.split('=')
        rst[ckl[0].strip()]=ckl[1]
    return rst

def dealAUInfo(uinfo):
    
    aO={}
    aO['time']=uinfo['time']
    aO['ip']=uinfo['ip'].split(',')[0]
    cookie=getCookie(uinfo['cookie'])
    #print(cookie)
    cpValues=['UserId','UserName','UserPwd','uservalues']
    for val in cpValues:
        #print(val)
        #print(hasattr(cookie,val))
        if val in cookie:
            aO[val]=cookie[val]
    if 'UserId' in aO:
        aO['gameName']=getUName(aO['UserId'])
    if 'ip' in aO:
        aO['place']=getPlace(aO['ip'])
    #print(aO)
    return aO

def saveAll(data):
    rst=json.dumps(data)
    f=open("CKS.txt","w",encoding="utf-8")
    f.write(rst)
    #f.write(str(armo))
    f.close()

    print("save success")
    
        
    
def work(start,end):
    data=getDataFromWeb(start,end)
    #print(data)
    uinfos=data['datas']
    print(len(uinfos))
    i=0
    datas=[]
    for info in uinfos:
        i=i+1
        try:
            tO=dealAUInfo(info)
            datas.append(tO)
            print('success:',i)
        except:
            print('fail:',i,'\n',info)
        
    saveAll(datas)
        

work(30,400)


