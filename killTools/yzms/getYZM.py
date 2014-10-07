import urllib.parse
import urllib.request
opener = urllib.request.build_opener()
def getYzm(id):
    value={"dt":"Wed Aug 27 2014 16:33:02 GMT 0800 (中国标准时间)"}
    purl="http://www.ss911.cn/pages/yzm.aspx?"+urllib.parse.urlencode(value)
    req=urllib.request.Request(purl)
    print(id)

    #urllib.request.urlretrieve(req,"yzm.jpg")
    pd=opener.open(req)
    pic=pd.read()
    f=open("yzma"+str(id)+".png","wb")
    f.write(pic);
    f.close()

for id in range(100,1000):
    getYzm(id)

