import json

f=open("rgd.txt","r",encoding="utf-8")
tList=[]
tLList=[]
for line in f.readlines():
    if line.find(',')>0:
        line=line.strip()
        cls=line.split(",")
        tuser={}
        tuser["uname"]=cls[3]
        tuser['uv']=cls[4]
        if len(cls[1])>12:
            tLList.append(tuser)
        else:
            tList.append(tuser)
        
    else:
        pass
f.close()

def createArmy(pList):
    armyList=[]
    print('solder:',len(pList))
    for i in range(0,int(len(pList)/20)):
        tlist=pList[i:i+20]
        armyO={}
        armyO['names']=tlist
        armyO['aname']="卫队"
        armyO['roomName']="卫队操练"
        armyList.append(armyO)
    print('arms:\n','num:',len(armyList),'\n',armyList)
    return armyList

def createNewArmy(pList):
    armyO={}
    armyO['leades']=pList[0:5]
    armyO['solders']=pList[5:len(pList)]
    armyO['aname']='卫队'
    armyO['roomName']='禁首房主'
    return armyO
    
print('goodPlayers:\n',tList)
print('badPlayers:\n',tLList)
armo=createArmy(tLList[1:21])
armo=createNewArmy(tLList)
f=open("myArmy.txt","w",encoding="utf-8")
f.write(json.dumps(armo))
#f.write(str(armo))
f.close()

print(tLList[1:2])
print(tLList[2:3])
