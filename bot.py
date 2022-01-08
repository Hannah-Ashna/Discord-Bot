# Work with Python 3.6
import discord
import os
import asyncio
import random
from imdb import IMDb
from datetime import datetime
from discord.ext import commands

# Environment Variables
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('CHANNEL_ID')

# Other Variables
watchList = []

# Discord Bot Setup Stuff
bot = commands.Bot(command_prefix="!")

# This is to keep the bot from falling asleep while hosted on Heroku.
# Obviously this can be removed once we move to a private host
# that won't time us out all the time ... 
async def stay_awake():
    await bot.wait_until_ready()
    while not bot.is_closed():
        now = datetime.now()
        print('Im awake!')

        if (now.hour == 12):
        
            channel = bot.get_channel(int(CHANNEL))
            await channel.send("Do your **Duolingo**, nerds...")

        await asyncio.sleep(1680) #runs every 28mins


# Command: Figure out if Jad is busy or not
@bot.command(
    name = "jad",
    brief = "Use this to figure out if Jad is available or not."
)
async def jad_availability(ctx):
    now = datetime.now()
    if (now.hour > 9 and now.hour < 17 and (now.weekday() != 5 and now.weekday() != 6)):
        await ctx.channel.send("He's probably at work but might still respond.")
    elif (now.hour > 9 and now.hour < 23):
        await ctx.channel.send("I mean he's probably free?")
    else:
        await ctx.channel.send("Jad's dead. F.")

# Command: Join the nightly watch party VIP list
@bot.command(
    name = "join",
    brief = "Use this to join the watch party VIP list!"
)
async def join_watch_party(ctx):
    UserName = (str(ctx.author)).split("#")
    if UserName[0] not in watchList:
        watchList.append(UserName[0])
        await ctx.channel.send("... Adding you to the **VIP** list")
    else:
        await ctx.channel.send("You're already on the list! Use `.Bail` to leave.")

# Command: Leave the nightly watch party VIP list
@bot.command(
    name = "bail",
    brief = "Use this to leave the watch party VIP list :("
)
async def leave_watch_party(ctx):
    UserName = (str(ctx.author)).split("#")
    if UserName[0] in watchList:
        watchList.remove(UserName[0])
        await ctx.channel.send("... damn, the **audacity**")
    else:
        await ctx.channel.send("You're not on the list! Use `.Me` to join.")


# Command: Show the list of members on the nightly watch party VIP list
@bot.command(
    name = "list",
    brief = "Use this to display the watch party VIP list."
)
async def show_watch_party(ctx):
    usersList = "**Joining us Tonight:**\n"
    for x in range (0, len(watchList)):
        usersList += "- " + watchList[x] + "\n"
    await ctx.channel.send(usersList)

# Command: Provide a random movie recommendation based on genre (IMDB)
@bot.command(
    name = "movie",
    brief = "Use this to get a random movie recommendation based on genre.",
    help = "Structure it like this: !movie (genre here)"
)
async def show_watch_party(ctx, arg):    
    ia = IMDb()
    search = arg.lower()
    movies = ia.get_keyword(search)     

    print("Number of Options: " + str(len(movies)))
        
    if (len(movies) == 0):
        await ctx.channel.send("No Movies Found")
    else:
        # Pick a random movie and print it
        await ctx.channel.send("**How about: **" + movies[random.randint(0, len(movies))]['title'])

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Greet the user
    if (message.content.lower().startswith("morning") or message.content.lower().startswith("mrnin") or 
        message.content.lower().startswith("mornin") or message.content.lower().startswith("g'day")):
        UserName = (str(message.author)).split("#")

        await message.channel.send("**Hello** " + UserName[0])
            
    # Call them out for sleeping too much! 
    if (message.content.lower().startswith("afternoon")):
        await message.channel.send("Damn ... took you long enough...")

    # Danny easter egg
    if (message.content.lower().startswith("danny")):
       await message.channel.send("Hee Hoo! Howdy doo!")
    
    # If nothing then process commands
    await bot.process_commands(message)

@bot.event
async def on_ready():
    now = datetime.now()
    print('Logged in as: ',bot.user.name, ' - ', now)

bot.loop.create_task(stay_awake())
bot.run(TOKEN)

