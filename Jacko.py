import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='')
status = cycle(["Jack o' apetite L'", "GreatZardasht", "MinecraftSr", "My server 'MagicNoob Community'!", "Other bots: MagicNoob, ZardashtianBot"])


@client.event
async def on_ready():
    change_status.start()
    print("On: True, Off: False")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specfiy an argument.')


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


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


@client.command(aliases=['purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    try:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Message(s) Deleted!')
    except:
        await ctx.send("You don't have permission.")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member}. Reason: {reason}")
    except:
        await ctx.send(f"You don't have permission.")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member}. Reason: {reason}")
    except:
        await ctx.send(f"You don't have permission.")


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    try:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
    except:
        await ctx.send(f"Couldn't ban {user.mention}. Reason : You don't have permission. / This user isn't banned.")

@client.command()
async def information(ctx):
    await ctx.send('**This shows you the information of the bot not the owner.**\nOwner: Mr Noob Pink\nFriend: Buckled Flea\nIDE: Python-3.6.8\nVersion: Big Chungus\nSo get the hell away.')


client.run(str(os.environ.get('BOT_TOKEN')))
