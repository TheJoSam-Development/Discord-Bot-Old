from discord.ext import commands
from discord.ext import tasks
from extensions.command_line.commands import inject

class command_line(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def command_line(self, ctx, calls=1):
        if calls >= 2: call_message = f'{calls} calls'
        else: call_message = '1 call'
        await ctx.send('You have now {} in your console'.format(call_message))
        
        for i in range(calls):
            cmd = input('[] > '.format(calls))
            if cmd.startswith('inject'):
                print('Starting Server Bot Injection sequence')
                inject.call()

def setup(bot):
    bot.add_cog(command_line(bot))
    while True:
        pass