#coding=utf-8

import weiboLogin
import urllib
import time

filename = 'config.txt'#保存微博账号的用户名和密码，第一行为用户名，第二行为密码
def searchWB():
    print('seachRst:')
    turl='http://s.weibo.com/weibo/%25E6%2597%25A0%25E8%2581%258A%25E5%2595%258A?topnav=1&wvr=5&b=1';
    result=urllib.request.urlopen(turl).read().decode('utf8')
    #print(result)
    f=open('wb.txt','w')
    f.write(result);
    f.close()
    print('getDone')
    
WBLogin = weiboLogin.WeiboLogin()
if WBLogin.login(filename)==1:
    print('Login success!')
    searchWB()
else:
    print('Login error!')
    #exit()


