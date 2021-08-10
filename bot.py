# Work with Python 3.6
import discord
import os
import asyncio
from datetime import datetime

TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Client()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Greet the user and show them their tasks for the day
    if (message.content.startswith("Morning") or message.content.startswith("morning") or message.content.startswith("mrnin") 
        or message.content.startswith("mornin") or message.content.startswith("Mornin") or message.content.startswith("G'day") or message.content.startswith("g'day")):
        await message.channel.send("Hello Human ;)")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.channel.send("Current Time =", current_time)
        
    # Call them out for sleeping too much! 
    if (message.content.startswith("afternoon")):
        await message.channel.send("Damn ... took you long enough... time to look at your tasks!")

    # Provide list of commands using .help
    if (message.content.startswith(".help")):
        helpCommand = discord.Embed(title = "Commands List:")
        helpCommand.add_field(name = ".SetTask", value = "Make a to-do list using \n.SetTask, Task1, Task2, ...", inline = False)
        helpCommand.add_field(name = ".AddTask", value = "Add items to the to-do list \n.AddTask, Task1, Task2, ...", inline = False)
        helpCommand.add_field(name = ".DeleteTask", value = "Remove items from the to-do list \n.DeleteTask, Task1, Task2, ...", inline = False)
        helpCommand.add_field(name = ".Bands", value = "This displays the band names list", inline = False)
        helpCommand.add_field(name = ".AddBand", value = "Add a band name to the list \n.AddBand, Task1, Task2, ...", inline = False)
        await message.channel.send(embed = helpCommand)

async def on_ready():
    print('Logged in as: ',bot.user.name)
    
bot.run(TOKEN)