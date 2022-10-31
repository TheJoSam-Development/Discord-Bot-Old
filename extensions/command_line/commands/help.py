def call(command_list: list, *command: str):
    print('Command Help:')
    if command_list == []:
        print('No commands found')
        return
    for i in command_list:
        print(f'- {i}')