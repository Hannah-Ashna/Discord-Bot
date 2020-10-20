# Work with Python 3.6
import discord
import os
import asyncio

TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Client()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Greet the user and show them their tasks for the day
    if (message.content.startswith("Morning") or message.content.startswith("morning") or message.content.startswith("mrnin") 
        or message.content.startswith("mornin") or message.content.startswith("G'day") or message.content.startswith("g'day")):
        await message.channel.send("Hello Human ;)")
        try:
            UserName = (str(message.author)).split("#")
            FileName = "Users/" + UserName[1] + '.txt'
            TasksOutput = "**Pending Tasks:**\n"
            TasksFile = open(FileName,"r")
            for line in TasksFile:
                TasksOutput = TasksOutput + line
            await message.channel.send(TasksOutput)
            TasksFile.close()
            
        except:
            print("Couldn't read from Tasks.txt")
        
    # Call them out for sleeping too much! 
    elif (message.content.startswith("afternoon")):
        await message.channel.send("Damn ... took you long enough... time to look at your tasks!")

    # Provide list of commands using .help
    if (message.content.startswith(".help")):
        helpcommand = discord.Embed(title = "Commands List:")
        helpcommand.add_field(name = ".SetTask", value = "Make a to-do list using **.SetTask, Task1, Task2, ...", inline = False)
        helpcommand.add_field(name = ".AddTask", value = "Add items to the to-do list **.AddTask, Task1, Task2, ...", inline = False)
        helpcommand.add_field(name = ".DeleteTask", value = "Remove items from the to-do list **.DeleteTask, Task1, Task2, ...", inline = False)
        await message.channel.send(embed = helpcommand)
        
    # Let the user set their task
    if (message.content.startswith(".SetTask")):
        await message.channel.send("Storing your tasks ...")
        
        try:
            # Split the number from the name and use the number to create a .txt file
            UserName = (str(message.author)).split("#")
            FileName = "Users/" + UserName[1] + '.txt'
            TasksFile = open(FileName, "w")
            
            # Store entire message content in msg
            msg = message.content
            # Split message by comma
            Tasks = msg.split(', ')
            # Loop through the Tasks and store each one in the designated text file
            for i in range (1, len(Tasks)):
                TasksFile.write("[" + str(i) + "] - " + Tasks[i] + " \n")
            TasksFile.close()
            
            # Inform the user of the success
            await message.channel.send("Success!")
            
        # If there's an error let the user know
        except:
            print("Couldn't Set Tasks")
            await message.channel.send("Well .. that didn't work as planned")
    
    # Let the user add to their task list   
    if (message.content.startswith(".AddTask")):
        await message.channel.send("Adding that task ...")
        
        try:
            # Split the number from the name and use the number to find the specific .txt file
            UserName = (str(message.author)).split("#")
            FileName = "Users/" + UserName[1] + '.txt'
            
            # Open the file to read first to get the number of lines
            TasksFile = open(FileName, "r")
            count = len(TasksFile.readlines()) + 1
            TasksFile.close()
            
            # Open the file again, this time to append
            TasksFile = open(FileName, "a+")
            msg = message.content
            Tasks = msg.split(', ')
            for i in range (1, len(Tasks)):
                # Use count to add the correct numbers to the tasks
                TasksFile.write("[" + str(count) + "] - " + Tasks[i] + " \n")
                count = count + 1
            TasksFile.close()
            # Inform the user of the success
            await message.channel.send("Success!")
            
        # If there's an error let the user know
        except:
            print("Couldn't Set Tasks")
            await message.channel.send("Well .. that didn't work as planned")
            


    # Let the user remove a task from their list  
    if (message.content.startswith(".DeleteTask")):
        await message.channel.send("Deleting item(s) ...")
        
        
        try:
            # Split the number from the name and use the number to find the specific .txt file
            UserName = (str(message.author)).split("#")
            FileName = "Users/" + UserName[1] + '.txt'
            
            
            # Store entire message content in msg
            msg = (str(message.content)).split(", ")
            for i in range (1, len(msg)):
                TasksFile = open(FileName, "r+")
                Item = "[" + msg[i] + "]"
                print (Item)
                lines = TasksFile.readlines()
                TasksFile.seek(0)
                lastIndex = 0
                for line in lines:
                    if Item not in line:
                        # if the item index-1 is above previous index's, subtract 1 from index
                        # only does it on the final item to avoid overwriting items before everything's deleted
                        if int(line[1])-1 > int(lastIndex) and i == len(msg) - 1:
                            line = '[' + str(lastIndex + 1) + line[2:len(line)]
                        TasksFile.write(line)
                        lastIndex = int(line[1])
                TasksFile.truncate()
                TasksFile.close()
            
        except:
            print("Couldn't Remove Item")
            await message.channel.send("Well .. that didn't work as planned")
            

    # Let the user view the bands list   
    if (message.content.startswith(".Bands")):
        await message.channel.send("Adding that task ...")
        try:
            FileName = "BandNames.txt"
            File = open(FileName,"r")
            bands = discord.Embed(title = "Band Names:")
            for line in File:
                bands.add_field(name = "", value = line, inline = False)
            await message.channel.send(embed = bands)

        except:
            print("Couldn't get band list")
            await message.channel.send("That's weird ... the band list is unavailable?")


async def on_ready():
    print('Logged in as: ',bot.user.name)
    
bot.run(TOKEN)
