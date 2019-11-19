

file="C:\\Users\\Glu\\Desktop\\KangleiIyek\\IyekListPair.txt"

import re
pattern = re.compile("^.*?ra$")

counter=0
with open("C:\\Users\\Glu\\Desktop\\KangleiIyek\\IyekListOnlyRA.txt", 'a',encoding="UTF-16") as the_file:
    with open(file, "r",encoding="UTF-16") as ins:
        for line in ins:
            counter=counter+1
            if(counter%10000==0):
                print(counter)
            line=line.replace("\n","").replace("\r","")#
            if pattern.match(line):
                the_file.write(line+"\n")


