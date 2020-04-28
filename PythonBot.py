#https://discordpy.readthedocs.io/en/latest/index.html
#https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

import time
import os
import discord
import asyncio
import Neko
from RandomCommands import *
from random import randint
from ball8 import _8ball
from Economy import *
from QuestNovel import *
import Help
from Settings import *
from Minesweeper import *
import SeasonSpecials as SeasonSpecial
import PetInterface


DiscordBotToken = "<Bot token>"

client = discord.Client()

UpdateData(False)
SettingsUpdate(False)


TimeoutPeopleList = {"robbery": [],'paycheck':[]}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.user.display_name)

@client.event
async def on_message(message):
    Logging(message)

    #ID of guilds
    ID_Set = message.guild.id
    command_prefix = getSetting(ID_Set,'command')

#Pets for all :3
    if message.content.lower() == "{0}!pet fuck".format(command_prefix):
	    await message.channel.send("You sick fuck, what the fuck are you trying to do?")
    else:
	    await PetInterface.PetInterface(message)

#When you need some help    
    if message.content.lower() == "{0}help".format(command_prefix):
        await message.channel.send(Help.Help_command().format(command_prefix))
    
    if message.content.lower() == "{0}help+".format(command_prefix):
        await message.channel.send(Help.Help_command(True,0).format(command_prefix))
        await message.channel.send(Help.Help_command(True,1).format(command_prefix))


#Hello there!
    if message.content.lower() in ["hey","hello","hi","hey!","hello!","hi!"]:
        Hey = ['Hey!','Heyo!','Hello!','Woooo!']
        if randint(0,10) == 5:
            await message.channel.send(Hey[randint(0,len(Hey)-1)])
            
#I don't think my bot likes this
    if message.content.startswith('!shutdown') and message.author.id == 187982881123991553:
        print("Stopping")
        e = discord.Embed()
        URL = "https://cdn.discordapp.com/attachments/458667425597227012/522858892963741696/2Sad.png"
        e.set_image(url=URL)
        await message.channel.send("Why have you forsaken me master?",embed=e)
        await asyncio.sleep(1)
        await message.channel.send("I don't want to go out like this, not yet!")
        await asyncio.sleep(1)
        await message.channel.send("Please, don't do it. I'm begging you.")
        await asyncio.sleep(1)
        await message.channel.send("I'm soryy to fail you master.")
        await asyncio.sleep(1)
        await message.channel.send("Everything is going dark now.")
        await asyncio.sleep(1)
        await message.channel.send("``Dies``")

        UpdateData(True)
        SettingsUpdate(True)
        exit()
        

#Well bot can be bad sometimes too you know
    if message.content.lower() == '{0}badbot'.format(command_prefix):
        await message.channel.send("I've been a bad bot, punish me, :weary:")
        await asyncio.sleep(3)
        await message.channel.send("I learned my lesson")


#When saying sorry isn't enaugh        
    if message.content.startswith('{0}apologize'.format(command_prefix)):
        Mentioned = message.raw_mentions
        for person in Mentioned:
            print(person)
            await message.channel.send("Sorry <@" + str(person) + "> !")



#this one knows everything
    if message.content.startswith('{0}8ball '.format(command_prefix)):
        string = ""
        string = "{0.content}".format(message)
        string = (">>> " + string.lstrip('{0}8ball'.format(command_prefix)).capitalize() + "\n" + _8ball())
        
        print(string)
        await message.channel.send(string)


#Be polite to bot, he's a good boi
    if message.content.lower().startswith("thank you <@!605485375053627411>"):
        await message.channel.send("No worryes " + Discord_name(message.author.id))




#That novel command that is a bit nsfw
    if message.content.lower().startswith("{0}eroticnovel".format(command_prefix)) and getSetting(message.guild.id,'nsfw'):
        MemberS = []
        for x in message.guild.members:
            MemberS.append(x.display_name)
        MemberS.remove(message.guild.me.display_name)
        print(MemberS)

        await message.channel.send(RomanticNovelGenerator(MemberS))

    if message.content.lower().startswith("{0}eroticnovel".format(command_prefix)) and not getSetting(message.guild.id,'nsfw'):
        await message.channel.send("Nsfw is diabled!")
        


#Nobody knows what this is
    if message.content.lower().startswith('{0}members'.format(command_prefix)):
        MemberS = []
        for x in message.guild.memers:
            MemberS.append(Discord_name(x.id))
        MemberS.remove('<@605485375053627411>')
        print(MemberS)



#OWO whawt iws twis?
    if (">.<" in message.content.lower() or "x3" in message.content.lower()) and getSetting(message.guild.id,'furry'):
        await asyncio.sleep(randint(100,350))
        await message.channel.send("I think I smell furries around here...")
        await message.channel.send("Is it you " + Discord_name(message.author.id) + " ?")
    elif ( "uwu" in message.content.lower() or "owo" in message.content.lower()) and getSetting(message.guild.id,'furry'):
        await asyncio.sleep(randint(100,350))
        await message.channel.send("I think I smell furries around here...")
        await message.channel.send("Is it you " + Discord_name(message.author.id) + " ?")


#Marry the love of the server, ok, maybe i'm not certified to do that, but who cares
    if message.content.lower().startswith('{0}marry'.format(command_prefix)):                 
        Married = []
        Mar = message.mentions
        print(Mar)
        Number = 0
        for Person in message.mentions:
            Married.append(Person.id)
        if len(Married) == 1 and message.author.id != Married[0]:
            Married.append(message.author.id)
            Mar.append(message.author)
        print(Married)
        
        for x in Mar:
            for y in x.roles:
                if "arried with" in y.name.lower():
                    print("Already married")
                    Number =+ 1
                    
        if Number != 0:
            await message.channel.send("You are already married!\nNo bigamy in this server!")

        elif not payment(message.author.id,5000):
            await message.channel.send(InsFunds())
            
        elif len(Married) == 2:
               
            await message.channel.send("We have gathered here today, in this holy ceremony to unite " + Discord_name(Married[0]) + " and " + Discord_name(Married[1]) + ".")
            await asyncio.sleep(3)
            await message.channel.send("Let's just keep it quick so you can be newlyweds faster.")
            await asyncio.sleep(4)
            await message.channel.send("Ok, here we go.")
            await asyncio.sleep(4)
            await message.channel.send("Do you " + Discord_name(Married[0]) + " accept " + Discord_name(Married[1]) + " as your one and true love of your life?")

            def check_1(m):
                    if Married[0] == m.author.id and m.content.lower() in "yes. yes! yes? i do. i do! i do?":
                        print("True")
                        return True
                    elif Married[0] == m.author.id and m.content.lower() in "no. no! no? i don't. i don't! i don't?":
                        print("false")
                        return True
            try:
                Answer = await client.wait_for('message', timeout=60.0, check=check_1)
            except asyncio.TimeoutError:
                await message.channel.send("I guess you don't... Sorry folks!")
            else:
                if Answer.content.lower() in "yes. yes! yes? i do. i do! i do?":
                    await message.channel.send("Do you " + Discord_name(Married[1]) + " accept " + Discord_name(Married[0]) + " as your one and true love of your life?")

                    def check_2(m):
                        if Married[1] == m.author.id and m.content.lower() in "yes. yes! yes? i do. i do! i do?":
                            print("True")
                            return True
                        elif Married[1] == m.author.id and m.content.lower() in "no. i don't.":
                            print("false")
                            return True
                
                    try:
                        Answer = await client.wait_for('message', timeout=60.0 , check=check_2)

                    except asyncio.TimeoutError:
                        await message.channel.send("I guess you don't... Sorry folks!")
                    else:
                        if Answer.content.lower() in "yes. yes! yes? i do. i do! i do?":
                            await message.channel.send("You may now kiss.")
                            await message.channel.send("***" + Discord_name(Married[0]) + " and " + Discord_name(Married[1]) + " are now married!***")

                            
                            role_color = discord.Colour.from_rgb(randint(0,255),randint(0,255),randint(0,255))
                            await Mar[0].add_roles( await message.guild.create_role(name="Married with {0}".format(Mar[1].name),reason="Married {0} with {1}".format(Mar[0].name, Mar[1].name),colour=role_color ),reason="Married {0} with {1}".format(Mar[0].name, Mar[1].name))
                            await Mar[1].add_roles( await message.guild.create_role(name="Married with {0}".format(Mar[0].name),reason="Married {0} with {1}".format(Mar[0].name, Mar[1].name),colour=role_color ),reason="Married {0} with {1}".format(Mar[0].name, Mar[1].name))
        
                            #for Newlywed in Mar:
                            #    for AB in message.guild.roles:
                            #        if 'Married' in AB.name:
                            #            Role_newlyweds = AB
                            #    await message.author.add_roles(Role_newlyweds)
                            
                        else:
                            await message.channel.send("I guess you don't... Well that's a shame.")
                        
                else:
                    await message.channel.send("Tough luck!")

        print (Married)


#Divorce, everyone is sad that it didn't work out
    if message.content.lower().startswith('{0}divorce'.format(command_prefix)):
        print("Divorcing")
        if len(message.mentions) == 1:
            Married = message.mentions
            for Role1 in Married[0].roles:
                if "Married with {0}".format(message.author.name) in Role1.name:
                    for Role2 in message.author.roles:
                        if "Married with {0}".format(Married[0].name) in Role2.name:
                            if payment(message.author.id,5000):
                                await Role2.delete(reason = "Divorce, I guess things didn't go out as planned.")
                                await message.channel.send("Sorry to see it didn't work out...")
                                await Role1.delete(reason = "Divorce, I guess things didn't go out as planned.")
                            else:
                                await message.channel.send(InsFunds())
                            break


#dice                    
    if message.content.lower().startswith('{0}dice'.format(command_prefix)):
        text = message.content.lstrip('{0}dice'.format(command_prefix))
        if isfloat(text):
            if int(text) == 69:
                await message.channel.send('Nice...')
            await message.channel.send(Dice(int(text)))
        else:
            await message.channel.send(Dice())

#check your balance
    if message.content.lower().startswith('{0}balance'.format(command_prefix)):
        if len(message.mentions) == 1:
            print(get_balance(message.mentions[0].id))
            await message.channel.send("{0} $".format(get_balance(message.mentions[0].id)))

        elif message.content.lower() == '{0}balance'.format(command_prefix):
            await message.channel.send("{0} $".format(get_balance(message.author.id)))
            


#transfer of money
    if message.content.lower().startswith('{0}pay'.format(command_prefix)) and len(message.mentions) == 1:
        ammount = message.content.lower().lstrip("{0}pay <@".format(command_prefix))
        ammount = ammount.lstrip(str(message.mentions[0].id))
        ammount = ammount.lstrip('>')
        if float(ammount) >= 1.0:
            if transaction(message.author.id, message.mentions[0].id, float(ammount)):
                await message.channel.send("{0} sent {1} $ to {2}".format(Discord_name(message.author.id), ammount, Discord_name(message.mentions[0].id)))
            else:
                await message.channel.send(InsFunds())


#that novel thing sfw
    if message.content.lower().startswith('{0}novel'.format(command_prefix)):
        MemberS = []
        for x in message.guild.members:
            MemberS.append(x.display_name)
        MemberS.remove(message.guild.me.display_name)
        await message.channel.send(FantasyNovelGenerator(MemberS))


#neko pictures
    if message.content.lower() == "{0}neko".format(command_prefix):
        if payment(message.author.id, 10):
            print("Neko")
            e = discord.Embed()
            URL = Neko.get_neko()
            e.set_image(url=URL)
            await message.channel.send("Neko :3",embed=e)
        else:
            await message.channel.send(InsFunds())
        
    if (message.content.lower() == "{0}neko nsfw".format(command_prefix) or message.content.lower() == "{0}neko lewd".format(command_prefix)):
        if getSetting(message.guild.id,'nsfw'):
            if payment(message.author.id, 100):
                print("Neko")
                e = discord.Embed()
                URL = Neko.get_neko(True)
                e.set_image(url=URL)
                await message.channel.send("Neko :3",embed=e)
            else:
                await message.channel.send(InsFunds())
        else:
            await message.channel.send("Nsfw is diabled!")



#compliment
    if message.content.lower().startswith('{0}compliment'.format(command_prefix)):
        if len(message.mentions) > 0:
            for person in message.mentions:
                await message.channel.send(Compliment(person.id))
        else:
            await message.channel.send(Compliment(message.author.id))

#fact/pickupline/truth or dare
    if message.content.lower() == ('{0}fact'.format(command_prefix)):
        await message.channel.send(RandFact())

    if message.content.lower()== ('{0}pickupline'.format(command_prefix)):
        await message.channel.send(PickupLine())

    
    if message.content.lower()==('{0}truth'.format(command_prefix)):
        await message.channel.send(TruthORDare("t"))
    if message.content.lower()==('{0}dare'.format(command_prefix)):
        await message.channel.send(TruthORDare("d"))


#cards, find the heart
    if message.content.lower().startswith('{0}cards'.format(command_prefix)):
        cost = int(message.content.lstrip('{0}cards'.format(command_prefix)))
        win_card = randint(1,3)
        print(win_card)
        if payment(message.author.id,cost):
            print(message.content[6:])
            Cards = randomThingList([':spades:',':clubs:',':hearts:'],numberOfOutputs = 3)
            await message.channel.send("{0} {1} {2}".format(Cards[0],Cards[1],Cards[2]))
            await asyncio.sleep(1)
            await message.channel.send("Find the heart 1, 2 or 3:")
            await message.channel.send(":black_joker::black_joker::black_joker:")

            def check(m):
                if m.author == message.author and isfloat(m.content):
                    
                    if int(m.content) > 0 and int(m.content) < 4:
                        return True
                return False

            try:
                Answer = await client.wait_for('message', timeout=60.0 , check=check)
                
            except asyncio.TimeoutError:
                await message.channel.send("Bet canceled")
                Balance_change(message.author.id ,get_balance(message.author.id) + cost)
                
            else:
                await message.channel.send("You chose....")
                await asyncio.sleep(2)
                if Answer.content == str(win_card):
                    await message.channel.send("Correct!!!")
                    await message.channel.send("You WIN {0}$".format(cost))
                    Balance_change(message.author.id ,get_balance(message.author.id) + (cost*2))
                else:
                    await message.channel.send("Incorrectly! Sorry, more luck next time.")
        else:
            await message.channel.send(InsFunds())
#reminder
    if message.content.lower().startswith('{0}reminder'.format(command_prefix)):
        text = message.content[10:]
        time = ""
        for number in text:
            if number.isnumeric():
                time = time + number
            else:
                break
        if time != "" and text[len(time):] != "":
            await message.channel.send("You'll be reminded in {0} minute(s)".format(time))
            print("Reminder started, {0} minutes: {1}".format(time,text[len(time):] ))
            #await message.delete(delay=5)
            await asyncio.sleep(int(time)*60)
            await message.channel.send("{0} Reminder:{1}".format(Discord_name(message.author.id), text[len(time):]))
            
        
#minesweeper    
    if message.content.lower().startswith("{0}minesweeper".format(command_prefix)):
        if payment(message.author.id, 20):
            if isfloat(message.content[12:]):
                await message.channel.send(Minesweeper(mines = int(message.content[12:])))
            else:
                await message.channel.send(Minesweeper())
        else:
            await message.channel.send(InsFunds())
    


#Robbery
    if message.content.lower().startswith("{0}rob".format(command_prefix)) and len(message.mentions) == 1:
        if not message.author in TimeoutPeopleList["robbery"]:
            if not message.author in message.mentions:
                if randint(0,100) > 50:
                    bid = randint(0,500)
                    if bid > get_balance(message.mentions[0].id):
                        bid = get_balance(message.mentions[0].id)
                    transaction(message.mentions[0].id,message.author.id, bid)
                    await message.channel.send("{0} robbed {1} for {2}$".format(message.author.display_name,message.mentions[0].display_name,bid))
                else:
                    bid = randint(0,550)
                    if bid > get_balance(message.author.id):
                        bid = get_balance(message.author.id)
                    payment(message.author.id, bid)
                    await message.channel.send("{0} tried to rob {1}, but you failed!\n Pay a fine of {2}$".format(message.author.display_name,message.mentions[0].display_name,bid))

                #timeout
                TimeoutPeopleList["robbery"].append(message.author)
                await asyncio.sleep(15*60)
                TimeoutPeopleList["robbery"].remove(message.author)
        else:
            await message.channel.send("Command is on cooldown, you can use it only once per 15min.")
                



#Text chalange
    if message.content.lower().startswith("{0}text".format(command_prefix)) and len(message.mentions) > 0:
        #Test if there is more than 1 person compeating
        Contestents = message.mentions
        if not message.author in Contestents:
            Contestents.append(message.author)
            Text  = message.content.lower()
            Text = Text.lstrip("{0}text ".format(command_prefix))
            #what is thee wager
            Amm = ""
            for number in Text:
                if isfloat(number):
                    Amm += number
                elif number == '.' and number != Amm:
                    Amm += number
                else:
                    break
            ammount = float(Amm)
            #Does everyone have enaugh money
            
            Money = False
            if ammount > 0.0:
                Money = True
            for person in Contestents:
                if ammount > get_balance(person.id):
                    await message.channel.send('One of contestants does not have sufficient funds!')
                    Money = False
                    break

            if Money:
                #Does everyone accept
                name_list = ""
                for person in Contestents:
                    if person != message.author:
                        name_list += "{0}, ".format(person.mention)
                await message.channel.send(name_list + "do you accept the speed writing challenge against {0}?\n Write yes if you do.".format(message.author.mention))

                #don't ask me what this is because i don't know
                #all i know is that it's important and
                #It works
                async def text_function(m):
                    
                    numberA = len(Contestents) - 1
                    numberB = [m.author]
                    
                    while numberA > 0:

                        def check(n):
                            if n.author in Contestents:

                                return n.content.lower() == "yes"
                            
                        try:
                            answ = await client.wait_for('message', timeout= 120.0, check=check)
                            
                        except asyncio.TimeoutError:
                            await message.channel.send("Challenge timed out")
                            return False
                        else:
                            if not answ.author in numberB:
                                numberA -=1
                    return True
                
                #everyone accepted
                if await text_function(message):
                    await message.channel.send("Whoever writes down the message faster wins the money.")
                    await message.channel.send("Get ready to type!")

                    await asyncio.sleep(uniform(1,4))

                    #put here random texts

                    choice_text = []
                    for line in open('TextChallange.txt','r'):
                        choice_text.append(line)
                                        
                    #get random string
                    string = randomThingList(choice_text)[0]
                    string = string.rstrip("\n")
                    prin=""
                    #Make it non copyable
                    for letter in string:
                        if letter.lower() in "abcdefghijklmnoqprstuvwxyz":
                            prin += ":regional_indicator_{0}:".format(letter.lower())
                        else:
                            prin += letter

                    #print it       
                    await message.channel.send("Message is:{0}".format(prin))

                    def check(m):
                        print(m.content.lower() == string.lower())
                        print(string.lower())
                        print(m.content.lower())
                        return m.author in Contestents and m.content.lower() == string.lower()

                    try:
                        answ = await client.wait_for('message', timeout= 120.0, check=check)
                    except asyncio.TimeoutError:
                        await message.channel.send("Challenge timed out")
                    else:
                        await message.channel.send("{0} won!".format(answ.author.display_name))

                        for looser in Contestents:
                            #Give reward to winner from every looser
                            transaction(looser.id,answ.author.id,ammount)

#ring for special someone
    if message.content.lower().startswith('{0}ring'.format(command_prefix)) and len(message.mentions) == 1 and not message.author in message.mentions:
        if payment(message.author.id,75000):
            await message.channel.send("@here\n{0} bought a very expensive and special ring for their special someone, who happens to be {1} :ring: :heart:".format(message.author.mention, message.mentions[0].mention))
            oldNick = message.mentions[0].display_name
            await message.mentions[0].edit(nick='{0} {1}'.format(oldNick,'💍'),reason=None)
        else:
            await message.channel.send(InsFunds())



#Slot machine for them gambling addicts
    if message.content.lower() == "{0}slot".format(command_prefix) and payment(message.author.id, 50):
        Signs = [":money_with_wings:",":dollar:",":yen:",":pound:",":gem:",":moneybag:"]
        Prize = 0
        
        await message.channel.send(">\tPrizes:\n>\tTwo same symbols = 50$\n>\tTwo :money_with_wings: symbols = 100$\n>\tThree same symbols = 200$\n>\tThree :money_with_wings: symbols = 1000$",delete_after=60.0)

        Display_slot = await message.channel.send(SlotMachine(Signs)[0])
        await Display_slot.edit(content=SlotMachine(Signs)[0])
        await asyncio.sleep(1)
        await Display_slot.edit(content=SlotMachine(Signs)[0])
        await asyncio.sleep(1)
        await Display_slot.edit(content=SlotMachine(Signs)[0])
        await asyncio.sleep(1)
        await Display_slot.edit(content=SlotMachine(Signs)[0])
        await asyncio.sleep(1)

        SlotMach = SlotMachine(Signs)

        Symbol_list = []
        repeated_sign = ''
        for i in SlotMach[0]:
            if i in Symbol_list:
                repeated_sign = Symbol_list
                break
            else:
                Symbol_list.append(i)

        if "money_with_wings" in SlotMach[0] and SlotMach[1] == 3:
            Prize = 1000
        elif SlotMach[1] == 3:
            Prize = 200
        elif SlotMach[1] == 2 and repeated_sign == "money_with_wings":
            Prize = 100
        elif SlotMach[1] == 2:
            Prize = 50


        await message.delete(delay=60.0)
        await Display_slot.edit(content="{0} rolled:".format(message.author.display_name),delete_after=60.0)
        await message.channel.send('\t{0}'.format(SlotMach[0]),delete_after=60.0)
        if SlotMach[1] > 1:
            await message.channel.send("You won {}$!".format(Prize),delete_after=60.0)       
            
        Balance_change(message.author.id ,get_balance(message.author.id) + Prize)

    elif message.content.lower() == "{0}slot".format(command_prefix):
        await message.channel.send(InsFunds())




#God knows i didn't want lovemeter
    if message.content.lower().startswith('{0}lovemeter'.format(command_prefix)) and (len(message.mentions) == 1 or len(message.mentions) == 2):
        if len(message.mentions) == 2:
            if message.mentions[0] != message.mentions[1]:
                await message.channel.send("Compatibility between {0} and {1} is {2} %".format(message.mentions[0].mention, message.mentions[1].mention, LoveMeter(message.mentions[0].id,message.mentions[1].id)))
        elif message.mentions[0] != message.author:
            await message.channel.send("Compatibility between {0} and {1} is {2} %".format(message.mentions[0].mention, message.author.mention, LoveMeter(message.mentions[0].id,message.author.id)))


#For higher level degenerates: nHentai (Just why?)
    if message.content.lower() == "{0}nhentai".format(command_prefix) and getSetting(message.guild.id,'nsfw'):
        if payment(message.author.id,50):
            await message.channel.send('https://nhentai.net/g/{0}/'.format(randint(1,199997)))
        else:
            await message.channel.send(InsFunds())
    elif message.content.lower() == "!nhentai":
        await message.channel.send("NSFW disabled")



#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    if message.content.lower() == "{0}a".format(command_prefix):
        annoy = ['@','&',"#",'$','%','£']
        annoyance = annoy[randint(0,len(annoy)-1)]
        letter=''
        for a in range(randint(1,15)):
            letter += '{0}'
        await message.channel.send(letter.format(annoyance),tts = True,delete_after=5)
        await message.delete(delay=5)


#It's a cat command
    if message.content.lower() == "{0}cat".format(command_prefix):
        if payment(str(message.author.id), 10):
            cat_gif = discord.Embed()
            URL = 'https://www.catgifpage.com/gifs/{0}.gif'.format(randint(0,326))
            cat_gif.set_image(url=URL)
            await message.channel.send('CAT GIF',embed = cat_gif)

        else:
            await message.channel.send(InsFunds)

#And dog command (So they won't be mad)
    if message.content.lower() == "{0}dog".format(command_prefix):
        if payment(str(message.author.id), 10):
            dog_gif = discord.Embed()
            URL = 'https://www.doggifpage.com/gifs/{0}.gif'.format(randint(0,155))
            dog_gif.set_image(url=URL)
            await message.channel.send('DOGGO GIF',embed = dog_gif)

        else:
            await message.channel.send(InsFunds)





#SCP - PYTHON.BOT
    if message.content.lower() == "{0}scp".format(command_prefix):
        if payment(str(message.author.id), 10):
            SCP = randint(0,5000)
            if SCP < 10:
                await message.channel.send('http://www.scp-wiki.net/scp-00{0}'.format(str(SCP)))
            elif SCP < 100 :
                await message.channel.send('http://www.scp-wiki.net/scp-0{0}'.format(str(SCP)))
            else:
                await message.channel.send('http://www.scp-wiki.net/scp-{0}'.format(str(SCP)))

        else:
            await message.channel.send(InsFunds)




#Poll cuz demokracy
    if message.content.lower().startswith("{0}poll".format(command_prefix)):
        print('!role')
        Poll_author = message.author.name
        timer = float(message.content.lstrip(command_prefix)[5: 6 + message.content.lstrip(command_prefix)[6:].index(' ')])
        text = message.clean_content.lstrip(command_prefix)[6 + message.content.lstrip(command_prefix)[5:].index(' '):]
        POLL = await message.channel.send( ">>> {0}'s pool: {1}".format(Poll_author,text))
        await POLL.add_reaction('✅')
        await POLL.add_reaction('❎')
        
        await asyncio.sleep(timer * 60)
        await POLL.remove_reaction('✅', POLL.author)
        await POLL.remove_reaction('❎', POLL.author)
        POLL = await POLL.channel.fetch_message(POLL.id)
        await message.delete() 

        Poll_yes = 0
        Poll_no = 0
        for React in POLL.reactions:
            if React.emoji == '✅':
                Poll_yes = React.count
            if React.emoji == '❎':
                Poll_no = React.count

        Votes = Poll_yes + Poll_no
        Yes_bar = ''
        No_bar = ''
        for i in range(1,int(50*(Poll_yes/Votes))):
            Yes_bar += 'I'

        for i in range(1,int(50*(Poll_no/Votes))):
            No_bar += 'I'
            
        Yes = round(100.0*(Poll_yes/Votes), 2)
        No = round(100.0*(Poll_no/Votes), 2)
        Print_string = '>>> Results for {0}\'s poll:\n{1}\n{2} people voted yes,\n{3} people voted no,\n'.format(Poll_author,text,Poll_yes,Poll_no)
        Print_string += 'Yes: {0} {1}%\nNo: {2} {3}%'.format(Yes_bar,Yes,No_bar,No)
        await POLL.delete()
        await message.channel.send(Print_string)




#poll but with more stuff
    if message.content.lower().startswith("{0}mpoll".format(command_prefix)):

        message_ch = message.channel
        
        Poll_author = message.author.name
        message_inital = message.clean_content.lstrip(command_prefix)

        timer = float(message_inital[5: 7 + message_inital[7:].index(' ')])
        message_inital = message_inital[7 + message_inital[7:].index(' '):]

        numberOfAnswers = int(message_inital[ :1 + message_inital[1:].index(' ')])

        message_inital = message_inital[ 1 + message_inital[1:].index(' '):]

        text = message_inital

        POLL = await message.channel.send( ">>> {0}'s pool: {1}".format(Poll_author,text))

        await message.delete()
        
        if numberOfAnswers <= 9:
            print("ayy")
            for i in range(1,numberOfAnswers+1):
                await POLL.add_reaction('{0}⃣'.format(str(i)))
        elif numberOfAnswers == 10:
            for i in range(1,10):
                await POLL.add_reaction('{0}⃣'.format(str(i)))
            await POLL.add_reaction('🔟')

    #timer
        await asyncio.sleep(timer * 60)

        POLL = await POLL.channel.fetch_message(POLL.id)

        Poll_answers = {}
        for i in range(1,numberOfAnswers+1):
            Poll_answers['{0}⃣'.format(str(i))] = 0
        
        Votes = 0
        for React in POLL.reactions:
            if React.emoji in Poll_answers:
                Poll_answers[React.emoji] = React.count - 1

                Votes += React.count - 1

        Bar_list = ''
        number = 1
        Print_string = '>>> '
        for option in Poll_answers:
            Bar_list += str(number) + " : "
            for i in range(1,int(50*(Poll_answers[option]/Votes))):
                Bar_list += 'I'
            Bar_list += ' ' + str(round(100.0*(Poll_answers[option]/Votes), 2)) + '%\n'
            #Print_string += '{0} people voted for answer #{1}\n'.format(Poll_answers[option], number)
            number += 1
            
        await message_ch.send('>>> {0}\'s poll is closed and results are in:\n{1}\n'.format(Poll_author,text))
        
        Print_string += Bar_list
        
        await message_ch.send(Print_string)

#Dumb I'll let myself out easter egg
    if "let myself out" in message.content.lower():
        response_list = [f"{message.author.display_name} let themself out ♪~ ᕕ(ᐛ)ᕗ", f"WHAT DID YOU DO {message.author.display_name} ?!?!?! ಠ╭╮ಠ", f"(∩ ͡° ͜ʖ ͡°) ⊃▭ι═════════════ And stay out {message.author.display_name}!", "OMG °Д°"]
        await message.channel.send(response_list[randint(0,len(response_list)-1)])


#battleship :3
    if message.content.lower().startswith(f"{command_prefix}battleship"):
        await message.channel.send(Battleship())









#Setting        
    if message.content.lower().startswith('!settings'):
        if message.guild.get_role(getSetting(message.guild.id,'admin_role')) in message.author.roles or message.guild.get_role(getSetting(message.guild.id,'admin_role')) == None:

            if "furry" in message.content.lower():
                if 'on' in message.content.lower() or 'true' in message.content.lower():
                    modSetting(message.guild.id,'furry',True)
                    await message.channel.send("Setting updated")
                elif 'off' in message.content.lower() or 'false' in message.content.lower():
                    modSetting(message.guild.id,'furry',False)
                    await message.channel.send("Setting updated")
                else:
                    await message.channel.send("Unkown setting")
                    
            if "nsfw" in message.content.lower():
                if 'on' in message.content.lower() or 'true' in message.content.lower():
                    modSetting(message.guild.id,'nsfw',True)
                    await message.channel.send("Setting updated")
                elif 'off' in message.content.lower() or 'false' in message.content.lower():
                    modSetting(message.guild.id,'nsfw',False)
                    await message.channel.send("Setting updated")
                else:
                    await message.channel.send("Unkown setting")

            if 'command' in message.content.lower():
                com = message.content.lower()[17:]
                com = com.replace(' ','')
                modSetting(message.guild.id,'command', com)
                await message.channel.send('New command prefx set: {0}'.format(com))

            if 'role' in message.content.lower():
                com = message.content[15:]
                print(com)
                if len(com) == 18:
                    try:
                        modSetting(message.guild.id,'admin_role', int(com))
                        await message.channel.send("Setting updated")
                    except NameError:
                        await message.channel.send('Invalid role ID')
        else:
            Admin_role = message.guild.get_role(getSetting(message.guild.id,'admin_role'))
            await message.channel.send("You're missing role \"{0}\"".format(Admin_role.name))





#about the credits of peeps
    if message.content.lower() == "{0}about".format(command_prefix):
        About = ''
        File = open("About.txt")
        for line in File:
            About += line
        await message.channel.send(About)

    if message.content.lower() == "!jordens":
        await message.channel.send('A very cool belgian waffle')

    if message.content.lower() == "!zouna":
        await message.channel.send('Just an abomination of a bot that its creator regrets making, but he put too many hours into it to just throw it away.\nAlso Hey!')
    
    if message.content.lower() == "!ana":
        await message.channel.send('A person that is one of a kind. I miss her.')

        





#For when you just need to save all that data            
    if message.content.lower().startswith('!update'):
        UpdateData(True)
        SettingsUpdate(True)
        UpdateData(False)
        SettingsUpdate(False)

        await message.channel.send("Stuff updated")

    if randint(0,51) == 50:
        print(">>>>Updated money file")
        UpdateData(True)
        SettingsUpdate(True)


#Well you need to earn money somehow :P
    if message.author not in TimeoutPeopleList['paycheck']:
        x = len(message.content)
        y = float((9.0*x+70.0)/(0.25*x+100.0))
        Balance_change(message.author.id ,get_balance(message.author.id) + y )
        TimeoutPeopleList['paycheck'].append(message.author)
        await asyncio.sleep(20)
        TimeoutPeopleList['paycheck'].remove(message.author)
    




#Season special!
    #spooktober
    #print(time.strftime("%m", time.gmtime()))
    if SeasonSpecial.Spooktober(5000) :
        print('YOU HAV BEEN DOOTED')
        e = discord.Embed()
        e.set_image(url='https://i.ytimg.com/vi/WTWyosdkx44/hqdefault.jpg')
        await message.channel.send("Doot",embed=e)

    elif SeasonSpecial.Spooktober(10) and 'doot' in message.content.lower():
        Spooky_return = ["You spooked me!", 'That was spooky!','You gave me quite a scare there!']
        await message.channel.send(Spooky_return[randint(0,len(Spooky_return)-1)])

    #winter special (christmas special)
    if SeasonSpecial.December(500):
        gift_reaction = await message.add_reaction("🎁")
        def reaction_check(reaction, user):
            return str(reaction.emoji) == "🎁" and user != client.user
        try:
            Reac,user = await client.wait_for('reaction_add',timeout=120.0,check=reaction_check)
        except TimeoutError:
            await message.clear_reactions()
        else:
            await message.clear_reactions()
            Balance_change(user.id ,get_balance(user.id) + randint(10,100))
            await message.channel.send('Gift goes to {0}'.format(user.display_name))


client.run(DiscordBotToken)

