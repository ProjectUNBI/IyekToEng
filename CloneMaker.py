import re
from operator import is_not
from functools import partial

filrdir = "C:\\Users\\Glu\\Desktop\\KangleiIyek\\IyekListOnlyFinalAndJoined.txt"
filrdirwrite = "C:\\Users\\Glu\\Desktop\\KangleiIyek\\IyekListOnlyFinalAndJoinedCloned.txt"

array = ["sh", "s", "f","bh","v","ll","pp","nn","mm","ll","kk","tt","ngng"]
regexsplit = "(sh)|(s)|(f)|(bh)|(v)|(ll)|(pp)|(nn)|(mm)|(ll)|(kk)|(tt)|(ngng)"  # dont preced "sh" by "s" and similar


def checkit(param: str):
    for line in array:
        if (line == param):
            return True
    return False


def makecobi(myfpart, myarray: array):
    cparray = myarray.copy()
    del cparray[0]
    arrycombi = []
    returnablearray = []
    for newnum in range(0, len(myarray[0])):
        if (len(myarray) > 1):
            fpart = myarray[0][newnum]
            arrycombi = arrycombi + makecobi(fpart, cparray)
        else:
            arrycombi = myarray[0]
    for line in arrycombi:
        returnablearray.append(myfpart + line)
    return returnablearray


def getposiblecombination(arrayble: array):
    cparray = arrayble.copy()
    del cparray[0]
    rrycombi = []
    for newnum in range(0, len(arrayble[0])):
        fpart = arrayble[0][newnum]
        rraycombi = rrycombi + makecobi(fpart, cparray)
    return rraycombi

counter=0
with open(filrdirwrite, 'a',encoding="UTF-16") as the_file:
    with open(filrdir,encoding="UTF-16") as f:
        for line in f:
            counter=counter+1
            if(counter%10000==0):
                print(counter)
            splitedme = line.replace("\n", "").replace("\r", "").lower().split("-->")
            line=splitedme[1]
            newline=""
            for string in array:
                splited = re.split(regexsplit, line)
                if len(splited)>1:
                    splited = list(filter(None.__ne__, splited))
                    # print(splited)
                    arrayble = []
                    for int in range(0, len(splited)):
                        iswhaiwan = checkit(splited[int])
                        if iswhaiwan:
                            if splited[int] == "s" or splited[int] == "sh":
                                arrayble.append(["s", "sh"])
                            if splited[int] == "f":
                                arrayble.append(["ph", "f"])
                            if splited[int] == "bh" or splited[int] == "v":
                                arrayble.append(["bh", "v"])
                            if splited[int] == "ll" :
                                arrayble.append(["l", "ll"])
                            if splited[int] == "pp" :
                                arrayble.append(["pp", "p"])
                            if splited[int] == "nn" :
                                arrayble.append(["nn", "n"])
                            if splited[int] == "mm" :
                                arrayble.append(["mm", "m"])
                            if splited[int] == "ll" :
                                arrayble.append(["l", "ll"])
                            if splited[int] == "kk" :
                                arrayble.append(["k", "kk"])
                            if splited[int] == "tt" :
                                arrayble.append(["t", "tt"])
                            if splited[int] == "ngng" :
                                arrayble.append(["ng", "ngng"])
                        else:
                            arrayble.append([splited[int]])
                    allposibleyunak = getposiblecombination(arrayble)
                else:
                    allposibleyunak=[line]
                break
            for yumnakname in allposibleyunak:
                # print(splitedme[0]+"-->"+yumnakname )
                the_file.write(splitedme[0]+"-->"+yumnakname + "\n")
                # break
            # print(line)
            # break
