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
        
        cmd_index = 0
        for i in range(calls):
            cmd_index += 1
            cmd = input('[{}] > '.format(cmd_index))
            if cmd.startswith('inject'):
                print('Starting Server Bot Injection sequence')
                inject.call(self.bot)
            else: break

def setup(bot):
    bot.add_cog(command_line(bot))