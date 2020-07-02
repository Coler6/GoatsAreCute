import discord
from discord.ext import commands
import random
import os
client = commands.Bot(command_prefix = 'g!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server, here we **goat** again.')
    await on_member_join.send(f'{member} has joined the server, here we **goat** again.')
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server, you have **goat** to be **kid**ding me. That is too **bad**')
    await on_member_remove.send(f'{member} has left the server, you have **goat** to be **kid**ding me. That is too **bad**')
@client.command()
async def illumix(ctx):
    await ctx.send('https://pbs.twimg.com/profile_images/1146134369674809349/WjI4mMZc_400x400.png')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

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
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

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

@commands.command(name='unban')
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def unban(self, ctx, userId):
    user = discord.Object(id=userId)
    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned {user}")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension})

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension})

for filename in os.listdir('./cogs'):
    if


client.run('NzI3MjYwOTE4NTA0ODgyMjU2.XvpTzQ.mFmynFz6q6_7bMEcUDaY_xOoLb0')
