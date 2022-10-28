# This will be processed in the next versions

commands = ['help', 'info', 'list', 'inject'] # example commands list will be changed to files

while True:
    command = input('> ')
    if command.startswith(tuple(commands)):
        print(command)