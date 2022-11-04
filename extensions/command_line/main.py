from discord.ext import commands
from discord.ext import tasks
import asyncio
import threading
import os
import sys
from extensions.command_line.commands import help, inject

global task_1
global command_file
global command_list
command_list = []
command_file = 'extensions/command_line/command_file.txt'

for i in os.listdir('extensions/command_line/commands'): # using commands directory for command_list
    command = i[:-3]
    if command == 'help':
        continue
    elif command == '__pycach':
        continue
    else: command_list.append(command)


async def bot_command_line():
        while True:
            command = input('> ')
            if command.startswith('help'):
                help.call(command_list)
            elif command.startswith('inject'):
                inject.call(command_file)


class command_line(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(command_line(bot))
    loop = asyncio.get_event_loop()
    task = loop.create_task(bot_command_line())
    loop.run_until_complete(task)

