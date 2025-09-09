import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mailer import Mailer
from mail import Mail
import universalFuncs

inputArgs = sys.argv[1:]
defaultArgs = ["No Provided Subject", "No Provided Body"]
args = universalFuncs.CheckArgs(inputArgs, defaultArgs)



userMailTarget = "afrika.mcclintock@outlook.com"

mail = Mailer("MarvinSirius42@gmail.com", "gfyy lbqb nmvp nnqj")
mail.sendMail(userMailTarget, args[0], args[1])

print("sent")