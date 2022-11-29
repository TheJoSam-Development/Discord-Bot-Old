import discord
from discord.ext import commands

@commands.command()
async def ping(ctx):
    await ctx.send('**PONG!**')

def setup(bot):
    bot.add_command(ping)