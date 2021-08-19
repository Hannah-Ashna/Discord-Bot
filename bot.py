# Work with Python 3.6
import discord
import os
import asyncio
from datetime import datetime

TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Client()
watchParty = discord.Embed(title = "Watch Party List:")
watchList = []
async def stay_awake():
    await bot.wait_until_ready()
    while not bot.is_closed():

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        start_time = "13:00:00"
        end_time = "14:00:00"

        channel = bot.get_channel(874759682839937024)
        
        # Setup the watchParty list
        if (current_time > start_time and current_time < end_time):
            await channel.send("Current watch party list is empty!\nDo .Me to join...")
        
        # Reset the watchParty list for the next day
        elif (current_time < start_time):
            watchParty = []
            watchParty = discord.Embed(title = "Watch Party List:")

        else:
            await channel.send(embed = watchParty)

        print('Im awake!')
        await asyncio.sleep(1680) #runs every 28mins


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Greet the user and show them their tasks for the day
    if (message.content.startswith("Morning") or message.content.startswith("morning") or message.content.startswith("mrnin") 
        or message.content.startswith("mornin") or message.content.startswith("Mornin") or message.content.startswith("G'day") or message.content.startswith("g'day")):
        UserName = (str(message.author)).split("#")
        await message.channel.send("**Hello** " + UserName[0])
        
    # Call them out for sleeping too much! 
    if (message.content.startswith("afternoon")):
        await message.channel.send("Damn ... took you long enough...")

    # Add a server member to the watch party list
    if (message.content.startswith(".Me")):
        UserName = (str(message.author)).split("#")
        if UserName[0] not in watchList:
            watchList.append(UserName[0])
            await message.channel.send("... Adding you to the **VIP** list")
        else:
            await message.channel.send("You're already on the list! Use `.Bail` to leave.")

    # Remove a server member from the watch party list
    if (message.content.startswith(".Bail")):
        UserName = (str(message.author)).split("#")
        if UserName[0] in watchList:
            watchList.remove(UserName[0])
            await message.channel.send("... damn, the **audacity**")
        else:
            await message.channel.send("You're not on the list! Use `.Me` to join.")

    # Display current watch party list attendees
    if (message.content.startswith(".Partylist")):
        usersList = "**Joining us Tonight:**"
        for x in range (0, len(watchList)):
            usersList += watchList[x] + "\n"
        await message.channel.send(usersList)



async def on_ready():
    print('Logged in as: ',bot.user.name)

bot.loop.create_task(stay_awake())
bot.run(TOKEN)