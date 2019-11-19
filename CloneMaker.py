import re
from operator import is_not
from functools import partial

filrdir = "C:\\Users\\Glu\\OneDrive\\Gutenberg\\merit_list\\YumnakRaw.txt"
filrdirwrite = "C:\\Users\\Glu\\OneDrive\\Gutenberg\\merit_list\\YumnakFinal.txt"

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


with open(filrdirwrite, 'a') as the_file:
    with open(filrdir) as f:
        for line in f:
            line = line.replace("\n", "").replace("\r", "").lower()
            for string in array:
                if string in line:
                    splited = re.split(regexsplit, line)
                    splited = list(filter(None.__ne__, splited))
                    print(splited)
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
                for yumnakname in allposibleyunak:
                    the_file.write(yumnakname + "\n")
            print(line)
