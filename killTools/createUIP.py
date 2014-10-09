

f=open("ips.txt","r",encoding="utf-8");
ipList=[]
for line in f.readlines():
    tline=line.strip()
    if tline.find(',')<0:
        tip=tline
    else:
        tip=tline.split(',')[0]
    if len(tip)>1:
        ipList.append(tip)
f.close()
ttxt=','.join(ipList)
print(ipList)
f=open("ipsForK.txt","w",encoding="utf-8");
f.write(ttxt)
f.close()
