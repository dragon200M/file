from random import choice
from string import ascii_uppercase
from string import hexdigits
import re


def generate():
    n = 10
    str = ""
    ind = ""

    for i in range(n):
        str +=  "".join(choice(ascii_uppercase))

    ind = "".join(choice(hexdigits) for n in range(6))

    return str, ind

#end def


def saveToFile(fileName , times):
    #Open file
    fo = open(fileName, "a")

    for i in range(times):
        #Append to file
        fo.write("\t".join(generate()) + "\n")
    #Close file
    fo.close()
#end def

#saveToFile("foo.okno",100)


def readFromFile(fileName):
    #Open file
    with open(fileName, 'r') as f:
        content = [[sp.strip() for sp in x.split("\t")] for x in f]
    return content
#end def


def saveBlock(variableList, outputFile):
    for i in readFromFile(variableList):
         fo = open(outputFile, 'a')
         zm = ''

         for a in i[1]:
             if a.isalpha() == False:
                 zm+=a


         list = [i[0],i[1],zm]
         fo.write( """
    IF [OPTION("{0}","{1}")] THEN
            
        IF [L1 = 6500] THEN
            SETOPTION("segment1","PPV");
            SETOPTION("segment3","{2}");
            SETOPTION("ItemType","1");
            SETOPTION("MeasurementUnit","7");
            SETNUMERICOPTION("Quantity",[L1]);
            SETOPTION("MeasurementUnit2","17");
            SETNUMERICOPTION("Quantity2",[1]);
            ENDIF
        IF [L1 < 6500 OR L1>6500] THEN
            SETOPTION("segment1","OH");
            SETOPTION("segment3","{2}");
            SETOPTION("ItemType","5");
            SETOPTION("MeasurementUnit","17");
            SETNUMERICOPTION("Quantity",[1]);
            SETOPTION("MeasurementUnit2","7");
            SETNUMERICOPTION("Quantity2",[L1]);
        ENDIF
    ENDIF
        """.format(*list))
         fo.close()

#end def

#saveBlock("foo.okno","a")


def isBalanced(expr):

    opening = set('([{')
    match = set([('(', ')'), ('[', ']'),('{','}')])
    stack = []
    for char in expr:
        if char in opening:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            lastOpen = stack.pop()
            if (lastOpen, char) not in match:
                return False
    return len(stack) == 0


def isFileOk(fileName):
    content = open(fileName, 'r')
    lista = []
    doubleP = []


    while True:
        line = content.readline()

        a = re.findall(r'"*',line)
        doubleP.append("".join(a))

        m  = re.findall(r'[(){}[\]]+', line)
        lista.append("".join(m))
        if not line:
            break

    expr = "".join(lista)
    content.close()
    check = False
    if len("".join(doubleP)) % 2 == 0:
        check = True

    return check, isBalanced(expr)





print(isFileOk('a'))