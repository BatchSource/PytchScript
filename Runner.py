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
        except IndexError: pass
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
        except IndexError: pass
        else: commands(varName, varValue, words, inputfile)
        currentLine+=1

def commands(varName, varValue, words, inputfile):
    global currentLine, totalLine, fromfile
    if words[0].lower() == "say" or words[0].lower() == "print" or words[0].lower() == "echo":
        say = ' '.join([str(elem) for elem in words[1:]])
        print(str(say))
    elif words[0].lower() == "key":
        from pynput.keyboard import Key, Controller as KeyboardController
        from pynput.mouse import Button, Controller as MouseController
        import win32api
        keyboard = KeyboardController()
        mouse = MouseController()
        if words[1].lower() == "cursor":
            if words[2].lower() == "move":
                win32api.SetCursorPos((int(words[3]),int(words[4])))
            elif words[2].lower() == "click":
                for i in words[3:]:
                    if i.lower() == "left": mouse.press(Button.left); mouse.release(Button.left)
                    elif i.lower() == "right": mouse.press(Button.right); mouse.release(Button.right)
                    elif i.lower() == "middle": mouse.press(Button.middle); mouse.release(Button.middle)
        elif words[1].lower() == "press":
            for i in words[2:]:
                if i.lower() == "ctrl" or i.lower() == "control":
                    keyboard.press(Key.ctrl); keyboard.release(Key.ctrl)
                elif i.lower() == "shift": keyboard.press(Key.shift); keyboard.release(Key.shift)             
                elif i.lower() == "alt" or i.lower() == "option": keyboard.press(Key.alt); keyboard.release(Key.alt)
                elif i.lower() == "copy":
                    keyboard.press(Key.ctrl); keyboard.press('c')
                    keyboard.release('c'); keyboard.release(Key.ctrl)
                elif i.lower() == "paste":
                    keyboard.press(Key.ctrl); keyboard.press('v')
                    keyboard.release('v'); keyboard.release(Key.ctrl)
                elif i.lower() == "tab": keyboard.press(Key.tab); keyboard.release(Key.tab)
                elif i.lower() == "esc": keyboard.press(Key.esc); keyboard.release(Key.esc)
                elif i.lower() == "f1": keyboard.press(Key.f1); keyboard.release(Key.f1)
                elif i.lower() == "f2": keyboard.press(Key.f2); keyboard.release(Key.f2)
                elif i.lower() == "f3": keyboard.press(Key.f3); keyboard.release(Key.f3)
                elif i.lower() == "f4": keyboard.press(Key.f4); keyboard.release(Key.f4)
                elif i.lower() == "f5": keyboard.press(Key.f5); keyboard.release(Key.f5)
                elif i.lower() == "f6": keyboard.press(Key.f6); keyboard.release(Key.f6)
                elif i.lower() == "f7": keyboard.press(Key.f7); keyboard.release(Key.f7)
                elif i.lower() == "f8": keyboard.press(Key.f8); keyboard.release(Key.f8)
                elif i.lower() == "f9": keyboard.press(Key.f9); keyboard.release(Key.f9)
                elif i.lower() == "f10": keyboard.press(Key.f10); keyboard.release(Key.f10)
                elif i.lower() == "f11": keyboard.press(Key.f11); keyboard.release(Key.f11)
                elif i.lower() == "f12": keyboard.press(Key.f12); keyboard.release(Key.f12)
                elif i.lower() == "delete" or i.lower() == "del": keyboard.press(Key.delete); keyboard.release(Key.delete)
                elif i.lower() == "insert": keyboard.press(Key.insert); keyboard.release(Key.insert)
                elif i.lower() == "enter": keyboard.press(Key.enter); keyboard.release(Key.enter)
                elif i.lower() == "down": keyboard.press(Key.down); keyboard.release(Key.down)
                elif i.lower() == "right": keyboard.press(Key.right); keyboard.release(Key.right)
                elif i.lower() == "left": keyboard.press(Key.left); keyboard.release(Key.left)
                elif i.lower() == "up": keyboard.press(Key.up); keyboard.release(Key.up)
                elif i.lower() == "backspace": keyboard.press(Key.backspace); keyboard.release(Key.backspace)
                elif i.lower() == "space": keyboard.press(Key.space); keyboard.release(Key.space)       
                else: keyboard.type(i)
        elif words[1].lower() == "type":
            typecontents = ' '.join([str(elem) for elem in words[2:]])
            keyboard.type(typecontents)
    
    elif words[0].lower() == "say." or words[0].lower() == "print." or words[0].lower() == "echo.": print("")
    elif "#" in words[0].lower() or "label" in words[0].lower() or "(" == words[0] or ")" in words[0] or "::" in words[0].lower() or "//" in words[0].lower(): pass # Comment
    elif words[0].lower() == "cmd":
        bat = ' '.join([str(elem) for elem in words[1:]])
        os.system(str(bat))
    elif words[0].lower() == "quit" or words[0].lower() == "exit" or words[0].lower() == "stop": exit()
    elif words[0].lower() == "write.file":
        writefile = ''.join([str(elem) for elem in words[1]])
        writecontents = ' '.join([str(elem) for elem in words[2:]])
        with open(writefile, 'a+') as filehandle:
            filehandle.write(writecontents+'\n')
    elif words[0].lower() == "call": callfile(words, varName, varValue, inputfile)
    elif words[0].lower() == "help" and fromfile == 0: os.system("start https://github.com/BatchSource/PytchScript/blob/master/README.md")
    elif "#" in words[0].lower() or "::" in words[0].lower() or "//" in words[0].lower(): pass
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
            except IndexError: pass
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
        try: comment = int(words[0]) - 1
        except TypeError:
            invalid = ' '.join([str(elem) for elem in words])
            print("\nInvalid syntax '" + str(invalid) + "'\n")
            os.system("pause")
        else:
            if int(words[0]) <= -2 or int(words[0]) == 0 or int(words[0]) == 1:
                print("\nYou cannot loop a command "+words[0]+" amount of times, however you can loop it indefinetly with -1.\n")
                os.system("pause")                
            else:
                forloopamount = int(words[0]); forcounter = 0
                words = words[1:]
                while forcounter != forloopamount:
                    commands(varName, varValue, words, inputfile)
                    forcounter+=1

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
        except IndexError: pass
        else: commands(varName, varValue, words, inputfile)
        currentLine+=1
        counterofstuff +=1

def Console():
    global varName, varValue, currentLine, totalLine, counterofstuff, fromfile
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
        except IndexError: pass
        else: commands(varName, varValue, words, inputfile)
        currentLine+=1
        counterofstuff+=1
