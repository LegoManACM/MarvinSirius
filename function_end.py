from function import Function

class Function_End(Function):
    def __init__(self):
        self.fName = "--end"
        self.fDesc = "leave a message describing what you accomplished between receiving a message and calling this '---end' function"
    
    def getFPrint(self):
        return("---" + self.fName)
    
    def processInput(self, fInput):
        print(fInput)
        return("quit")