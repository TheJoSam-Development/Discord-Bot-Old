from discord.ext import commands

def convert_for_framework(command_file: str):
    cf = open(command_file, 'r')
    global row_number
    global command_number
    global T0
    row_number = 0
    command_number = 0
    T0 = 0
    for row in cf.readlines():
        if not row.startswith('T'): # skips comments 
            continue
        
        if command_number == 0 and T0 == 0 and row.startswith('T0'):
            print('Init row found')
            command_number += 1
            T0 = 1
        elif row.startswith('T0') and T0 == 0:
            print('T0 can only be 1 time inside command_file')
        
        if row.startswith('T1'):
            print(str(row[3:]).rstrip())
            command_number += 1
        
        if row.startswith('T2'):
            args = row[3:].split(' ', maxsplit=1)
            print(f'Sending message "{str(args[1]).rstrip()}" into channel "{args[0]}"')
            command_number += 1

if __name__ == '__main__':
    convert_for_framework('extensions/command_line/test_command_file.txt')