# Step 2 : Setting up a basic BOT

In this second step, we will start coding and trying to make our bot go online.

## Step 2.1 : Importing libraries

We will need to import a few different libraries so that we can run our bot.

The different libraries you need to begin are :

```os``` : to import our environement variable where our bot's token is stored not to leak it anywhere  
```discord``` : obviously used to run your bot  
```commands``` (import from ```discord```) : This will help you modify your command prefix.  
Don't worry, we'll explain it to you in just a moment

## Step 2.2 : Environement & Prefixes

Our app needs to be secured, so nobody would have access to our token if they happen to find the source code.  
Take a look at these links, there might be useful informations.

https://realpython.com/how-to-make-a-discord-bot-python/#interacting-with-discord-apis
https://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html

If you need to find your bot's token, go back to https://discord.com/developers/applications,   
click on your app, then on BOT and finally on **Copy** under the **Token** section.  

You should have something like ```ODM4MDk1OTE4Mzk2OTk3NjYy.043Mz5_NCh.6bNmi_h1zFaZYI2Hpg44fxc```

Great. Now you have stored your token in an environment variable and you're able to get it from your python program.

## Step 2.2 : Start the bot

If you're here, you've probably checked the different links we gave to you in the previous steps.  
You might have noticed that there were pieces of codes.  

Are you able to start your bot and print a message in your terminal ?




Hint : Your bot needs to be **ready** to start working. You also need to **run** it with your token.... got it?
