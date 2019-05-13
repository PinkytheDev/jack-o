import discord
import json
import os
from discord.ext import commands

client = commands.bot(command_prefix="")

@client.event
async def on_ready():
	print(client.user.name + " is Online on everyserver of Discord.")
	
client.run('NTQ4NDE2NDg0NTAyNjY3MjY4.XNltEg.ugwnfNiQqPzHz4SqzNW-CO6xBdA')
