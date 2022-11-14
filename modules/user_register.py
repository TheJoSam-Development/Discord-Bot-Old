import tuuid_creator
import logging
import logging.config
import audit_logger
import os
import csv
import json

__version__ = '1.3'
__author__  = 'TheJoSam'

LOGGER = logging.config.dictConfig(json.load(open('config/logger.json', 'r')))
logger = logging.getLogger(__name__)

register_file = 'data/user_register.csv'

if not os.path.exists(register_file):
    with open(register_file, 'w') as user_register:
        fieldnames = 'tuuid,discord_user_id,discord_join_date,server_join_date'
        user_register.write(fieldnames + '\n')

def register_user(user_id: str, join_date: str, server_join_date: str):
    global exists
    global user
    exists = False
    
    try: 
        with open(register_file, 'r') as user_register:
            user_register_reader = user_register.readlines()
            line_count = 0
            for item in user_register_reader:
                data = item.split(',')
                logger.log(level=5, msg=f'[register_user][User {line_count}]: data: {data}')
                if line_count == 0:
                    line_count += 1
                    continue
                elif user_id in data[1]:
                    logger.error('[register_user]: called an error with errorcode 52')
                    exists = True
                    break
                
    except Exception: logger.error(f'[register_user]: raised an exception errorcode 57: {Exception}')
    
    try: user = {'tuuid': f'{tuuid_creator.generate_type_6(1)}', 'discord_user_id': f'{user_id}', 'discord_join_date': f'{join_date}', 'server_join_date': f'{server_join_date}'}
    except: logger.error(f'[register_user]: raised an exception with errorcode 56: {Exception}')
    
    with open(register_file, 'a+', newline='') as user_register:
        fieldnames = ['tuuid', 'discord_user_id', 'discord_join_date', 'server_join_date']
        user_register_writer = csv.DictWriter(user_register, fieldnames=fieldnames)
        if not exists:
            user_register_writer.writerow(user)
        else:
            logger.error('[register_user]: called an error with errorcode 52')


def get_user(user_id: str):
    try: 
        with open(register_file, 'r') as user_register:
            user_register_reader = user_register.readlines()
            line_count = 0
            for item in user_register_reader:
                data = item.split(',')
                print(data)
                if line_count == 0:
                    line_count += 1
                    continue
                elif user_id not in data[1]:
                    logger.error('[get_user]: called an error with errorcode 54')
                    break
                else:
                    return data
                
    except Exception: logger.error(f'[get_user]: raised an exception errorcode 57: {Exception}')


class user_file:
    def __init__(self, tuuid: str):
        self.tuuid = tuuid
        logger.debug('[user_file][init]: Initialized user_file object')
    
    def write_data(self, new_data, category):
        with open('{}.json'.format(self.tuuid), 'r+') as file:
            file_data = json.load(file)
            file_data[f'{category}'].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    
    def read_data(self):
        with open('{}.json'.format(self.tuuid), 'r+') as file:
            return json.load(file)
    
    def empty_file(self):
        with open('{}.json'.format(self.tuuid), 'w+') as file:
            file.write('')