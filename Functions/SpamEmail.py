import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mailer import Mailer
from mail import Mail
import universalFuncs
import time


inputArgs = sys.argv[1:]
defaultArgs = ["Target", "30.0", "1.0"] #target email, length, interval
args = universalFuncs.CheckArgs(inputArgs, defaultArgs)

userMailTarget = args[0]

mail = Mailer("MarvinSirius42@gmail.com", "gfyy lbqb nmvp nnqj")

StartTime = time.time()
spamming = True

while spamming:
    mail.sendMail(userMailTarget, "POO POO", "EAT POO POO")

    time.sleep(float(args[2]))

    if(time.time() - StartTime > float(args[1])):
        spamming = False

print("Spamming Complete")