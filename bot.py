import discord 
import random
TOKEN = 'MTAzNjg2MjE4MjIwMzMyNjUzNQ.GnvPAn.9Ouj7UnlT43QAavtNumFPWNJFz4Kz-HX5jVhKg'
intents = discord.Intents.default()
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print('We have logged in as {0.users}'.format(client))
#1036439896354725950
    general_channel = client.get_channel(1036439896354725950)
    await general_channel.send("Hello")
client.run(TOKEN)