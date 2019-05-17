import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix= '')

@client.event
async def on_ready():
    print("On: True, Off: False")

@client.event
async def on_member_join(member, ctx):
    await ctx.say(f'Welcome {member} to our server! Have fun!')

@client.event
async def on_member_remove(member, ctx):
    await ctx.say(f'{member} had just left our server. Bye Bye {member}.')

@client.command()
async def ping(ctx):
    await ctx.say(f"Pong!, {round(client.latency * 1000)}ms")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt",
                 "Yes, definitely.",
                 "You may reply on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 'Cannot predict now.',
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

client.run(str(os.environ.get('BOT_TOKEN')))
