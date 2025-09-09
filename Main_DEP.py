from mailer import Mailer
from mail import Mail
from gpt4all import GPT4All
import time
from function import Function
from function_email import Function_Email
from function_end import Function_End

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", n_threads=8, device="cpu",)
mail = Mailer("MarvinSirius42@gmail.com", "gfyy lbqb nmvp nnqj")

modelBriefing = "speak the minimal words possible to satisfy requests"

operatedEmails = []

functions = []
functions.append(Function_Email("afrika.mcclintock@outlook.com"))
functions.append(Function_End())

def help():
    helpstr = ""
    for func in functions:
        helpstr += func.fName + "\n"
    return(helpstr)


recieved = 0
with model.chat_session():

    print(model.generate(modelBriefing))

    while True:
        
        newMail = mail.read_emails()

        if(newMail != None):
            for toOperateOn in newMail:
                recieved += 1
                modelOperating = True

                forModelMSG = toOperateOn.Body
                forModelSRC = "--User"
                activeFunc = None
                funcOutput = ""

                while modelOperating:
                    modelOutput = model.generate("Read the following request:\n" + forModelMSG + "\n Choose a function from the following list to fufil the request, call only one function at a time, be sure to email the user. Call '--end' when done\n" + help())
                    print("> "*15)
                    print(modelOutput)
                    if(activeFunc != None):
                        forModelMSG = activeFunc.processInput(modelOutput)
                        activeFunc = None
                    elif("--help" in modelOutput):
                        forModelMSG = help()
                        forModelSRC = "--System"
                    else:
                        forModelMSG = "Remember you can call '--help' to get availible functions."
                        for func in functions:
                            if(func.getFPrint() in modelOutput):
                                forModelMSG = func.fDesc
                                forModelSRC = "--System"
                                activeFunc = func
                    
                    if(forModelMSG == "quit"):
                        modelOperating = False
                    
                            

                operatedEmails.append(toOperateOn)
        
        print("Got " + str(recieved))
        recieved = 0

        mail.delete_emails()

        time.sleep(5)

    
    



"""

with model.chat_session():
    print(model.generate("Hey you there?", max_tokens=150))

mail = Mailer("MarvinSirius42@gmail.com", "gfyy lbqb nmvp nnqj")

#mail.sendMail("afrika.mcclintock@outlook.com", "Simpler Sending?", "This message was sent from a line of code!")

newMail = mail.read_emails()

for mail in newMail:
    print("\nFrom: " + mail.From + "\nSubject: " + mail.Subject)
    """