# Discord Bot - The Lil' Assistant
Created this bot as part of a running gag with a few friends over the lockdown period.  
We would often greet each other every morning and go over our plans for the day. I decided to make us a bot that stores our to-do lists based on our discord **#Numbers**.
The bot allows users to add tasks and remove tasks and completely re-do their current list. In addition to that, the bot also has some easter egg (inside joke-based) commands.

The bot is currently being hosted via an **AWS EC2 Instance** instead of on **Heroku**

------------------------------------

### Commands List:
**Commands Help**  
Provides user with a list of tasks that the bot is able to do  
Syntax: `.help`

**Create Task list**  
Wipes any existing task list and starts fresh with a list of tasks.  
Syntax: `.SetTask, Task1, Task2, ..., TaskN`

**Add Task(s)**  
Appends the existing list of tasks to add new tasks.  
Syntax: `.AddTask, Task1, Task2, ..., TaskN`

**Delete Task(s)**  
Removes a task from the list based on its number in the list.  
Syntax: `.DeleteTask, TaskNum1, TaskNum2, ..., TaskNumN`

**View Task(s)**  
Syntax: `Morning, morning, mornin, mrnin, G'day, g'day`

**Show Band List**  
Syntax: `.bands`

**Add Bands to Band List**  
Syntax: `.AddBand, Name1, Name2, ..., NameN`

**Easter Egg**  
Created for those days where we'd sleep in instead of waking up early.  
Syntax: `afternoon`

-------------------------------

### Creator's Notes:
#### Using Heroku: 
You'll need to manually create temporary task lists for each user in the 'Users' folder. It is definitely a less than ideal process, however, it appears when the bot runs on heroku without any existing files in that folder none of the commands work.

#### Using AWS EC2 Instance:
Using a process manager like [PM2](https://www.npmjs.com/package/pm2) will allow for the bot to be run 24/7 even when you've closed your connection to the instance. Using the instance instead of Heroku prevents loss of data due to Heroku's frequent 24-hour resets. However, ensure that you frequently check up on your instance and do the ocassional 'maintenance' shutdown and restart if necessary. The main downside being the free trial ends after a year, and I havent fully examined the cost of running the bare minimum just yet.
