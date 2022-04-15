# Discord Bot - The Lil' Assistant 
Created this bot as part of a running gag with a few friends over the lockdown period. 
This bot was originally a to-do list reminder bot but has now been reworked to fit our needs as a group on discord. The bot will now send a daily reminded to ask us if we're available for a watch party session in the evening; it gives us the option to add our name to the watch party list. Slightly before the call is scheduled to begin it will send us another reminder with the list of attending members for the evening.

In addition to this primary function, the bot also has some easter egg (inside joke-based) commands.

The bot was previously hosted on an **AWS EC2 Instance** however due to hosting costs I have managed to move it back to **Heroku**.

------------------------------------

### Commands List:
**Commands Help**  
Provides user with a list of tasks that the bot is able to do  
Syntax: `.help`

**Join Daily Watchparty**  
Adds your Discord username to the watchparty list.    
Syntax: `.join`

**Leave Daily Watchparty**  
Removes your Discord username from the watchparty list.   
Syntax: `.bail`

**Show Daily Watchparty Attendees List**  
Displays a list of all members that want to join the daily watchparty.   
Syntax: `.partylist`

**Danny Bot says Hi**  
Syntax: `Morning, morning, mornin, mrnin, G'day, g'day`

**Easter Egg**  
Created for those days where we'd sleep in instead of waking up early.  
Syntax: `afternoon`

-------------------------------

### Creator's Notes:
#### Using Heroku: 
You'll need to manually create temporary task lists for each user in the 'Users' folder. It is definitely a less than ideal process, however, it appears when the bot runs on heroku without any existing files in that folder none of the commands work.
