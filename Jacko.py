import discord
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
	print(client.user.name + " is Online on everyserver of Discord.")
	

client.run(str(os.environ.get('BOT_TOKEN')))
