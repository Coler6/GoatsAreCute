import discord
from discord.ext import commands, tasks
from itertools import cycle
from discord.utils import get
import random
import asyncio
import os
import youtube_dl
client = commands.Bot(command_prefix = 'g!')

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="goats         g!help for help."))

#WELCOME/LEAVE COMMANDS
class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

botdata = BotData()

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

#FUN COMMANDS
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def goats(ctx):
    responses = ["https://i.imgur.com/GaPoxOD.jpg",
                "https://i.imgur.com/Sb7aaeA.jpg",
                "https://i.imgur.com/XRZFBUQ.jpg",
                "https://imgur.com/97051cc6-9d38-411a-bcda-4a600fe71a82",
                "https://i.imgur.com/GYtW2rj.jpg",
                "https://i.imgur.com/wBVcBy2.jpg",
                "https://imgur.com/8c8bb401-d38d-47d4-a223-8359640a142b",
                "https://i.imgur.com/bh1rjHU.jpg",
                "https://i.imgur.com/nWtjVb7.jpg",
                "https://i.imgur.com/sMHl52t.jpg",
                "https://i.imgur.com/43EKJqB.jpg",
                "https://i.imgur.com/VmzPmOd.jpg",
                "https://i.imgur.com/GYtW2rj.jpg",
                "https://i.imgur.com/OUszsOD.jpg",
                "https://i.imgur.com/SMvWukk.jpg",
                "https://i.imgur.com/EjDdZUF.jpg",
                "https://i.imgur.com/1jE0hQZ.jpg",
                "https://i.imgur.com/G4tAGGq.jpg",
                "https://i.imgur.com/bEkgXeX.jpg",
                "https://imgur.com/a0c61e9a-7ca5-49b9-93c6-b0f2bb614500",
                "https://imgur.com/25f0e80a-4d48-4c6e-aa63-9e0660a4d156",
                "https://i.imgur.com/hGatqXD.jpg",
                "https://i.imgur.com/iLcF3dI.jpg",
                "https://i.imgur.com/lbD1ULo.jpg",
                "https://i.imgur.com/HLphakw.jpg",
                "https://i.imgur.com/EVMNhq3.jpg",
                "https://i.imgur.com/i8obDzJ.jpg",
                "https://i.imgur.com/fS8UVaG.jpg",
                "https://i.imgur.com/vQdh5eL.jpg",
                "https://i.imgur.com/EkqJG5m.jpg",
                "https://i.imgur.com/RnHej9b.jpg",
                "https://i.imgur.com/4tr2OPW.jpg",
                "https://i.imgur.com/to9mALS.jpg",
                "https://i.imgur.com/BZkNTDG.jpg",
                "https://i.imgur.com/zHCmO6q.jpg",
                "https://i.imgur.com/cd6vYSC.jpg",
                "https://i.imgur.com/g96nPYf.jpg",
                "https://i.imgur.com/vWq4Q2x.jpg",
                "https://i.imgur.com/2fHDgJf.jpg",
                "https://i.imgur.com/u2ghRCK.jpg",
                "https://i.imgur.com/zK8ur8t.jpg",
                "https://i.imgur.com/ec350EO.jpg",
                "https://i.imgur.com/FL2nUQz.jpg",
                "https://i.imgur.com/KaHM9ZS.jpg",
                "https://i.imgur.com/2p9r7YG.jpg",
                "https://i.imgur.com/4LuhRoW.jpg",
                "https://i.imgur.com/RQmPVLE.jpg",
                "https://i.imgur.com/9drPkys.jpg",
                "https://i.imgur.com/qW9J550.jpg",
                "https://i.imgur.com/2ThV2Of.jpg",
                "https://i.imgur.com/9ucdAuz.jpg",
                "https://i.imgur.com/tJXlOPV.jpg",
                "https://i.imgur.com/htW5PLI.jpg",
                "https://i.imgur.com/qzQtY4O.jpg",
                "https://i.imgur.com/K2DkcDw.jpg",
                "https://i.imgur.com/jVqdXRj.jpg",
                "https://i.imgur.com/Ziukby7.jpg",
                "https://i.imgur.com/jGFoA5e.jpg",
                "https://i.imgur.com/uZpogzn.jpg",
                "https://i.imgur.com/9iAnJ6L.jpg",
                "https://i.imgur.com/y3XU87y.jpg",
                "https://i.imgur.com/tDUheKs.jpg"]
    await ctx.send(f'Goated! {random.choice(responses)}')

@client.command()
async def birds(ctx):
    responses = ["https://i.imgur.com/DnAF7UU.jpg",
                "https://i.imgur.com/ptF83A7.jpg",
                "https://i.imgur.com/ctjl8H0.jpg",
                "https://i.imgur.com/x4EzdrN.jpg",
                "https://i.imgur.com/BghdL6c.jpg",
                "https://i.imgur.com/DvKDXAZ.jpg",
                "https://i.imgur.com/qSkYWMU.jpg",
                "https://i.imgur.com/pEd8a9s.jpg",
                "https://i.imgur.com/gLFMlrM.jpg",
                "https://i.imgur.com/acA1QhG.jpg"]
    await ctx.send(f'Birds! {random.choice(responses)}')

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

#MODERATION
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'You were kicked! Next time do not be so **BAAAAA**d')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'You were banned! Next time do not be so **BAAAAA**d')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention} better not be a pain in the **horn**')
            return

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("Muted {}, next time stop being a pain in the **horn**" .format(member.mention,ctx.author.mention))
            return

            overwrite = discord.PermissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("Muted {}, next time stop being a pain in the **horn**" .format(member.mention,ctx.author.mention))

@client.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("Unmuted {}, better not **butt** in to the conversion" .format(member.mention,ctx.author.mention))
            return

#Music
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f'Successfully joined voice channel!')

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send(f'Successfully lefted voice channel!')

players = {}

@client.command(pass_context=True)
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing (do the stop command to stop the music)")
        return

    await ctx.send("Getting everything ready now!")

    voice = get(ctx.bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }



    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        await ctx.send('Downloading audio now!')
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing"))
    voice.sourse = discord.PCMVolumeTransformer(voice.source)
    voice.sourse.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname}")
    print("playing")

@client.command(pass_context=True)
async def pause(ctx):

    voice = get(ctx.bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Music has been paused")
    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing failed pause")

@client.command(pass_context=True)
async def resume(ctx):

    voice = get(ctx.bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("Music is not paused")
        await ctx.send("Music is not paused")

@client.command(pass_context=True)
async def stop(ctx):

    voice = get(ctx.bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("Music has been stopped")
    else:
        print("Music not playing failed to stop")
        await ctx.send("Music not playing failed to stop")

client.run('NzI3MjYwOTE4NTA0ODgyMjU2.XvpTzQ.mFmynFz6q6_7bMEcUDaY_xOoLb0')
