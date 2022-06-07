from discord.ext import commands
from discord.ext import tasks
import discord
import random
import HistoryBot
import time
import datetime

botToken = "PUT TOKEN HERE"
channelID = PUT CHANNEL ID HERE

prefix = "Unused Prefix"
bot = commands.Bot(command_prefix=prefix)

goodNightTime = datetime.time(hour=23, minute=54, second=30)

@tasks.loop(hours=24, minutes=0)
async def dailyReminder():
    today = datetime.date.today()
    today = today.strftime("%B %d")
    channel = bot.get_channel(channelID)
    
    await channel.send("Today is " + today + ", here are some interesting facts that happened in history on this day!")
    await channel.send("If you want to see more facts just type '>fact'")
    
    

@tasks.loop(hours=6, minutes=0)
async def eventChain(): 
    eventList = HistoryBot.getEventList()
    channel = bot.get_channel(channelID)
    await channel.send(random.choice(eventList))

@bot.event
async def on_ready():
    threadStarted = False
    print("Startup Succesful")
    dailyReminder.start()
    eventChain.start()
    
    if 1==2:
        eventList = HistoryBot.getEventList()
        channel = bot.get_channel(channelID)
        await channel.send(random.choice(eventList))

        
@bot.event
async def on_message(message):

    if message.content.lower() == ">fact":
        eventList = HistoryBot.getEventList()
        channel = bot.get_channel(channelID)
        await channel.send(random.choice(eventList))
    
    await bot.process_commands(message)
    

async def eventThread():
    while True:
        channel = bot.get_channel(channelID)
        await channel.send(random.choice(eventList))
        time.sleep(10)

bot.run(botToken)
