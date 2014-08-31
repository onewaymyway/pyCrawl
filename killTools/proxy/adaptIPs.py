


def getProxys():
    f=open("ips.txt","r",encoding="utf-8")
    nips=[]
    for line in f.readlines():
        tline=line.strip()
        if tline in nips:
            continue
        nips.append(tline)
    f.close()
    return nips

proxys=getProxys()
print('proxyCount:',len(proxys))
f=open("ipadt.txt","w",encoding="utf-8")
ct='\n'.join(proxys)
f.write(ct)
f.close()
