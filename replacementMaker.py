import os
import sys

fileKok = os.path.normcase('./KangleiIyek/kok.txt')
onlyfileKok=os.path.normcase('./KangleiIyek/onlykok.txt')
filecheitap=os.path.normcase('./KangleiIyek/cheitap.txt')
filelonsum=os.path.normcase('./KangleiIyek/lonsum.txt')
filerar=os.path.normcase('./KangleiIyek/rar.txt')
filesample=os.path.normcase('./KangleiIyek/FinalAllRsnd.txt')
filesigna=os.path.normcase('./KangleiIyek/signa.txt')

def read(arg:str):
    with open(arg, 'r',encoding="UTF-16") as content_file:
        return content_file.read()

# print()
# print(read(filecheitap))

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
# print(onlykokpair)

lonsum=read(filelonsum).split(":>")
onlylonsum=[]
for elem in lonsum:
    wp=elem.split("=")
    onlylonsum.append(wp.copy())
    kokpair.append(wp)
# print(kokpair)

cheitap=read(filecheitap).split(":")
cheitappair=[]
for elem in cheitap:
    wp=elem.split(">=")
    cheitappair.append(wp)

# print(cheitappair)

rartap=read(filerar).split(":")
rarpair=[]
for elem in rartap:
    wp=elem.split("=")
    rarpair.append(wp)

# print(rarpair)

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

# print(mixurepair)

signa = read(filesigna).split(":")
signapair=[]
for signelm in signa:
    signapair.append(signelm.split("="))

# print(signapair)


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

counter = 0
data = set()

with open(filesample, encoding='utf-8') as f:
    for l in f.readlines():
        data.add(l.replace('\n', ''))

dc = 0
dataset = ''
for w in data:
    # dataset += w + '\n'
    
    if ((counter + 1) % 10000) == 0:
        with open('data/data-{}.txt'.format(dc), 'w') as f:
            f.write(dataset)
            dataset = ''
            dc += 1
    
    s = '{} - {}'.format(gettrasliterate(w), w)
    dataset += s + '\n'
    sys.stdout.write("\r%d" % counter)
    sys.stdout.flush()    
    counter += 1

# with open(filesample, 'w') as f:
#     f.write(dataset)

# with open('data.txt', 'w') as f:
#     f.write(dataset)
