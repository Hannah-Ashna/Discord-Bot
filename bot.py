# Work with Python 3.6
import discord
import os
import asyncio
import random
from datetime import datetime
from imdb import IMDb

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('CHANNEL_ID')

bot = discord.Client()
watchList = []

async def stay_awake():
    await bot.wait_until_ready()
    while not bot.is_closed():

        print('Im awake!')
        now = datetime.now()

        if (now.hour == 13):
            await CHANNEL.send("Do your Duolingo!")

        await asyncio.sleep(1680) #runs every 28mins

        


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Greet the user and show them their tasks for the day
    if (message.content.lower().startswith("morning") or message.content.lower().startswith("mrnin") or 
        message.content.lower().startswith("mornin") or message.content.lower().startswith("g'day")):
        UserName = (str(message.author)).split("#")

        await message.channel.send("**Hello** " + UserName[0])
            
    # Call them out for sleeping too much! 
    if (message.content.lower().startswith("afternoon")):
        await message.channel.send("Damn ... took you long enough...")

    # Add a server member to the watch party list
    if (message.content.lower().startswith(".join")):
        UserName = (str(message.author)).split("#")
        if UserName[0] not in watchList:
            watchList.append(UserName[0])
            await message.channel.send("... Adding you to the **VIP** list")
        else:
            await message.channel.send("You're already on the list! Use `.Bail` to leave.")

    # Remove a server member from the watch party list
    if (message.content.lower().startswith(".bail")):
        UserName = (str(message.author)).split("#")
        if UserName[0] in watchList:
            watchList.remove(UserName[0])
            await message.channel.send("... damn, the **audacity**")
        else:
            await message.channel.send("You're not on the list! Use `.Me` to join.")

    # Display current watch party list attendees
    if (message.content.lower().startswith(".partylist")):
        usersList = "**Joining us Tonight:**\n"
        for x in range (0, len(watchList)):
            usersList += "- " + watchList[x] + "\n"
        await message.channel.send(usersList)

    # Danny easter egg
    if (message.content.lower().startswith("danny")):
       await message.channel.send("hee hoo")

    # Jad busy command
    if (message.content.lower().startswith(".jadbusy?")):
        now = datetime.now()
        
        if (now.hour > 9 & now.hour < 17 & (now.weekday() != 5 & now.weekday() != 6)):
            await message.channel.send("He's probably at work but might still respond.")
        elif (now.hour > 9 & now.hour < 23):
            await message.channel.send("I mean he's probably free?")
        else:
            await message.channel.send("Jad's dead. F.")

    # Movie Suggestions
    if (message.content.lower().startswith(".findmovie")):
        ia = IMDb()
        search = message.content.lower()[11::]
        search = search.replace(' ', '-')
        movies = ia.get_keyword(search)
        
        print("Number of Options: " + str(len(movies)))
        
        if (len(movies) == 0):
            await message.channel.send("No Movies Found")
        else:
            # Pick a random movie and print it
            await message.channel.send("**How about: **" + movies[random.randint(0, len(movies))]['title'])
            

async def on_ready():
    print('Logged in as: ',bot.user.name)

bot.loop.create_task(stay_awake())
bot.run(TOKEN)
