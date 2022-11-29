import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time

import json
import logging
import logging.config
from alive_progress import alive_bar
import os

from modules import extension_loader

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

commands = list()
command_files = os.listdir(str(config['dirs']['commands_dir']))
for command_file in command_files:
    if command_file.endswith('.py'):
        if command_file.__contains__('/'):
            commands.append(command_file[:-3].replace('/', '.'))
        else:
            commands.append(command_file[:-3])
    else: continue

logger.info('[Command Handler]: Started command handler')
logger.warning('[Command Handler]: Not verified commands can damage your data security!')
if commands != []:
    with alive_bar(spinner='classic', total=int(len(commands)), title='Commands', enrich_print=False) as bar:
        for command in commands:
            logger.debug('[Command Handler]: Starting loading command: {}'.format(command))
            bar.text('Loading {}'.format(command))
            try:
                bot.load_extension(('commands.' + command))
                loaded_commands.append(command)
                time.sleep(0.05)
            except Exception as e:
                logger.error('[Command Handler]: load_extension raised an error with errorcode 20: {}'.format(e))
            logger.debug('[Command Handler]: Finish loading command: {}'.format(command))
            bar()
else:
    logger.warning('[Command Handler]: registered extension not found: errorcode 21')


if extensions['extensions'] != []:
    with alive_bar(spinner='classic', total=int(len(extensions['extensions'])), title='Extensions', enrich_print=False) as bar:
        for extension in extensions['extensions']:
            logger.debug('[Extension Handler]: Starting loading extension: {}'.format(extension))
            bar.text('Loading {}'.format(extension))
            try:
                if extension.startswith('extension.'):
                    bot.load_extension(extension)
                    loaded_extensions.append(extension)
                    time.sleep(0.05)
                    continue
                extension_data = extension_loader.get_extension_meta(extension)
                bot.load_extension(extension_data[5])
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
async def load_extension(ctx, extension: str):
    if extension.startswith('extension.') or extension.startswith('commands.'):
        bot.load_extension(extension)
        loaded_extensions.append(extension)
        time.sleep(0.05)
    extension_data = extension_loader.get_extension_meta(extension)
    bot.load_extension(extension_data[5])
    loaded_extensions.append(extension)

@bot.command()
async def reload_extension(ctx, extension: str):
    if extension.startswith('extension.') or extension.startswith('commands.'):
        bot.reload_extension(extension)
        time.sleep(0.05)
        return
    extension_data = extension_loader.get_extension_meta(extension)
    bot.reload_extension(extension_data[5])

@bot.command()
async def unload_extension(ctx, extension: str):
    if extension.startswith('extension.') or extension.startswith('commands.'):
        bot.unload_extension(extension)
        loaded_extensions.append(extension)
        time.sleep(0.05)
        return
    extension_data = extension_loader.get_extension_meta(extension)
    bot.unload_extension(extension_data[5])
    loaded_extensions.remove(extension)


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