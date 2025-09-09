from mailer import Mailer
from mail import Mail
from function import Function

class Function_Email(Function):
    def __init__(self, targetEmailAddr):
        self.fName = "--Email"
        self.fDesc = """By calling this function you are responding to the user.
        In the first line of the response please give a 3 word descripton of what your message pertains to.
        In the rest of the message say what you need to tell the user."""
        self.targetEmailAddr = targetEmailAddr
        self.mail = Mailer("MarvinSirius42@gmail.com", "gfyy lbqb nmvp nnqj")
    
    def getFPrint(self):
        return("---" + self.fName)
    
    def processInput(self, fInput, emailTarget=""):
        fInput = fInput.lower()
        if(emailTarget == ""):
            target = self.targetEmailAddr
        else:
            target = emailTarget

        subjectLine = fInput.split("\n")[0]

        return(self.mail.sendMail(emailTarget, "From Marvin lol", fInput[len(subjectLine):], max_tokens=150))
