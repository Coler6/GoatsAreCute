import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import asyncio
import os
client = commands.Bot(command_prefix = 'g!')

class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

botdata = BotData()

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="goat         g!help for help."))

@client.event
async def on_member_join(member):
    if botdata.welcome_channel != None:
        await botdata.welcome_channel.send(f"{member.mention} has just joined the server, here we **goat** again! :smile: ")

    else:
        print("Welcome channel was not set.")

@client.event
async def on_member_remove(member):
    if botdata.goodbye_channel != None:
        await botdata.goodbye_channel.send(f"{member.mention} has left the server, you have **goat** to be **kid**ding me. That is too **bad**. :frowning: ")

    else:
        print("Goodbye channel was not set.")

@client.command()
async def set_welcome_channel(ctx, channel_name=None):
    if channel_name != None:
        for channel in ctx.guild.channels:
            if channel.name == channel_name:
                botdata.welcome_channel = channel
                await ctx.channel.send(f"Welcome channel has been set to: {channel.name}")
                await channel.send("This is the new welcome channel!")

    else:
        await ctx.channel.send("You must need a welcome channel for this command to work.")

@client.command()
async def set_goodbye_channel(ctx, channel_name=None):
    if channel_name != None:
        for channel in ctx.guild.channels:
            if channel.name == channel_name:
                botdata.goodbye_channel = channel
                await ctx.channel.send(f"Goodbye channel has been set to: {channel.name}")
                await channel.send("This is the new goodbye channel!")

    else:
        await ctx.channel.send("You must need a goodbye channel for this command to work.")


@client.command()
async def goat(ctx):
    await ctx.send('https://i.imgur.com/GaPoxOD.jpg')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def goats(ctx):
    responses = ["https://i.imgur.com/GaPoxOD.jpg",
                "https://i.imgur.com/Sb7aaeA.jpg"]
    await ctx.send(f'Goated! {random.choice(responses)}')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{user.mention} was kicked! Next time do not be so **BAAAAA**d')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{user.mention} was banned! Next time do not be so **BAAAAA**d')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_user:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention} better not be a pain in the **horn**')
            return

client.run('NzI3MjYwOTE4NTA0ODgyMjU2.XvpTzQ.mFmynFz6q6_7bMEcUDaY_xOoLb0')
