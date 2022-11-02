import discord 
import random
TOKEN = 'MTAzNjg2MjE4MjIwMzMyNjUzNQ.GSn2RK.g2C2V9jTTr0JM9U48AJ1BuE0uI4l79B_YfdfGE'
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.users}'.format(client))
#1036439896354725950
    general_channel = client.get_channel(1036439896354725950)
    await general_channel.send("Hello")
client.run(TOKEN)