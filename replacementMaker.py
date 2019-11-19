
fileKok="C:\\Users\\Glu\\Desktop\\KangleiIyek\\kok.txt"
onlyfileKok="C:\\Users\\Glu\\Desktop\\KangleiIyek\\onlykok.txt"
filecheitap="C:\\Users\\Glu\\Desktop\\KangleiIyek\\cheitap.txt"
filelonsum="C:\\Users\\Glu\\Desktop\\KangleiIyek\\lonsum.txt"
filerar="C:\\Users\\Glu\\Desktop\\KangleiIyek\\rar.txt"
# filesample="C:\\Users\\Glu\\Desktop\\KangleiIyek\\sample.txt"
filesample="C:\\Users\\Glu\\Downloads\\Telegram Desktop\\FinalAll.txt"

filesigna="C:\\Users\\Glu\\Desktop\\KangleiIyek\\signa.txt"


def read(arg:str):
    with open(arg, 'r',encoding="UTF-16") as content_file:
        return content_file.read()



print()
print(read(filecheitap))

kok=read(fileKok).split(":")
kokpair=[]

for elem in kok:
    wp=elem.split("=")
    kokpair.append(wp)
onlykok=read(onlyfileKok).split(":")

onlykokpair=[]
for elem in onlykok:
    wp=elem.split("=")
    onlykokpair.append(wp.copy())
print(onlykokpair)

lonsum=read(filelonsum).split(":>")
onlylonsum=[]
for elem in lonsum:
    wp=elem.split("=")
    onlylonsum.append(wp.copy())
    kokpair.append(wp)
print(kokpair)

cheitap=read(filecheitap).split(":")
cheitappair=[]
for elem in cheitap:
    wp=elem.split(">=")
    cheitappair.append(wp)

print(cheitappair)

rartap=read(filerar).split(":")
rarpair=[]
for elem in rartap:
    wp=elem.split("=")
    rarpair.append(wp)

print(rarpair)

#mixure maker
mixurepair=[]
for kokelm in kokpair:
    for cheitapelm in cheitappair:
        apun=kokelm[0]+cheitapelm[0]
        if kokelm[0]=="ꯑ":
            apuneng=cheitapelm[1]
        else:
            apuneng=kokelm[1]+cheitapelm[1]
        # apuneng = kokelm[1] + cheitapelm[1]
        mixurepair.append([apun,apuneng])

print(mixurepair)

signa = read(filesigna).split(":")
signapair=[]
for signelm in signa:
    signapair.append(signelm.split("="))

print(signapair)


############################################################
import re
def gettrasliterate(ele:str):
    for rarelem in rarpair:
        ele=re.sub(rarelem[0]+'$', rarelem[1], ele)
    for mixelm in mixurepair:
        ele = ele.replace(mixelm[0], mixelm[1])
    for chtp in cheitappair:
        ele = ele.replace(chtp[0], chtp[1])
    for lnsm in onlylonsum:
        ele = ele.replace(lnsm[0], lnsm[1])
    for kk in onlykokpair:
        ele = ele.replace(kk[0], kk[1])
    for sig in signapair:
        ele = ele.replace(sig[0], sig[1])
    return ele.replace("∆","")#repalcing "apun"
#################################################################

sample=read(filesample).split("\n")

counter=0
with open("C:\\Users\\Glu\\Desktop\\KangleiIyek\\IyekListPair.txt", 'a',encoding="UTF-8") as the_file:
    for myele in sample:
        myele=myele.replace("\n","").replace("\r","")
        counter=counter+1
        if(counter%10000==0):
            print(counter)
            # break
        the_file.write(myele + "-->" + gettrasliterate(myele)+"\n")