
def getDicArr(dic):
    rst=[]
    for ct in dic:
        rst.append(ct)
    return rst

def getProxys(of):
    f=open(of,"r",encoding="utf-8")
    nips={}
    for line in f.readlines():
        tline=line.strip()
        if tline in nips:
            continue
        nips[tline]=1
    f.close()
    return nips

def adptProxy(of,tf):
    proxys=getDicArr(getProxys(of))
    print('proxyCount:',len(proxys))
    f=open(tf,"w",encoding="utf-8")
    ct='\n'.join(proxys)
    f.write(ct)
    f.close()

#adptProxy('ipsn.txt','ipadt1.txt')
adptProxy('proxyTotal.txt','proxyLib.txt')
#adptProxy('apiProxy1.txt','apiproxyLib.txt')
    
    

