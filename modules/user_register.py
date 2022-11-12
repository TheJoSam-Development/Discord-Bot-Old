import tuuid_creator
import logger as logging
import audit_logger
import os
import csv

logger = logging.logging(module = 'USER REGISTER')
logger.debug(message = 'User Register Initialized')

register_file = 'data/user_register.csv'

if not os.path.exists(register_file):
    with open(register_file, 'w') as user_register:
        fieldnames = 'tuuid,discord_user_id,discord_join_date,server_join_date'
        user_register.write(fieldnames + '\n')

def register_user(user_id, join_date, server_join_date):
    global exists
    global user
    exists = False
    
    if type(user_id) is not str:
        logger.error(message = 'called an error with errorcode 3: Argument not required type (str)', extra = '[register_user]')
    if type(join_date) is not str:
        logger.error(message = 'called an error with errorcode 3: Argument not required type (str)', extra = '[register_user]')
    if type(server_join_date) is not str:
        logger.error(message = 'called an error with errorcode 3: Argument not required type (str)', extra = '[register_user]')
    
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
                elif user_id in data[1]:
                    logger.error(message = 'called an exception with errorcode 52', extra = '[register_user]')
                    exists = True
                    break
                
    except Exception as ex: logger.error(message = f'raised an exception errorcode 57: {ex}', extra = '[register_user]')
    
    try: user = {'tuuid': f'{tuuid_creator.generate_type_6(1)}', 'discord_user_id': f'{user_id}', 'discord_join_date': f'{join_date}', 'server_join_date': f'{server_join_date}'}
    except: logger.error(message = f'raised an exception with errorcode 56: {Exception}', extra = '[register_user]')
    
    with open(register_file, 'a+', newline='') as user_register:
        fieldnames = ['tuuid', 'discord_user_id', 'discord_join_date', 'server_join_date']
        user_register_writer = csv.DictWriter(user_register, fieldnames=fieldnames)
        if not exists:
            user_register_writer.writerow(user)
        else:
            logger.error(message = 'canceled user registration with errorcode 52', extra = '[register_user]')


def get_user(user_id):
    if type(user_id) is not str:
        logger.error(message = 'called an error with errorcode 3: Argument not required type (str)', extra = '[get_user]')
    
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
                    logger.error(message = 'called an exception with errorcode 54', extra = '[register_user]')
                    break
                else:
                    return data
                
    except Exception as ex: logger.error(message = f'raised an exception errorcode 57: {ex}', extra = '[register_user]')