import discord 
import random
from discord.ext import commands
TOKEN = ''
intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.users}'.format(client))

@client.event 
async def on_message(message):
    id = client.get_guild(1036439895905939546)
    if message.author == client.user:
        return 

    if message.content.startswith('!hi'):
        await message.channel.send('hi')
    
    elif message.content == '!users':
        await message.channel.send(f" Number of Members {id.member_count} ")
    
    if message.content.startswith('!help'):
        help_command = discord.Embed(colour=0x00ff00)
        help_command.add_field(name = 'Commands:', value = '!important dates\n!TA hours\n!Due dates', inline=False)
        await message.channel.send(embed=help_command)

client.run(TOKEN)