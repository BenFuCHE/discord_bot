import discord 
TOKEN = 'MTAzNjg2MjE4MjIwMzMyNjUzNQ.G7_hyk.ZvXwLIJ8sErOg3rQu2ixCfyPj4umhUDxWwCbbY'
intents = discord.Intents().all()
intents.members = True
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
        await message.channel.send(f'Number of Members: {id.member_count}')
    
    if message.content.startswith('!help'):
        help_command = discord.Embed(colour=0x00ff00)
        help_command.add_field(name = 'Commands:', value = '!important dates\n!TA hours\n!Due dates', inline=False)
        await message.channel.send(embed=help_command)

@client.event
async def on_member_join(member):
    id = client.get_guild(1036439895905939546)
    channel = client.get_channel(1036439896354725950)
    await channel.send(f'Welcome to the server {member.mention}! ' + ':tada:'*3)
    await member.send(f'Welcome to {id.name}, {member.name}!')

client.run(TOKEN)