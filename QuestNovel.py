from random import randint, uniform


Names = ["Steve", "Jon", "Bob", "Jonny"]
def randomThingList(ListOfItems,numberOfOutputs = 1,RandomLeinght = False, MaxLenght = 100,MinLenght = 1):
        List = []
        i = 0

        if RandomLeinght:
            numberOfOutputs = randint(MinLenght,MaxLenght)
            
        if len(ListOfItems) < numberOfOutputs:
            numberOfOutputs = len(ListOfItems)
     
        while i < numberOfOutputs:
            x = randint(0,len(ListOfItems)-1)
            if not ListOfItems[x] in List:
                i = i + 1
                List.append(ListOfItems[x])
        return List


def FantasyNovelGenerator(characters = []):

    
    roles = []
    traits = []
    places = []
    quests = []
    quest_proprety = []
    Nothing = True
    try:
        for line in open("QuestNovelPack.txt"):
            linea = line[0:5]

            if "#" in line:
                continue        
            elif "role" in linea.lower():
                roles.append(line[4:].strip('\n ').lower())

            elif "place" in linea.lower():
                places.append(line[5:].strip('\n '))
            elif "quest_item" in line[0:11].lower():
                quests.append(line[10:].strip('\n ').lower())
            elif "trait" in linea.lower():
                traits.append(line[5:].strip('\n ').lower())
            elif "quest_proprety" in line[0:16].lower():
                quest_proprety.append(line[14:].strip('\n ').lower())
                
    except OSError:
        pass

    '''print('Characters: {0}'.format(characters))
    print('Roles: {0}'.format(roles))
    print('Traits: {0}'.format(traits))
    print('Places: {0}'.format(places))
    print('Quests: {0}'.format(quests))
    print('Quest_proprety: {0}'.format(quest_proprety))
    '''
    
    Romance = round(uniform(0,10), 1)
    Fights = round(uniform(0,10), 1)
    Adventure = round(uniform(0,10), 1)
    Raiting = round((Romance + Fights + Adventure)/2.25, 1)
    if Raiting > 10.0:
        Raiting = 10.0
    
    #Random list of names
    printed = randomThingList(characters,numberOfOutputs = randint(2,4))
    #printed = printed + randomThingList(characters[0])


    Printout = 'In a new fantasy novel staring:\n'

    #Iterate thru the names
    for name in printed :
        Printout = Printout + name + ' as ' + traits[randint(0,len(traits)-1)]
        Printout = Printout + ' '+ roles[randint(0,len(roles)-1)] + '\n'


    #Sticging text togeather
    Printout = Printout + "Join their journey to the {0}, where they will go on {1} quest to find {2} of {3}.".format(places[randint(0,len(places)-1)], "epic", quests[randint(0,len(quests)-1)], quest_proprety[randint(0,len(quest_proprety)-1)])

    #Printing out part
    #print (Printout + ("\nThe novel raiting: {0}/10 \nRomance raiting: {1}/10 \nAdventure raiting: {2}".format(Raiting,Romance,Adventure)))
    
    return (Printout + "\nThe novel rating: {0}/10 \nRomance rating: {1}/10 \nAdventure rating: {2}/10".format(Raiting,Romance,Adventure))
