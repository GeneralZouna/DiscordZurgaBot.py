from Pet import *
from Settings import *
from Economy import *
from time import time

Pet_list = Load_pet()


async def PetInterface(message):
    command_prefix = getSetting(message.guild.id,'command')

    if message.content.lower().startswith(f'{command_prefix}pet') and len(message.mentions) == 1:

        await message.channel.send(Pet_list[str(message.mentions[0].id)].Status())

    elif message.content.lower().startswith(f'{command_prefix}pet') and len(message.mentions) >= 1:
        pass

    elif message.content.lower().startswith(f'{command_prefix}pet'):
        
        if not (str(message.author.id) in Pet_list):
            Pet_list[str(message.author.id)] = Pet()

        Action = message.content.lower().replace(f'{command_prefix}pet ','')
        print(f'{message.author.display_name}:{Action}')
        
        if Action == "play":
            await message.channel.send(Pet_list[str(message.author.id)].Play('play'))
        
        elif Action == 'pet':
            await message.channel.send(Pet_list[str(message.author.id)].Play('pet'))
        
        elif Action == 'feed':
            await message.channel.send(Pet_list[str(message.author.id)].Feed())
        
        elif Action.startswith('rename'):
            New_name = message.content.lstrip(f'{command_prefix}pet rename ')
            Old_name = Pet_list[str(message.author.id)].Name
            Pet_list[str(message.author.id)].Name = New_name
            await message.channel.send(f'{Old_name} changed name to {New_name}')
        
        elif Action == 'kill':
            Pet_list[str(message.author.id)].HP = 0.0
            await message.channel.send(Pet_list[str(message.author.id)].Status())

        elif Action == 'medicine' and payment(str(message.author.id), 1000.0):
            Pet_list[str(message.author.id)].HP = 100.0
            await message.channel.send('Your pet has been healed')

        elif Action == 'medicine':
            await message.channel.send(InsFunds())

        elif Action == 'revive' and payment(str(message.author.id), 25000.0):
            Pet_list[str(message.author.id)].Status()
            Pet_list[str(message.author.id)].Alive = True
            Pet_list[str(message.author.id)].HP = 100.0
            Pet_list[str(message.author.id)].Hunger = 50.0
            Pet_list[str(message.author.id)].Last_time = int(time())
            await message.channel.send(f"By the power of an ancient ritual, {message.author.mention}'s pet has been revived")

        elif Action == 'revive':
            await message.channel.send("Miracles don't happen for free you know...")

        else:
            await message.channel.send(Pet_list[str(message.author.id)].Status())

    
    if message.content.lower().startswith(f'!save_pets'):
        SavePetList(Pet_list)
        await message.channel.send('Update done!')

    if randint(0,2700) > 2500:
        SavePetList(Pet_list)
