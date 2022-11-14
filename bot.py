import discord 
import datetime 
import time
TOKEN = ''
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

    if message.content.startswith('!math116'):
        m116_command = discord.Embed(title= 'Math 116')
        m116_command.add_field(name = 'TA Hours', value = 'Tuesday: 5:30 PM - 6:45')
        m116_command.add_field(name = 'Status', value = 'Virtual') 
        await message.channel.send(embed=m116_command)
    
    if message.content.startswith('!math115'):
        m115_command = discord.Embed(title= 'Math 115')
        m115_command.add_field(name = 'TA Hours', value = 'Monday: 11:30am - 12:20pm\nWednesday: 11:30am - 12:20pm\nFriday: 4:30pm - 5:20pm')
        m115_command.add_field(name = 'Status', value = 'Office: MC 6509') 
        await message.channel.send(embed=m115_command)
    
    if message.content.startswith('!che102'):
        c102_command = discord.Embed(title='CHE 102')
        c102_command.add_field(name = 'TA Hours', value = 'Thursday: 4:00pm - 5:00pm')
        c102_command.add_field(name = 'Status', value = 'Office: E6 5010') 
        await message.channel.send(embed=c102_command)
    
    if message.content.startswith('!che100'):
        c100_command = discord.Embed(title='CHE 100')
        c100_command.add_field(name= 'Instructor Hours', value = 'Prof. Tam: Thursday 3:30pm - 4:20pm\nProf. Moreoli: Monday 3:30pm - 4:20pm')
        c100_command.add_field(name = 'TA Hours', value = 'Bugra Birgili: Tuesday 4:00pm - 5:00pm\nKishore Kandasamy: Wednesday 11:30am - 12:20pm\nChristopher Sung: Wednesday 4:30pm - 5:20pm')
        c100_command.add_field(name = 'Office', value = 'Prof. Tam: QNC 5617\nProf. Moresoli: E6 4010\nBugra Birgili: E6-5110\nKishore Kandasamy: E6-5104\nChristopher Sung: E6-4120')
        await message.channel.send(embed=c100_command)

    if message.content.startswith('!WEEFTA' or '!che180'):
        weef_command = discord.Embed(title = 'WEEFTA')
        weef_command.add_field(name = 'WEEFTA', value = 'Monday: 8:30am - 6:00pm - Friday: 8:30am - 6:00pm')
        weef_command.add_field(name = 'Status', value = 'Office: E2 1792')
        await message.channel.send(embed=weef_command)

    if message.content.startswith('!che180'):
        weef_command = discord.Embed(title = 'CHE 180')
        weef_command.add_field(name = 'WEEFTA', value = 'Monday: 8:30am - 6:00pm - Friday: 8:30am - 6:00pm')
        weef_command.add_field(name = 'Status', value = 'Office: E2 1792')
        await message.channel.send(embed=weef_command)

    if message.content == '!users':
        await message.channel.send(f'Number of Members: {id.member_count}')
    
    if message.content.startswith('!help'):
        help_command = discord.Embed(title= 'Commands', colour=0x00ff00)
        help_command.add_field(name = 'Dates:',value = '!important dates\n!Due dates', inline=False)
        help_command.add_field(name = 'TA hours:', value='!math116\n!math115\n!che102')
        await message.channel.send(embed=help_command)
    
    if message.content.startswith('!setmeeting'):
        help_command = discord.Embed(title= 'Instructions', colour=0x00ff00)
        help_command.add_field(name = 'Step 1',value = '', inline=False)
        help_command.add_field(name = '', value='')
        await message.channel.send(embed=help_command)

@client.event
async def on_member_join(member):
    id = client.get_guild(1036439895905939546)
    channel = client.get_channel(1036439896354725950)
    await channel.send(f'Welcome to the server {member.mention}! ' + ':tada:'*3)
    await member.send(f"Welcome to {id.name}, {member.name}! Here's a list of commands to use on the server:")
    
    help_command = discord.Embed(title= 'Commands', colour=0x00ff00)
    help_command.add_field(name = 'TA Hours:',value = '!math116\n!math115\n!che102\n!che100\n!che120\n!che180\n!WEEFTA', )
    help_command.add_field(name = 'Important Dates:', value='')
    await member.send(embed=help_command)

client.run(TOKEN)