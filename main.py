import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time

import json
from modules import logger as log_module
from alive_progress import alive_bar
import asyncio
import threading

config_file_path = './config/main.json'
config_file = open(config_file_path, 'r')
config = json.load(config_file)

extension_file = open(config['extensions_file'])
extensions = json.load(extension_file)
extension_file.close()

logger = log_module.logging(module='MAIN')
logger.info(message='Logging module loaded')

global loaded_commands
global loaded_extensions
loaded_commands   = []
loaded_extensions = []

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = str(config['prefix']), intents = intents)
#bot.remove_command('help') #Uncomment when using an external Help command (official is WIP)

logger.info(message='Started command handler', extra='[Command Handler]')
logger.warning(message='Not verified commands can damage your data security!', extra='[Command Handler]')
if extensions['commands'] != []:
    with alive_bar(spinner='classic', total=int(len(extensions['commands']))) as bar:
        for command in extensions['commands']:
            logger.debug(message='Starting loading command: {}'.format(command), extra='[Command Handler]')
            try:
                bot.load_extension(command)
                loaded_commands.append(command)
                time.sleep(0.05)
            except Exception as e:
                logger.error(message='load extension raised an error with errorcode 20: {}'.format(e), extra='[Command Handler]')
            logger.debug(message='Finished loading command: {}'.format(command), extra='[Command Handler]')
            bar()
else:
    logger.warning(message='registered command not found: errorcode 21', extra='[Command Handler]')

if extensions['extensions'] != []:
    with alive_bar(spinner='classic', total=int(len(extensions['extensions']))) as bar:
        for command in extensions['extensions']:
            logger.debug(message='Starting loading command: {}'.format(command), extra='[Extension Handler]')
            try:
                bot.load_extension(command)
                loaded_extensions.append(command)
                time.sleep(0.05)
            except Exception as e:
                logger.error(message='load extension raised an error with errorcode 20: {}'.format(e), extra='[Extension Handler]')
            logger.debug(message='Finished loading extension: {}'.format(command), extra='[Extension Handler]')
            bar()
else:
    logger.warning(message='registered extension not found: errorcode 21', extra='[Extension Handler]')


@bot.command()
async def list_commands(ctx):
    if loaded_commands != []:
        await ctx.send('Loaded Commands: {}'.format(loaded_commands))
    else:
        await ctx.send('No Loaded Commands')

@bot.command()
async def list_extensions(ctx):
    if loaded_extensions != []:
        await ctx.send('Loaded Extensions: {}'.format(loaded_extensions))
    else:
        await ctx.send('No Loaded Extensions')

@bot.command()
@has_permissions(administrator=True)
async def logout(ctx):
    await ctx.send('logging out')
    await bot.logout()
    logger.error('logged out of system: errorcode 500')

@bot.event
async def on_ready():
    logger.info('Bot connected successfully')
    logger.info('Bot ready')

bot.run(str(config['api_key']))