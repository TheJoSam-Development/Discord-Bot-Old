import discord
from discord.ext import commands

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason):
    if reason == None:
        reason = ''
    await user.kick(reason=reason)
    await ctx.send('User "{}" was kicked for "{}"'.format(user.name, reason))

def setup(bot):
    bot.add_command(kick)