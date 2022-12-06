"""
Student Names: Ben Fu, Nabih Chaudry
Student ID'S: 20988871, 21009341
Project Title: Discord Bot
Date of Completion: December 6, 2022
"""

# Python libraries obtained from the discord website
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import math
from asyncio import sleep
import random

load_dotenv()

intents = discord.Intents().all()  # Setting up statement to run all privileges for the discord bot
intents.members = True  # Must be true, otherwise command prompts may not all function
status = 0

bot = commands.Bot(command_prefix='!', intents=intents) #changed built-in functions and client to 'bot', added prefix to call each command in discord
bot.remove_command('help') #removed built-in help command to implement custom one


def multi(x: float, y: float):  # Defintion's to perform arithmetic operations of datatype float
    return x * y


def addi(x: float, y: float):
    return x + y


def subt(x: float, y: float):
    return x - y


def divi(x: float, y: float):
    return x/y


def square(x: float):
    return math.sqrt(x)


@bot.event
async def on_ready():
    print('We have logged in as {0.users}'.format(bot))  # Inviation to welcome the bot on the server


@bot.event
async def on_member_join(member):  # Creating bot ID and allowing the joining of other users onto the servers
    id = bot.get_guild(1036439895905939546) #Specfic Bot ID, DO NOT SHARE UNLESS NEEDED TOO!!!
    channel = bot.get_channel(1036439896354725950)
    await channel.send(f'Welcome to the server {member.mention}! ' + ':tada:' * 3)  # Welcome message from the discord bot
    await member.send(f"Welcome to {id.name}, {member.name}! Here's a list of commands to use on the server:")

    commands = discord.Embed(title='Commands', colour=0xA020F0)  # commands variable is set for the user to see all possible commands the bot can perform
    commands.add_field(name='TA Hours:', value='!math116\n!math115\n!che102\n!che100\n!che120\n!che180\n!weef\n!reminderdetails\n!reminder\n!cancel\nmult')
    await member.send(embed=commands)


@bot.command()  # Definitions to perform operiations on data type float
async def mult(ctx, x: float, y: float):
    sol = multi(x, y)
    await ctx.send(sol)


@bot.command()  # Bot-command is the function definition from the discord library
async def add(ctx, x: float, y: float):
    sol = addi(x, y)
    await ctx.send(sol)


@bot.command()
async def sub(ctx, x: float, y: float):
    sol = subt(x, y)
    await ctx.send(sol)

@bot.command()
async def div(ctx, x: float, y: float):
    sol = div(x,y)
    await ctx.send(sol)

@bot.command()
async def root(ctx, x: float):
    sol = square(x)
    await ctx.send(sol)

@bot.command() #command to set a reminder and break time, continues to loop until specified to stop
async def reminder(ctx, time: int, *, x: int):
    global a
    a = 1 
    await ctx.send(f'```Reminder Set```')
    while a: 
        if a==1:
            await sleep(time)
        if a==2:
            break
        if a==1:
            await ctx.send(f'```Break Time```, {ctx.author.mention}')
        elif a==2:
            break 
        if a==1:
            await sleep(x)
        elif a==2:
            break 
        if a==1:
            await ctx.send(f'```Resume```')

@bot.command() #command to stop the loop 
async def cancel(ctx):
    global a
    a = 2
    await ctx.send(f'```Succesfully cancelled reminder```')


@bot.command()
async def reminderdetails(ctx):  # Reminder details is used to further elabaorate reminder to enter time and then take break
    embed = discord.Embed(title='How to set up a reminder')
    embed.add_field(name='Step 1 ', value='Use the command !reminder followed by the amount of time (in seconds) between each reminder and the message. Ex !reminder 45 time to take a break!')
    embed.add_field(name='Step 2', value='Use the command !cancel to cancel the reminder')
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx): # Help function is used to allow the user to see which course office hours are available
    embed = discord.Embed(title='Commands', colour=0x00ff00)
    embed.add_field(name='Dates:', value='!important dates\n!Due dates', inline=False)
    embed.add_field(name='TA hours:', value='!math116\n!math115\n!che102\n!che100\n!che120\n!che180\n!weef\n!reminderdetails\n!reminder\n!cancel\nmult')
    await ctx.send(embed=embed)


@bot.command() # Each course will output specfic office hours correpsonding to the course information found on learn
async def math116(ctx): 
    m116_command = discord.Embed(title='Math 116', colour=0xA020F0) # Discord bot will output dates, timing and location for the MATH 116 Course
    m116_command.add_field(name='TA Hours', value='Monday: 11:30am - 12:20pm \nWednesday: 4:30 pm - 5:20 pm') # New-line is used to format information
    m116_command.add_field(name='Office', value='Monday: MC 6169') 
    m116_command.add_field(name='Virtual', value='Tuesday: Zoom')
    await ctx.send(embed=m116_command)


@bot.command() # Each course will output specfic office hours correpsonding to the course information found on learn
async def math115(ctx):
    m115_command = discord.Embed(title='Math 115', colour=0xA020F0) # Discord bot will output dates, timing and location for the MATH 115 Course
    m115_command.add_field(name='TA Hours', value='Monday: 11:30am - 12:20pm\nWednesday: 11:30am - 12:20pm\nFriday: 4:30pm - 5:20pm') # New-line is used to format information
    m115_command.add_field(name='Status', value='Office: MC 6509')
    await ctx.send(embed=m115_command)


@bot.command() # Each course will output specfic office hours correpsonding to the course information found on learn
async def che102(ctx):
    c102_command = discord.Embed(title='CHE 102', colour=0xA020F0) # Discord bot will output dates, timing and location for the CHE 102 Course
    c102_command.add_field(name='TA Hours', value='Thursday: 4:00pm - 5:00pm') 
    c102_command.add_field(name='Status', value='Office: E6 5010')
    await ctx.send(embed=c102_command)


@bot.command() # Each course will output specfic office hours correpsonding to the course information found on learn
async def che100(ctx):
    c100_command = discord.Embed(title='CHE 100', colour=0xA020F0) # Discord bot will output dates, timing and location for the CHE 100 Course
    c100_command.add_field(name='Instructor Hours', value='Prof. Tam: Thursday 3:30pm - 4:20pm\nProf. Moreoli: Monday 3:30pm - 4:20pm') 
    c100_command.add_field(name='TA Hours', value='Bugra Birgili: Tuesday 4:00pm - 5:00pm\nKishore Kandasamy: Wednesday 11:30am - 12:20pm\nChristopher Sung: Wednesday 4:30pm - 5:20pm')
    c100_command.add_field(name='Office', value='Prof. Tam: QNC 5617\nProf. Moresoli: E6 4010\nBugra Birgili: E6-5110\nKishore Kandasamy: E6-5104\nChristopher Sung: E6-4120')
    await ctx.channel.send(embed=c100_command)


@bot.command() # Each course will output specfic office hours correpsonding to the course information found on learn
async def che180(ctx):
    c180_command = discord.Embed(title='WEEFTA', colour=0xA020F0) # Discord bot will output dates, timing and location for the CHE 180 Course
    c180_command.add_field(name='WEEFTA Hours', value='Monday: 8:30am - 6:00pm - Friday: 8:30am - 6:00pm') 
    c180_command.add_field(name='Status', value='Office: E2 1792')
    await ctx.send(embed=c180_command)

@bot.comand() # Each course will output specfic office hours correpsonding to the course information found on learn
async def che120(ctx):
    c120_command = discord.Embed(title='CHE 120', colour=0xA020F0) # Discord bot will output dates, timing and location for the CHE 120 Course
    c120_command.add_field(name='Instructor Hours', value='Tuesday: 4:00pm- 6:00pm') 
    c120_command.add_feild(name='Status', value='Office: E6 2016')
    await ctx.send()

@bot.command() # Each course will output specfic office hours correpsonding to the course information found on learn
async def weef(ctx):
    weef_command = discord.Embed(title='WEEFTA', colour=0xA020F0) # Discord bot will output dates, timing and location for the WEEF TA'S
    weef_command.add_field(name='WEEFTA', value='Monday: 8:30am - 6:00pm - Friday: 8:30am - 6:00pm') 
    weef_command.add_field(name='Status', value='Office: E2 1792')
    await ctx.send(embed=weef_command)


bot.run(os.getenv('bot_token'))  #Bot-token must be enabled in order to tell the IDE what code the bot is taking, used env to hide bot-token