import discord 
import random
TOKEN = 'MTAzNjg2MjE4MjIwMzMyNjUzNQ.GSn2RK.g2C2V9jTTr0JM9U48AJ1BuE0uI4l79B_YfdfGE'
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.users}'.format(client))
client.run(TOKEN)