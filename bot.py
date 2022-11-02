import discord 
import random
TOKEN = ''
intents = discord.Intents.default()
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print('We have logged in as {0.users}'.format(client))
#1036439896354725950
    #general_channel = client.get_channel(1036439896354725950)
    #await general_channel.send("Hello")
@bot.event
async def on_member_join(member):
    channel = bot.get_channel('1036439896354725950')
    await channel.send("Hello {user}, Welcome to the server!")
client.run(TOKEN)