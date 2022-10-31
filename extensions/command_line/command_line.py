# This will be worked on in next iteration
import os
from commands import help, inject

global command_file
global command_list
command_list = []
command_file = 'beta-features/command_line/command_file.txt'

for i in os.listdir('beta-features/command_line/commands'): # using commands directory for command_list
    command = i[:-3]
    if command == 'help':
        continue
    elif command == '__pycach':
        continue
    else: command_list.append(command)

while True:
    command = input('> ')
    if command.startswith('help'):
        help.call(command_list)
    elif command.startswith('inject'):
        inject.call(command_file)