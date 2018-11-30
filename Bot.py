import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import datetime as dt
from urllib.request import urlopen

Client = discord.Client
client = commands.Bot(command_prefix = ">")




@client.event
async def on_ready():
    print ("Bot is ready")


@client.event
async def on_message(message):
    userID = message.author.id
    if userID == '300092893060661251' and message.content.lower() == "begin":
        mynum=0
        mylist = list()
        while mynum < 3000:
            mylist.append(mynum)
            mynum+=1

        while True:
            now = dt.datetime.now()
            curday = now.day
            yesterday = curday
            curmonth = now.month
            allmonths = {
                1:"January",
                2:"February",
                3:"March",
                4:"April",
                5:"May",
                6:"June",
                7:"July",
                8:"August",
                9:"September",
                10:"October",
                11:"November",
                12:"December",


                }
            link = "https://en.wikipedia.org/wiki/"+allmonths[curmonth]+"_"+str(curday)+"#Events"

            
            f = urlopen(link)
            myfile = str(f.read())
            #myfile = myfile.replace('<a href="/wiki/', "")
            #myfile = myfile.replace('_', " ")
            #myfile = myfile.replace('title=', "")

            myfile = myfile.replace('"', "")

            num1 =myfile.index('id=Births')
            num2 =myfile.index("Edit section: Events")
            #print(myfile)
            myfile = myfile[num2:num1]
            myfile = myfile.split("&#8211;")
            myfile.remove(myfile[0])
            fulllist = list()
            for line in myfile:
                removemode = False
                line = line.replace('758', "")
                line = line.replace('\\xe2\\x80\\x93', " ")
                line = line.replace('\\n', "")
                line = line.replace('R\\xc3\\xado', "")
                line = line.replace('\\xc5\\x82\\xc5\\xbcec', "")
                line = line.replace('<span class=mw-headline', "")
                line = line.replace('\\', "")
                for i in range(line.count('<')):
                    try:
                        start = line.find('<')
                        end = line.find('>', start+1)
                        line = line[:start] + line[end+1:]
                    except:
                        pass
                if line[-5:] in mylist:
                    line = line[:-2]
                fulllist.append(line)
            while yesterday == curday:
                
                await client.send_message(message.channel, random.choice(fulllist))
                time.sleep(60*60*6)



        

client.run("NTE3OTk4ODkwNTE2MDg2Nzg5.DuKY3g.A4aFtiqZPB0ypbkfYHJj9nLJxP0")




