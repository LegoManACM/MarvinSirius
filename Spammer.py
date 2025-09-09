from mailer import Mailer
from time import sleep

userMailTarget = "peter.erikson@gmail.com"

mail = Mailer("MarvinSirius42@gmail.com", "gfyy lbqb nmvp nnqj")

while True:
    mail.sendMail(userMailTarget, "POO POO", "EAT POO POO")
    print("-")
    mail.sendMail(userMailTarget, "POO POO", "EAT POO POO")
    print("--")
    sleep(1)

