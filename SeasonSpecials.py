from random import randint, uniform
import time

def Spooktober(Odds):
    doot = randint(0,Odds)
    return time.strftime("%m",time.gmtime()) == "10" and doot == int(Odds/2)

def December(Odds):
    number = randint(0,Odds)
    return time.strftime("%m",time.gmtime()) == "12" and number == int(Odds/2)

def November(Odds):
    number = randint(0,Odds)
    return time.strftime("%m",time.gmtime()) == "11" and number == int(Odds/2)
