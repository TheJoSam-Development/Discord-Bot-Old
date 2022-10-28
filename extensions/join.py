from discord.ext import commands
import sys

sys.path.append('..')
from modules import user_register

class login(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        user_register.register_user(user_id = member.id, join_date = 'NA', server_join_date = 'NA')


def setup(bot):
    bot.add_cog(login)