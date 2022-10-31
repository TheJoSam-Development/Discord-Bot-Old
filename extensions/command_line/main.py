from discord.ext import commands
from discord.ext import tasks

class command_line(commands.Cog):
    def __init__(self, bot):
        self.bot = bot