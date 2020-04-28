from random import randint, uniform
import time



def randomThingList(array,numberOfOutputs = 1,RandomLeinght = False, MaxLenght = 100,MinLenght = 1):
    List = []
    i = 0

    if RandomLeinght:
        numberOfOutputs = randint(MinLenght,MaxLenght)
        
    if len(array) < numberOfOutputs:
        numberOfOutputs = len(array)
 
    while i < numberOfOutputs:
        x = randint(0,len(array)-1)
        if not array[x] in List:
            i = i + 1
            List.append(array[x])
    return List

        

def RomanticNovelGenerator(characters = []):
    roles = []
    traits = []
    places = []
    Fantasies = []
    Nothing = True
    try:
        for line in open("RomanticNovelPack.txt"):
            linea = line[0:5]

            if "#" in line:
                continue        
            elif "role" in linea.lower():
                roles.append(line[4:].strip('\n ').lower())

            elif "place" in linea.lower():
                places.append(line[5:].strip('\n ').lower())
            elif "fanta" in linea.lower():
                Fantasies.append(line[5:].strip('\n ').lower())
            elif "trait" in linea.lower():
                traits.append(line[5:].strip('\n ').lower())
    except OSError:
        return "Missing file"

    print('Characters: ')
    print(characters)
    
    Romance = round(uniform(0,10), 1)
    Erotic = round(uniform(0,10), 1)
    Raiting = round((Romance + Erotic)/1.5, 1)
    if Raiting > 10.0:
        Raiting = 10.0
    
    #Random list of names
    printed = randomThingList(characters,randint(2,4))
    #printed = printed + randomThingList(characters[0])


    Printout = 'In a new romantically-erotic novel starring:\n'

    #Iterate thru the names
    for name in printed :
        Printout = Printout + name + ' as ' + traits[randint(0,len(traits)-1)]
        Printout = Printout + ' '+ roles[randint(0,len(roles)-1)] + '\n'

    fantasie = randomThingList(Fantasies)

    #Sticging text togeather
    Printout = Printout + 'They will make out in the ' + places[randint(0,len(places)-1)]
    Printout = Printout + ", where they'll play out their " + fantasie[0] + " fantasie(s)"

    #Printing out part
    return Printout + "\nThe novel rating: " + str(Raiting) + "/10 \nRomance rating: " + str(Romance) + "/10 \nErotic rating: " + str(Erotic) + "/10"
    

def Discord_name(string):
    return "<@" + str(string) + ">"


def Dice(Sided=6):
    if Sided > 1:
        return randint(1,Sided)
    else:
        return "No dice"

def Compliment(person_id):
    compliments = ["alluring","appealing","dazzling","delicate","delightful","cute","awesome","smart","amazing","astonishing","beautiful","sweet","charming","funny","gorgeous","intelligent","breathtakeing","elegant","exquisite","fascinating","fine","good-looking","graceful","handsome","lovely","magnificent","marvelous","pretty","stunning","superb","wonderful","angelic"]
    return "Hey, Psst!!\n {0}\n You're {1}".format(Discord_name(person_id),compliments[randint(0,len(compliments))])



def LoveMeter(PersonA, PersonB):

    return round(float((PersonA * PersonB) % 100.0) + float((PersonA + PersonB) % 100 ) / 100, 1)

def Logging(message):
    try:
        print("{0}{1}-{2}:{3}".format(time.strftime("[%d.%m.%Y/%H:%M:%S]", time.localtime()),message.guild.name,message.author.name,message.content))
        return ("{0}{1}-{2}:{3}".format(time.strftime("[%d.%m.%Y/%H:%M:%S]", time.gmtime()),message.guild.name,message.author.name,message.content))
    except AttributeError:
        return ("{0} {1}:{2}".format(time.strftime("[%d.%m.%Y/%H:%M:%S]", time.gmtime()),message.author.name,message.content))

def RandFact():
    facts = []
    for line in open("Facts.txt","r"):
        facts.append(line)
    return facts[randint(0,len(facts)-1)]


def TruthORDare(TorD):
    responses = [[],[]]
    try:
        for line in open("TruthOrDare.txt"):
            linea = line[0:6]

            if "#" in line:
                continue        
            elif "truth" in linea.lower():
                responses[0].append(line[6:].strip('\n '))

            elif "dare" in linea.lower():
                responses[1].append(line[5:].strip('\n '))

    except OSError:
        return "Missing file"
    if TorD.lower() == "t":
        return responses[0][randint(0,len(responses[0])-1)]
    elif TorD.lower() == "d":
        return responses[1][randint(0,len(responses[1])-1)]
    
    
def PickupLine():
    facts = []
    for line in open("PickupLines.txt","r"):
        facts.append(line.strip('\n '))
    return facts[randint(0,len(facts)-1)]

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False



def SlotMachine(Symbols = [":money_with_wings:",":dollar:",":yen:",":gem:",":moneybag:"]):
    Same = 1
    Display = []
    for x in range(3):
        Squear = randint(0,len(Symbols)-1)
        if Symbols[Squear] in Display:
            Same += 1
        Display.append(Symbols[Squear])
    String = ""
    for char in Display:
        String += char
    return(String,Same)

def Battleship():
    return f'http://en.battleship-game.org/id{randint(10000000, 9000000000000)}'