import os
import time
from random import randrange
import sys
sys.setrecursionlimit(10**8)

# Initialize lists and int
varName = []; varValue = []
currentLine = 0
totalLine = 'initialize'
counterofstuff = 0

def skipif(inputfile):
    global currentLine, totalLine
    open_file = open(inputfile, 'r')
    counter2 = 0
    everyline = []
    for everyline1 in open_file:
        everyline1.rstrip()
        everyline.append(everyline1)
    for i in everyline[currentLine:]:
        testwords1 = i.split()
        try: comment = testwords1[0]
        except IndexError: comment = 0
        else:
            words1 = i.split()
            if words1[0] == ")": break
        counter2 += 1
    currentLine += counter2

def callfile(words, varName, varValue, inputfile):
    global currentLine, fromfile
    newwords = ' '.join([str(elem) for elem in words[1:]])
    oldcurrentLine = int(currentLine + 1); currentLine = 0
    oldfromfile = fromfile; fromfile = 1    
    while True:
        num_lines = sum(1 for amountofline in open(newwords))
        if num_lines <= currentLine:
            currentLine = oldcurrentLine
            fromfile = oldfromfile
            if fromfile == 0:
                Console()
            elif fromfile == 1:
                Runner(inputfile)
        open_file = open(newwords, 'r')
        counter2 = 0
        for i in open_file:
            if counter2 == currentLine:
                totalLine = i
                break
            else: counter2 += 1
        words = totalLine.split()
        # Find and replace with var values
        allcomments = ["#", "::", "//"]
        for i in allcomments:
            commentloop = 1
            for elem in words[1:]:
                if i in elem: words = words[0:commentloop]
                commentloop+=1
        word_counter = 0
        for elem in varName:
            elem = "["+elem+"]"
            loopcounter = 0
            for item in words:
                if elem in item: words[loopcounter] = item.replace(elem, str(varValue[word_counter]))
                if "&" in item: words[loopcounter] = item.replace("&", " ")
                loopcounter+=1
            word_counter += 1
        
        try: comment = words[0]
        except IndexError: comment = 0
        else: commands(varName, varValue, words, inputfile)
        currentLine+=1

def commands(varName, varValue, words, inputfile):
    global currentLine, totalLine, fromfile
    if words[0].lower() == "say" or words[0].lower() == "print" or words[0].lower() == "echo":
        say = ' '.join([str(elem) for elem in words[1:]])
        print(str(say))
    elif words[0].lower() == "say." or words[0].lower() == "print." or words[0].lower() == "echo.": print("")
    elif "#" in words[0].lower() or "label" in words[0].lower() or "(" == words[0] or ")" in words[0] or "::" in words[0].lower() or "//" in words[0].lower(): comment = 0 # Comment
    elif words[0].lower() == "cmd":
        bat = ' '.join([str(elem) for elem in words[1:]])
        os.system(str(bat))
    elif words[0].lower() == "quit": exit()
    elif words[0].lower() == "write.file":
        writefile = ''.join([str(elem) for elem in words[1]])
        writecontents = ' '.join([str(elem) for elem in words[2:]])
        with open(writefile, 'a+') as filehandle:
            filehandle.write(writecontents+'\n')
    elif words[0].lower() == "call": callfile(words, varName, varValue, inputfile)
    elif "#" in words[0].lower() or "::" in words[0].lower() or "//" in words[0].lower(): comment = 0
    elif words[0].lower() == "write":
        write = ' '.join([str(elem) for elem in words[1:]])
        print(str(write), end=' ')
    elif words[0].lower() == "title":
        titleprompt = ' '.join([str(elem) for elem in words[1:]])
        os.system('title '+titleprompt)
    elif words[0].lower() == "clear" or words[0].lower() == "cls": os.system("cls")
    elif words[0].lower() == "pause": 
        if len(words) == 2:
            if words[1].lower() == "nul":
                os.system("pause >nul")
        else:
            os.system("pause")
    elif words[0].lower() == "wait": time.sleep(int(words[1]) / 1000)
    elif words[0].lower() == "goto" and fromfile == 1:
        open_file = open(inputfile, 'r')
        counterthing = 0
        for linei in open_file:
            testwords = linei.split()
            try: comment = testwords[0]
            except IndexError: comment = 0
            else:
                wordsinline = linei.split()
                if wordsinline[0].lower() == "label" and wordsinline[1:] == words[1:]:
                    currentLine = counterthing
            counterthing +=1
    elif words[0].lower() == "goto" and fromfile == 0: print("Goto is not a valid function of the console.")
    elif words[0].lower() == "set" or words[0].lower() == "var": # Vars
        if words[2].lower() == "input":
            setinput = ' '.join([str(elem) for elem in words[3:]])
            varinput = input(setinput + " ")
            set2input = ''.join([str(elem) for elem in words[1]])
            if set2input in varName: # check if variable already exists
                varnameindex = int(varName.index(set2input))
                varnameindex1 = varName[varnameindex]
                varvalueindex1 = varValue[varnameindex]
                varName.remove(varnameindex1) # Remove variable from list
                varValue.remove(varvalueindex1) # Remove variable from list
            varName.append(set2input)
            varValue.append(varinput)
        elif words[2] == "=" or words[2].lower() == "to":
            set1input = ' '.join([str(elem) for elem in words[3:]])
            set3input = ''.join([str(elem) for elem in words[1]])
            if set3input in varName: # check if variable already exists
                varnameindex = int(varName.index(set3input))
                varnameindex1 = varName[varnameindex]
                varvalueindex1 = varValue[varnameindex]
                varName.remove(varnameindex1) # Remove variable from list
                varValue.remove(varvalueindex1) # Remove variable from list
            varName.append(set3input)
            varValue.append(set1input)
        elif words[2].lower() == "remove" or words[2].lower() == "undefine":
            set3input = ''.join([str(elem) for elem in words[1]])
            if set3input in varName: # check if variable already exists
                varnameindex = int(varName.index(set3input))
                varnameindex1 = varName[varnameindex]
                varvalueindex1 = varValue[varnameindex]
                varName.remove(varnameindex1) # Remove variable from list
                varValue.remove(varvalueindex1) # Remove variable from list
    elif words[0].lower() == "int":
        if words[2] == "=" or words[2].lower() == "to":
            if words[4] == "+" or words[4].lower() == "plus":
                set1input = int(words[3]) + int(words[5])
            if words[4] == "*" or words[4].lower() == "times" or words[4].lower() == "by":
                set1input = int(words[3]) * int(words[5])
            if words[4] == "/" or words[4].lower() == "divided":
                set1input = int(words[3]) / int(words[5])
            if words[4] == "-" or words[4].lower() == "minus":
                set1input = int(words[3]) - int(words[5])
            set3input = ''.join([str(elem) for elem in words[1]])
            if set3input in varName: # check if variable already exists
                varnameindex = int(varName.index(set3input))
                varnameindex1 = varName[varnameindex]
                varvalueindex1 = varValue[varnameindex]
                varName.remove(varnameindex1) # Remove variable from list
                varValue.remove(varvalueindex1) # Remove variable from list
            varName.append(set3input)
            varValue.append(set1input)
        elif words[2] == "+=":
            indexvalue = int(varName.index(words[1]))
            varValue[indexvalue] = int(varValue[indexvalue]) + int(words[3])
        elif words[2] == "-=":
            indexvalue = int(varName.index(words[1]))
            varValue[indexvalue] = int(varValue[indexvalue]) - int(words[3])
        elif words[2] == "*=":
            indexvalue = int(varName.index(words[1]))
            varValue[indexvalue] = int(varValue[indexvalue]) * int(words[3])
        elif words[2] == "/=":
            indexvalue = int(varName.index(words[1]))
            varValue[indexvalue] = int(varValue[indexvalue]) / int(words[3])
    elif words[0].lower() == "float" or words[0].lower() == "double" or words[0].lower() == "int.decimal":
        if words[2] == "=" or words[2].lower() == "to":
            if words[4] == "+" or words[4].lower() == "plus":
                set1input = float(words[3]) + float(words[5])
            if words[4] == "*" or words[4].lower() == "times" or words[4].lower() == "by":
                set1input = float(words[3]) * float(words[5])
            if words[4] == "/" or words[4].lower() == "divided":
                set1input = float(words[3]) / float(words[5])
            if words[4] == "-" or words[4].lower() == "minus":
                set1input = float(words[3]) - float(words[5])
            set3input = ''.join([str(elem) for elem in words[1]])
            if set3input in varName: # check if variable already exists
                varnameindex = int(varName.index(set3input))
                varnameindex1 = varName[varnameindex]
                varvalueindex1 = varValue[varnameindex]
                varName.remove(varnameindex1) # Remove variable from list
                varValue.remove(varvalueindex1) # Remove variable from list
            varName.append(set3input)
            varValue.append(set1input)
        elif words[2] == "+=":
            indexvalue = int(varName.index(words[1]))
            varValue[indexvalue] = float(varValue[indexvalue]) + float(words[3])
        elif words[2] == "-=":
            indexvalue = int(varName.index(words[1]))
            varValue[indexvalue] = float(varValue[indexvalue]) - float(words[3])
        elif words[2] == "*=":
            indexvalue = int(varName.index(words[1]))
            varValue[indexvalue] = float(varValue[indexvalue]) * float(words[3])
        elif words[2] == "/=":
            indexvalue = int(varName.index(words[1]))
            varValue[indexvalue] = float(varValue[indexvalue]) / float(words[3])
    elif words[0].lower() == "random" or words[0].lower() == "rand":
        if words[1] in varName: # check if variable already exists
            varnameindex = int(varName.index(words[1]))
            varnameindex1 = varName[varnameindex]
            varvalueindex1 = varValue[varnameindex]
            varName.remove(varnameindex1) # Remove variable from list
            varValue.remove(varvalueindex1) # Remove variable from list
        # Set randvar
        randvar = int(randrange(int(words[2]))) + 1
        varName.append(words[1])
        varValue.append(randvar)
    elif words[0].lower() == "if.sensitive" or words[0].lower() == "if.cs":
        if words[2] == "=" or words[2] == "==" or words[2].lower() == "equ" or words[2].lower() == "is" or words[2].lower() == "equals":
            if words[1] == words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == ">" or words[2].lower() == "gtr":
            if words[1] > words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == "<" or words[3].lower() == "lss":
            if words[1] < words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2].lower() == "not" or words[2] == "!=":
            if words[1] != words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == ">=" or words[2].lower() == "geq" or words[2] == "=>":
            if words[1] >= words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == "<=" or words[2].lower() == "leq" or words[2] == "=<":
            if words[1] <= words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
    elif words[0].lower() == "if":
        if words[2] == "=" or words[2] == "==" or words[2].lower() == "equ" or words[2].lower() == "is" or words[2].lower() == "equals":
            if words[1].lower() == words[3].lower():
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == ">" or words[2].lower() == "gtr":
            if words[1].lower() > words[3].lower():
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == "<" or words[3].lower() == "lss":
            if words[1].lower() < words[3].lower():
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2].lower() == "not" or words[2] == "!=":
            if words[1].lower() != words[3].lower():
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == ">=" or words[2].lower() == "geq" or words[2] == "=>":
            if words[1].lower() >= words[3].lower():
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == "<=" or words[2].lower() == "leq" or words[2] == "=<":
            if words[1].lower() <= words[3].lower():
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
    elif words[0].lower() == "if.sensitive" or words[0].lower() == "if.cs":
        if words[2] == "=" or words[2] == "==" or words[2].lower() == "equ" or words[2].lower() == "is" or words[2].lower() == "equals":
            if words[1] == words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == ">" or words[2].lower() == "gtr":
            if words[1] > words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == "<" or words[3].lower() == "lss":
            if words[1] < words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2].lower() == "not" or words[2] == "!=":
            if words[1] != words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == ">=" or words[2].lower() == "geq" or words[2] == "=>":
            if words[1] >= words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == "<=" or words[2].lower() == "leq" or words[2] == "=<":
            if words[1] <= words[3]:
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
    elif words[0].lower() == "if.int" or words[0].lower() == "if.integer":
        if words[2] == "=" or words[2] == "==" or words[2].lower() == "equ" or words[2].lower() == "is" or words[2].lower() == "equals":
            if int(words[1].lower()) == int(words[3].lower()):
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == ">" or words[2].lower() == "gtr":
            if int(words[1].lower()) > int(words[3].lower()):
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == "<" or words[3].lower() == "lss":
            if int(words[1].lower()) < int(words[3].lower()):
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2].lower() == "not" or words[2] == "!=":
            if int(words[1].lower()) != int(words[3].lower()):
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == ">=" or words[2].lower() == "geq" or words[2] == "=>":
            if int(words[1].lower()) >= int(words[3].lower()):
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
        elif words[2] == "<=" or words[2].lower() == "leq" or words[2] == "=<":
            if int(words[1].lower()) <= int(words[3].lower()):
                words = words[4:]
                commands(varName, varValue, words, inputfile)
            elif words[4] == "(" and fromfile == 1: skipif(inputfile)
    else:
        invalid = ' '.join([str(elem) for elem in words])
        print("\nInvalid syntax '" + str(invalid) + "'\n")
        os.system("pause")

def Runner(inputfile):
    global varName, varValue, currentLine, totalLine, counterofstuff, fromfile
    fromfile = 1
    while True:
        num_lines = sum(1 for amountofline in open(inputfile))
        if num_lines <= currentLine: exit()
        open_file = open(inputfile, 'r')
        counter2 = 0
        for i in open_file:
            if counter2 == currentLine:
                totalLine = i
                break
            else: counter2 += 1
        words = totalLine.split()
        # Find and replace with var values
        allcomments = ["//", "##"]
        for i in allcomments:
            commentloop = 1
            for elem in words[1:]:
                if i in elem: words = words[0:commentloop]
                commentloop+=1
        word_counter = 0
        for elem in varName:
            elem = "["+elem+"]"
            loopcounter = 0
            for item in words:
                if elem in item: words[loopcounter] = item.replace(elem, str(varValue[word_counter]))
                if "&" in item: words[loopcounter] = item.replace("&", " ")
                loopcounter+=1
            word_counter += 1
        
        try: comment = words[0]
        except IndexError: comment = 0
        else: commands(varName, varValue, words, inputfile)
        currentLine+=1
        counterofstuff +=1

def Console():
    global varName, varValue, currentLine, totalLine, counterofstuff, fromfile, home
    fromfile = 0
    inputfile = 0
    sys.setrecursionlimit(10**8)
    currentLine = 0
    totalLine = 'initialize'
    counterofstuff = 0
    while True:
        open_file = input('>>> ')
        totalLine = open_file
        words = totalLine.split()
        # Find and replace with var values
        allcomments = ["//", "##"]
        for i in allcomments:
            commentloop = 1
            for elem in words[1:]:
                if i in elem: words = words[0:commentloop]
                commentloop+=1
        word_counter = 0
        for elem in varName:
            elem = "["+elem+"]"
            loopcounter = 0
            for item in words:
                if elem in item: words[loopcounter] = item.replace(elem, str(varValue[word_counter]))
                if "&" in item: words[loopcounter] = item.replace("&", " ")
                loopcounter+=1
            word_counter += 1
        
        try: comment = words[0]
        except IndexError: comment = 0
        else: commands(varName, varValue, words, inputfile)
        currentLine+=1
        counterofstuff+=1