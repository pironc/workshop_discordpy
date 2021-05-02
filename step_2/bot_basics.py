# importing libraries
import discord
from discord.ext import commands, tasks
import os

# This will be the prefix so the bot know when you are sending a command
client = commands.Bot(command_prefix = '!')

# This is a basic event, to know when the bot is up and running
@client.event
async def on_ready():
    print("The bot is ready")

# This is a custom command (cf. "your_command")
@client.command()
async def your_command(ctx):
    # This is your channel ID for this workshop
    channel = client.get_channel(123456789)

    # Send a message to the channel
    await channel.send("Send a message")

# Your bot token
client.run(os.environ['workshop_bot_secret'])