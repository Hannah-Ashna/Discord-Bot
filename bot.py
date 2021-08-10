# Work with Python 3.6
import discord
import os
import asyncio
from datetime import datetime

TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Client()

async def stay_awake():
    await bot.wait_until_ready()
    while not bot.is_closed():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        channel = bot.get_channel(820446444841730111)
        if (current_time > "21:25:00"):
            watchParty = discord.Embed(title = "Watch Party List:")
            watchParty.add_field(name = "aaaa", value = "aaaaa", inline = False)
            
            await channel.send(embed = watchParty)
        
        else:
            await channel.send("hee hoo")
        
        print('Im awake :)')
        await asyncio.sleep(1680) #runs every 28mins.


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Greet the user and show them their tasks for the day
    if (message.content.startswith("Morning") or message.content.startswith("morning") or message.content.startswith("mrnin") 
        or message.content.startswith("mornin") or message.content.startswith("Mornin") or message.content.startswith("G'day") or message.content.startswith("g'day")):
        
        await message.channel.send("Hello H0M0")
        
    # Call them out for sleeping too much! 
    if (message.content.startswith("afternoon")):
        await message.channel.send("Damn ... took you long enough...")

async def on_ready():
    print('Logged in as: ',bot.user.name)

bot.loop.create_task(stay_awake())
bot.run(TOKEN)