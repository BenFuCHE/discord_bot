import discord 
import random
TOKEN = 'MTAzNjg2MjE4MjIwMzMyNjUzNQ.GPjAuZ.4f2m2uEOnuw_fQbxJW0ZFUuABlhTca8NiSJkg8'
intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.users}'.format(client))

@client.event 
async def on_message(message):
    id = client.get_guild(1036439895905939546)
    if message.author == client .user:
        return 

    if message.content.startswith('!hi'):
        await message.channel.send('hi')
    
    elif message.content == '!users':
        await message.channel.send(f""" Number of Members {id.member_count} """)

client.run(TOKEN)