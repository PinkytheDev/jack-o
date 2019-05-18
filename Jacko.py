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
    await ctx.send(f"Pong!, {round(client.latency * 1000)}ms")

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

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    try:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Message(s) Deleted!')
    except:
        await ctx.send("You don't have permission.")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member}. Reason: {reason}")
    except:
        await ctx.send(f"You don't have permission.")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member}. Reason: {reason}")
    except:
        await ctx.send(f"You don't have permission.")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('a')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


client.run(str(os.environ.get('BOT_TOKEN')))
