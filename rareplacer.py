

file="C:\\Users\\Glu\\Desktop\\KangleiIyek\\IyekListPair.txt"
replacible="C:\\Users\\Glu\\Desktop\\KangleiIyek\\IyekListOnlyRA.txt"



def read(arg:str):
    with open(arg, 'r',encoding="UTF-16") as content_file:
        return content_file.read()

repalcible=read(replacible).split("\n")
rplacearry=[]
for str in repalcible:
    if("-->" in str):
        str=str.replace("\n","").replace("\r","")
        split=str.split("-->")
        rplacearry.append(split)
counter=0
import re
pattern = re.compile("^.*?ra$")

with open("C:\\Users\\Glu\\Desktop\\KangleiIyek\\IyekListOnlyFinalAndJoined.txt", 'a',encoding="UTF-16") as the_file:
    with open(file, "r",encoding="UTF-16") as ins:
        for line in ins:
            counter=counter+1
            if(counter%10000==0):
                print(counter)
            line=line.replace("\n","").replace("\r","")#
            the_file.write(line + "\n")
            if pattern.match(line):
                for pairmap in rplacearry:
                    if (pairmap[0] in line):
                        the_file.write(pairmap[0] + "-->" + pairmap[1] + "\n")
                        break
                else:
                    continue





