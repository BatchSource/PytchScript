import os
import time
from random import randrange
from Runner import Runner
from Runner import Console
import sys
sys.setrecursionlimit(10**8)

from os.path import expanduser
home = expanduser("~")

def help():
    os.system("cls")
    print(
    "Usage: python pytch.py <argument>"
    + '\n\n'
    + "Interpreter Options\n"
    + "\"-h\" or \"--help\"        - Open this screen\n"
    + "\"-r\" or \"--run\" <file>  - Run the .pytch file\n"
    + "\"-c\" or \"--console\"     - Opens the Pytch console\n"
    )

if len(sys.argv) < 2:
    help(); os.system("pause")
elif sys.argv[1] == '-h' or sys.argv[1] == '--help': help()
elif sys.argv[1] == '-r' or sys.argv[1] == '--run':
    inputfile = sys.argv[2]
    inputfile = inputfile.rstrip('"')
    if os.path.isfile(inputfile):
        filename, file_extension = os.path.splitext(inputfile)
        if file_extension.lower() == '.pytch':
            varName = []; varValue = []
            currentLine = 0
            totalLine = 'initialize'
            counterofstuff = 0
            os.system("cls")
            Runner(inputfile)
        else:
            print("The file is not a .pytch file.")
            print("")
            os.system("pause")
            exit()
    else:
        print("The file does not exist.")
        print("")
        os.system("pause")
        exit()
elif sys.argv[1] == '--console' or sys.argv[1] == '-c':
    os.system("cls")
    varName = []; varValue = []
    print("Pytch [Version 1.0]")
    print("(c) 2020 Alex Irick. All rights reserved.\n")
    Console()
else:
    print("Invalid argument.")
    print("")
    os.system("pause")
    exit()

