import string
import math
import subprocess
from pathlib import Path

def CleanString(strClean):
    return(strClean.strip())#.translate(str.maketrans("", "", string.punctuation)))

def RunScript(script, args = []):
    return(subprocess.run(["python", script] + args, capture_output=True, text=True, check=True))

def CheckArgs(inputArgs, defaultArgs):
    args = defaultArgs
    for i in range(len(defaultArgs)):
        if(len(inputArgs) >= i + 1):
            if(inputArgs[i] != None):
                args[i] = inputArgs[i]
    return(args)