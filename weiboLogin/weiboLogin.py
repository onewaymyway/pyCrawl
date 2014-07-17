#coding=utf-8
import sys
import urllib.parse
import urllib.request
import http.cookiejar 
import base64
import re
import json
import hashlib
import rsa
import binascii

class WeiboLogin:
        
    
    def __init__(self):
        
        cookie = http.cookiejar.CookieJar()                                        #保存cookie，为登录后访问其它页面做准备
        cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)             
        opener = urllib.request.build_opener(cjhdr)
        urllib.request.install_opener(opener)
	#print('initfun')
    def get_servertime(self,username):
        print('get_servertime')
        url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=&su=%s&rsakt=mod&client=ssologin.js(v1.4.4)' % username
        data = urllib.request.urlopen(url).read().decode('utf8')
        p = re.compile('\((.*)\)')
        print('data:',data)
        try:
                #json_data = p.search(data).group(1)
                json_data = json.loads(data)
                print('js:',data)
                servertime = str(json_data['servertime'])
                nonce = json_data['nonce']
                pubkey = json_data['pubkey']
                rsakv = json_data['rsakv']
                return servertime, nonce, pubkey, rsakv
        except:
                print ('Get severtime error!')
                return None

    def get_pwd(self, password, servertime, nonce, pubkey):
        rsaPublickey = int(pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537)
        #创建公钥
        message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
        passwd = rsa.encrypt(message.encode(), key)
        #加密
        passwd = binascii.b2a_hex(passwd)
        #将加密信息转换为16进制。
        return passwd

    def get_user(self, username):
        username_ = urllib.request.quote(username).encode()
        username = base64.encodestring(username_)[:-1]
        return username
    def get_account(self,filename):
        f=open(filename,'r')
        flag = 0
        for line in f:
            if flag == 0:
                username = line.strip()
                flag +=1
            else:
                pwd = line.strip()
        f.close()
        return username,pwd
    def login(self,filename):
                
        username,pwd = self.get_account(filename)
        print('uname:'+username+' pwd:'+pwd)


        url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.4)'
        try:
            servertime, nonce, pubkey, rsakv = self.get_servertime(username)
            print(servertime)
            print(nonce)
            print(pubkey)
            print(rsakv)
        except:
            print('get servertime error!')
            return
        postdata = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'userticket': '1',
        'ssosimplelogin': '1',
        'vsnf': '1',
        'vsnval': '',
        'su': '',
        'service': 'miniblog',
        'servertime': '',
        'nonce': '',
        'pwencode': 'rsa2',
        'sp': '',
        'encoding': 'UTF-8',
        'prelt': '115',
        'rsakv': '',
        'url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
        }
        postdata['servertime'] = servertime
        postdata['nonce'] = nonce
        postdata['rsakv'] = rsakv
        postdata['su'] = self.get_user(username)
        postdata['sp'] = self.get_pwd(pwd, servertime, nonce, pubkey)
        tpostdata = urllib.parse.urlencode(postdata).encode('utf-8')
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0 Chrome/20.0.1132.57 Safari/536.11'
            }
        req = urllib.request.Request(url, tpostdata, headers)
        result = urllib.request.urlopen(req)
        text = result.read().decode('gbk')
        print(text)
        p = re.compile('location\.replace\(\'(.*)\'\)')
        #此处和之前略有区别，小心！
        try:
            login_url = p.search(text).group(1)
            #print login_url
            result=urllib.request.urlopen(login_url)
            for kk in result:
                print(kk)
            print(result)
            print("Login success!")
            return 1
        except:
            print('Login error!')
            return 0
