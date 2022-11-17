from alive_progress import alive_bar
import sys
sys.path.append('modules/')
from modules import user_register
from modules import tuuid_creator

def call(bot):
    guild_members = 0
    for guild in bot.guilds:
        print('Here are all members from guild: {}'.format(guild.id))
        guild_members = 0
        for member in guild.members:
            print(' - ' + member.name)
            guild_members += 1
        
        with alive_bar(spinner='classic', total=int(guild_members), title='Inject members', enrich_print=False) as bar:
            for member in guild.members:
                bar.text('Injecting user: {}'.format(member.id))
                if user_register.check_if_exists(str(member.id)):
                    bar()
                    continue
                user_register.register_user(user_id=str(member.id), join_date='N/A', server_join_date='N/A')
                bar()