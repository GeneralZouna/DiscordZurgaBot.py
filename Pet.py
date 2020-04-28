from time import time
from random import uniform, randint
import os


class Pet():
    
    def __init__(self):
        #When you create pet this are starting values
        self.Alive = True
        self.Mortal = True
        self.Hibernate = False

        self.Name = "Pet"
        self.HP = 100.0
        self.Mood = 100.0
        self.Hunger = 100.0
        self.Stamina = 100.0

        self.Moral = 90.0
        self.Trust = 50.0
        self.Saturation = 50.0

        #speed at which values change
        self.HUNGER_DECAY = 43200.0
        self.HEALTH_DECAY = 250000.0
        self.MOOD_DECAY = 28800.0
        self.MORAL_DECAY = 604800.0
        self.STAMINA_REGEN = 14400.0
        self.SATURATION_DECAY = 604800.0

        #When was the last time you checked on your pet?
        self.Last_time = int(time())

        #Known faces of pet
        self.expressions = { 'happy':'(◕‿‿◕)',
                             'bored':'(-__-)',
                             'sad':'(╥☁╥ )',
                             'friendly':'(♥‿‿♥)',
                             'cool':'(⌐■_■)',
                             'waiting':'(•‿‿•)',
                             'dead' : '(#__#)',
                             'grateful':'(^‿‿^)',
                             'table flip': '(╯°□°）╯︵ ┻━┻'
                            } #Add more emotions to it

    
    def HPChange(self,timeChange):
        #Health deays if it's hungry (So far)
        self.HP -= (100.0/ self.HEALTH_DECAY) * timeChange

        if self.HP <= 0.0:
            self.HP = 0.0
            if self.Mortal:
                self.Alive = False
        elif self.HP > 100.0:
            self.HP = 100.0


    def StaminaChange(self,timeChange):
        if self.HP > self.Stamina:
            if self.Hunger > (100.0/(self.STAMINA_REGEN * 4.0)):
                self.Stamina += (100.0/ self.STAMINA_REGEN) * timeChange
                self.Hunger -= 100.0/(self.STAMINA_REGEN * 4.0)
   
        if self.Stamina < 0.0:
            self.Stamina = 0.0

        elif self.Stamina > self.HP:
            self.Stamina = self.HP


    def HungerChange(self,timeChange):
        #Hunger ticks down by time, to ensure it's not going to
        #deplete under 8h i'm not giving it random factor
        HChange = (100.0/(self.HUNGER_DECAY*(1.0+(self.Saturation/100.0))))*timeChange

        if (self.Hunger - HChange) <= 0.0:
            StarvationTime = abs((HChange - self.Hunger)/(100.0/(self.HUNGER_DECAY*(1.0+(self.Saturation/100.0) ))))
            self.Hunger = 0.0

            self.HPChange(StarvationTime)


        elif (self.Hunger - HChange) >= 0.0:
            self.Hunger -= HChange

        if self.Hunger < 0.0:
            self.Hunger = 0.0
        elif self.Hunger > 100.0:
            self.Hunger = 100.0


    def MoodChange(self,timeChange):
        #Mood is dependant on how hungry it is
        if timeChange > 600:
            self.Mood -= abs(timeChange * (((100.0 - self.Hunger)/100) +1) * 100/ self.MOOD_DECAY)

        if self.Mood < 0.0:
            self.Mood = 0.0
        elif self.Mood > self.HP:
            self.Moral += self.Mood - self.HP
            self.Mood = self.HP

    
    def MoralChange(self,timeChange):
        #Depending on It's mood It changes it's moral
        MChange = (self.Mood - 50.0) * timeChange/self.MORAL_DECAY
        self.Moral += MChange #this just means add MChange to Moral

        if self.Moral < 0.0:
            self.Moral = 0.0
        elif self.Moral > self.HP:
            self.Moral = self.HP


    def SaturationChange(self,timeChange):
        self.Saturation -= timeChange * (100-self.Hunger) /self.SATURATION_DECAY

        if self.Saturation < 0.0:
            self.Saturation = 0.0
        elif self.Saturation > self.HP:
            self.Saturation = self.HP



    def selfCheck(self):
        if self.HP <= 0.0:
            self.HP = 0.0
            if self.Mortal:
                self.Alive = False

        if not self.Alive and self.Mortal: #Basically if it's dead it's dead
            return f'{self.expressions["dead"]}\nR.I.P {self.Name}'
        #What happened since you last checked on it

        if self.Hibernate:
            self.Last_time = int(time())


        TimePassed = float(int(time()) - self.Last_time)
        
        self.StaminaChange(TimePassed)
        self.HungerChange(TimePassed)
        self.MoodChange(TimePassed)
        self.MoralChange(TimePassed)
        self.SaturationChange(TimePassed)
        self.HPChange(0)

        if self.HP > 100.0:
            self.HP = 100.0

        if self.Mood > self.HP:
            self.Mood = self.HP
        elif self.Mood < 0.0:
            self.Mood = 0.0
        if self.Stamina > self.HP:
            self.Stamina = self.HP
        elif self.Stamina < 0.0:
            self.Stamina = 0.0
        if self.Hunger > self.HP:
            self.Hunger = self.HP
        elif self.Hunger < 0.0:
            self.Hunger = 0.0
        if self.Moral > self.HP:
            self.Moral = self.HP
        elif self.Moral < 0.0:
            self.Moral = 0.0


        self.Last_time = int(time())


    def Mischief(self,action):
        '''
        action - what you were doing 
        0 - Just checked on it
        1 - was playing with it
        2 - was feeding it
        '''

        Food = 0.0
        Fun = 0.0

        if uniform(-500.0,80.0) > self.Moral:

            bad_things = [[f'{self.Name} flipped the table (╯°□°）╯︵ ┻━┻',f'{self.Name} is chewing on your shoes (◕﹏◕)'], #bad things it may do while being checked on
                      [f'{self.Name} flipped the table ┻━┻︵ \\(°□°)/ ︵ ┻━┻ \n',f'{self.Name} chewed on your shoes (◕﹏◕)'],#bad things while you were playing with it
                      [f'{self.Name} ate your homework (◕﹏◕)\n [+{round(Food,2)} hunger]']]# bad things while you were feeding it

            #Certain actions also do certain things, like eating your homework will replanish it's hunger bar :P
            BadChoice = randint(0,len(bad_things[action])-1)
            
            if BadChoice == 0 and action == 2:
                Food = uniform(0.0,5.0)
                self.Hunger += Food

            if action > 0:
                Fun = uniform(0.0,5.0)
                self.Mood += Fun


            bad_things = [[f'{self.Name} flipped the table (╯°□°）╯︵ ┻━┻',f'{self.Name} is chewing on your shoes (◕﹏◕)'], #bad things it may do while being checked on
                      [f'{self.Name} flipped the table ┻━┻︵ \\(°□°)/ ︵ ┻━┻ \n',f'{self.Name} chewed on your shoes (◕﹏◕)'],#bad things while you were playing with it
                      [f'{self.Name} ate your homework (◕﹏◕)\n [+{round(Food,2)} hunger]']]# bad things while you were feeding it
                      

            return True , bad_things[action][BadChoice]
        else:
            return False, ''



    def Feed(self):
        self.selfCheck()
        if not self.Alive and Mortal:
            return f'{self.expressions["dead"]}\nR.I.P {self.Name}'

        Bad = self.Mischief(2)
        if Bad[0]:
            return Bad[1]

        Food = uniform(30.0,50.0)

        OldHunger = self.Hunger + 0.1


        if self.Hunger < 90.0:
            self.Hunger += Food
            if self.Hunger > 100.0:
                self.Saturation += abs(self.Hunger-100.0)/10.0
                self.Hunger = 100.0

            self.Last_time = int(time())

            return f'{self.expressions["grateful"]}\n{self.Name} is happy you fed it. [+{round(Food)} hunger]'

        else:
            return f'{self.expressions["bored"]}\n{self.Name} is not interested in eating at the moment.'



    def Play(self, Activity):
        self.selfCheck()

        if not self.Alive and self.Mortal:
            return f'{self.expressions["dead"]}\nR.I.P {self.Name}'

        Bad = self.Mischief(1)
        if Bad[0]:
            return Bad[1]

        if Activity.lower() == 'pet' and self.Stamina > 15.0:
            improvement = uniform(10.0,25.0)
            self.Mood += improvement
            self.Stamina -= 15.0
            return f'{self.expressions["grateful"]}\n{self.Name} is happy you pet it.\nIt feels happier now. [+{round(improvement,2)} mood] [-15 stamina]'

        elif Activity.lower() == 'play' and self.Stamina > 20.0:
            improvement = uniform(15.0,30.0)
            self.Mood += improvement
            self.Stamina -= 20.0
            return f'{self.expressions["grateful"]}\n{self.Name} is happy you played with it.\nIt feels happier now. [+{round(improvement,2)} mood][-20 stamina]'

        elif Activity.lower() in 'playpet':
            return f'(≖__≖)\n{self.Name} is too tired right now.'
        
        else:
            return 'Pet is confused'



    def Status(self):
        #First update everything about it
        Bad = self.Mischief(0)
        self.selfCheck()

        #It's no point looking how it feels like if it's dead, duh
        if not self.Alive and self.Mortal:
            return f'{self.expressions["dead"]}\nR.I.P {self.Name}'
        
        #Now since it's still kicking let's see how it's feeling like today

        emotion = ''
        if self.Mood > 70:
            if int(self.Mood % 3) == 2:
                emotion = 'cool'
            elif int(self.Mood) % 5 == 4:
                emotion = 'friendly'
            else:
                emotion = 'happy'
        elif self.Mood > 55:
            emotion = 'waiting'
        elif self.Mood > 40:
            emotion = 'bored'
        elif self.Mood <= 40:
            emotion = 'sad'

        #If it's bad it's going to give us message it did something bad and what was the bad thing
        if Bad[0]:
            return f'{Bad[1]}\nMood:{emotion.capitalize()}\nHP:{round(self.HP,2)}\nHunger:{round(self.Hunger,2)}\nMood:{round(self.Mood,2)}\nStamina:{round(self.Stamina,2)}'


        return f'{self.expressions[emotion]}\nMood:{emotion.capitalize()}\nHP:{round(self.HP,2)}\nHunger:{round(self.Hunger,2)}\nMood:{round(self.Mood,2)}\nStamina:{round(self.Stamina,2)}'


    



'''

    (⇀‿‿↼) sleeping
    (≖‿‿≖) awakening
    (◕‿‿◕) awake / normal
    ( ⚆_⚆), (☉_☉ ) observing (neutral mood)
    ( ◕‿◕), (◕‿◕ ) observing (happy)
    (°▃▃°) intense
    (⌐■_■) cool
    (•‿‿•) happy
    (^‿‿^) grateful
    (ᵔ◡◡ᵔ) excited
    (✜‿‿✜) smart
    (♥‿‿♥) friendly
    (☼‿‿☼) motivated
    (≖__≖) demotivated
    (-__-) bored
    (╥☁╥ ) sad
    (ب__ب) lonely
    (☓‿‿☓) broken
    (#__#) debugging
'''
def Save_Pet(ID,Pet,Save = False):
    try:
        File = open("Pet_info.pet",'x')
    except Exception:
        pass

    Save_data = f"ID {ID}\nHP {Pet.HP}\nMood {Pet.Mood}\nHunger {Pet.Hunger}\nName {Pet.Name}\nTime {Pet.Last_time}\nMoral {Pet.Moral}\nSaturation {Pet.Saturation}\nAlive {Pet.Alive}\nMortal {Pet.Mortal}\nHibernate {Pet.Hibernate}\n\n"
    if Save:
        File = open("Pet_info.pet",'w')
        File.write(Save_data)
        File.close()
        print('saved')
        return ''
    else:
        print(f'Saved data:\n{Save_data}')
        return Save_data




def SavePetList(Pet_list):
    File = open("Pet_info.pet",'w')
    i = 0
    Save_data = ''
    ID_List = list(Pet_list)
    print("saveing")
    for Pet in Pet_list:
        Save_data += Save_Pet(Pet,Pet_list[Pet])
        i += 1
    File.write(Save_data)
    File.close()
    print("saved")


def TrueToTrue(string):
    if 'true' in string.lower():
        return True
    else:
        return False

def Load_pet():
    pet_list = {}
    ID = ''
    print('Loading started')
    try:
        for line in open("Pet_info.pet",'r'):            
            if line.startswith('ID'):
                ID = line.lstrip('ID').replace(' ','').replace('\n','')
                pet_list[ID] = Pet()

            elif line.startswith('HP'):
                pet_list[ID].HP = float(line.lstrip('HP'))

            elif line.startswith('Mood'):                
                pet_list[ID].Mood = float(line.lstrip('Mood'))

            elif line.startswith('Hunger'):
                pet_list[ID].Hunger = float(line.lstrip('Hunger'))

            elif line.startswith('Name'):
                pet_list[ID].Name = line[5:].lstrip(' ').replace('\n','')

            elif line.startswith('Time'):
                pet_list[ID].Last_time = int(line.lstrip('Time'))

            elif line.startswith('Moral'):
                pet_list[ID].Moral = float(line.lstrip('Moral'))

            elif line.startswith('Saturation'):
                pet_list[ID].Saturation = float(line.lstrip('Saturation'))

            elif line.startswith('Alive'):
                pet_list[ID].Alive = TrueToTrue(line.lstrip('Alive'))

            elif line.startswith('Mortal'):
                pet_list[ID].Mortal = TrueToTrue(line.lstrip('Mortal'))

            elif line.startswith('Hibernate'):
                pet_list[ID].Hibernate = TrueToTrue(line.lstrip('Hibernate'))


        print('load succsesfull')
        return pet_list

    except Exception:
        print('loading failed')
        return pet_list





'''
Pet_list = Load_pet()

if len(list(Pet_list)) < 1:
    Pet_list['pet'] = Pet()
Key = list(Pet_list)[0]



while Pet_list[Key].Alive:
    print(Pet_list[Key].Status())
    Action = input().lower()
    os.system("cls")
    if Action == "play":
        print(Pet_list[Key].Play('play'))
    elif Action == 'pet':
        print(Pet_list[Key].Play('pet'))
    elif Action == 'feed':
        print(Pet_list[Key].Feed())
    elif Action == 'rename':
        New_name  = input(f'New name of {Pet_list[Key].Name} is going to be: ').replace('\n','')
        Sure = input(f"Are you sure you wish to name your pet {New_name}? (y/n)")
        if Sure.lower() == "y":
            Pet_list[Key].Name = New_name
    
    Pet_list[Key].Status()
    Save_Pet(Key,Pet_list[Key], True)
    if Action in 'exitgoodbye' and len(Action) > 2:
        print('Bye master (>^-^)>')
        break





os.system('pause;')
'''
'''
play - play with your pay
pet - pett the critter
feed - feed it
rename - change it's name
exit/bye/goodbye - leave/close the window
'''