command_lines = ['T0', 'T2'] # direct Command CommandFile system

def call(command_file):
    cf = open(command_file, 'w')
    cf.writelines(command_lines)