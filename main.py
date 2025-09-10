from mailer import Mailer
from mail import Mail
from pathlib import Path
import subprocess
import time
import math
import string
import universalFuncs

heartBeat = 15
lastBeat = time.time()

mail = Mailer("MarvinSirius42@gmail.com", "gfyy lbqb nmvp nnqj")

funcPath = Path("./Functions")



#def RunScript(script, args = []):
#    return(subprocess.run(["python", script] + args, capture_output=True, text=True, check=True))

#def CleanString(strClean):
#    return(strClean.strip().translate(str.maketrans("", "", string.punctuation)))
    

def MailForMarvin(email):
    print(">>> Mail received for Marvin!")
    body = email.Body
    lines = body.split("\n")

    print(email.Subject)
    
    encounteredError = False

    for lineOG in lines:
        line = universalFuncs.CleanString(lineOG)
        #call = universalFuncs.CleanString(lineOG.split("(", 1)[0])

    for func in funcPath.iterdir():
        try:
            if(email.Subject == func.name.split(".")[0]):
                arguments = lines
                #lineArgs = ""
                #try:
                #    lineArgs = line.split("(")[1]
                #    lineArgs = lineArgs.split(")")[0]
                #    arguments = lineArgs.split(",")
                #except:
                #    arguments = []

                print(">>> Running: " + func.name + " with args: " + str(arguments))
                result = universalFuncs.RunScript(func, arguments)
                print(">>> Output:", result.stdout)
        except Exception as e:
            print(">>> Tried and failed:\n" + str(e))
            encounteredError = True

    if(encounteredError == False):
        mail.delete_emails(emailID = email.MailID.decode())

while True:
    #heart Beat
    if((time.time() - heartBeat) > lastBeat):
        lastBeat = time.time()
        #print("\n>>> Tick")
        
        #check for mail
        newMail = mail.read_emails()

        #if has mail
        if(newMail != None):
            #iterate through mail
            for item in newMail:
                MailForMarvin(item)

                    
                
