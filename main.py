import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time

import json
import logging
import logging.config
from alive_progress import alive_bar
import sys

config_file_path = './config/main.json'
config_file = open(config_file_path, 'r')
log_config_file = open('config/logger.json', 'r')
log_config = json.load(log_config_file)
config = json.load(config_file)

extension_file = open(config['extensions_file'])
extensions = json.load(extension_file)
extension_file.close()

logger_cfg = logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)
logger.info(': Logging module loaded')

global loaded_commands
global loaded_extensions
loaded_commands   = []
loaded_extensions = []

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = str(config['prefix']), intents = intents)
#bot.remove_command('help') #Uncomment when using an external Help command (official is WIP)

logger.info('[Command Handler]: Started command handler')
logger.warning('[Command Handler]: Not verified commands can damage your data security!')
if extensions['commands'] != []:
    with alive_bar(spinner='classic', total=int(len(extensions['commands'])), title='Commands', enrich_print=False) as bar:
        for command in extensions['commands']:
            logger.debug('[Command Handler]: Starting loading command: {}'.format(command))
            bar.text('Loading {}'.format(command))
            try:
                bot.load_extension(command)
                loaded_commands.append(command)
                time.sleep(0.05)
            except Exception as e:
                logger.error('[Command Handler]: load extension raised an error with errorcode 20: {}'.format(e))
            logger.debug('[Command Handler]: Finished loading command: {}'.format(command))
            bar()
else:
    logger.warning('[Command Handler]: registered command not found: errorcode 21')

if extensions['extensions'] != []:
    with alive_bar(spinner='classic', total=int(len(extensions['extensions'])), title='Extensions', enrich_print=False) as bar:
        for extension in extensions['extensions']:
            logger.debug('[Extension Handler]: Starting loading extension: {}'.format(extension))
            bar.text('Loading {}'.format(extension))
            try:
                bot.load_extension(extension)
                loaded_extensions.append(extension)
                time.sleep(0.05)
            except Exception as e:
                logger.error('[Extension Handler]: load extension raised an error with errorcode 20: {}'.format(e))
            logger.debug('[Extension Handler]: Finished loading extension: {}'.format(extension))
            bar()
else:
    logger.warning('[Extension Handler]: registered extension not found: errorcode 21')


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