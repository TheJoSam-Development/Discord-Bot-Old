import secrets

global characters_file
global reserved_list
characters_file = 'config/tuuid_characters.txt'
reserved_list   = 'data/tuuid_list.dat'

def generate_type_1(count: int):
    chars = list(open(characters_file, 'r').read())
    used_read = open(reserved_list, 'rt')
    used = open(reserved_list, 'a+')
    used_list = used_read.readlines()
    
    block1 = []
    block2 = []
    block3 = []
    block4 = []
    block5 = []
    block6 = []
    block1_lenght = 10
    block2_lenght = 10
    block3_lenght = 5
    block4_lenght = 5
    block5_lenght = 5
    block6_lenght = 10
    
    
    for i in range(count):
        base = ''
        for i in range(block1_lenght):
            for i in range(3):
                block1.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block1))
        base += '-'

        for i in range(block2_lenght):
            for i in range(3):
                block2.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block2))
        base += '-'

        for i in range(block3_lenght):
            for i in range(3):
                block3.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block3))
        base += '-'

        for i in range(block4_lenght):
            for i in range(3):
                block4.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block4))
        base += '-'

        for i in range(block5_lenght):
            for i in range(3):
                block5.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block5))
        base += '-'

        for i in range(block6_lenght):
            for i in range(3):
                block6.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block6))
        
        if (base + '\n') not in used_list:
            used.write(base + '\n')
            used.close()
            used_read.close()
            return base
        else:
            i = 0


def generate_type_4(count: int):
    global output
    output = []
    chars = list(open(characters_file, 'r').read())
    used_read = open(reserved_list, 'rt')
    used = open(reserved_list, 'a+')
    used_list = used_read.readlines()
    
    block1 = []
    block2 = []
    block3 = []
    block4 = []
    block5 = []
    block6 = []
    block1_lenght = 15
    block2_lenght = 10
    block3_lenght = 10
    block4_lenght = 10
    block5_lenght = 10
    block6_lenght = 10
    
    
    for i in range(count):
        base = ''
        for i in range(block1_lenght):
            for i in range(3):
                block1.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block1))
        base += '-'

        for i in range(block2_lenght):
            for i in range(3):
                block2.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block2))
        base += '-'

        for i in range(block3_lenght):
            for i in range(3):
                block3.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block3))
        base += '-'

        for i in range(block4_lenght):
            for i in range(3):
                block4.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block4))
        base += '-'

        for i in range(block5_lenght):
            for i in range(3):
                block5.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block5))
        base += '-'

        for i in range(block6_lenght):
            for i in range(3):
                block6.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block6))
        
        if (base + '\n') not in used_list:
            used.write(base + '\n')
            used.close()
            used_read.close()
            return base
        else:
            i = 0


def generate_type_6(count: int):
    chars = list(open(characters_file, 'r').read())
    used_read = open(reserved_list, 'rt')
    used = open(reserved_list, 'a+')
    used_list = used_read.readlines()
    
    block1 = []
    block2 = []
    block3 = []
    block4 = []
    block5 = []
    block6 = []
    block1_lenght = 15
    block2_lenght = 15
    block3_lenght = 15
    block4_lenght = 10
    block5_lenght = 10
    block6_lenght = 20
    
    
    for i in range(count):
        base = ''
        for i in range(block1_lenght):
            for i in range(3):
                block1.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block1))
        base += '-'

        for i in range(block2_lenght):
            for i in range(3):
                block2.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block2))
        base += '-'

        for i in range(block3_lenght):
            for i in range(3):
                block3.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block3))
        base += '-'

        for i in range(block4_lenght):
            for i in range(3):
                block4.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block4))
        base += '-'

        for i in range(block5_lenght):
            for i in range(3):
                block5.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block5))
        base += '-'

        for i in range(block6_lenght):
            for i in range(3):
                block6.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block6))
        
        if (base + '\n') not in used_list:
            used.write(base + '\n')
            used.close()
            used_read.close()
            return base
        else:
            i = 0


def generate_type_5(count: int):
    chars = list(open(characters_file, 'r').read())
    used_read = open(reserved_list, 'rt')
    used = open(reserved_list, 'a+')
    used_list = used_read.readlines()
    
    block1 = []
    block2 = []
    block3 = []
    block4 = []
    block5 = []
    block6 = []
    block7 = []
    block1_lenght = 20
    block2_lenght = 15
    block3_lenght = 15
    block4_lenght = 15
    block5_lenght = 10
    block6_lenght = 20
    block7_lenght = 20
    
    
    for i in range(count):
        base = ''
        for i in range(block1_lenght):
            for i in range(3):
                block1.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block1))
        base += '-'

        for i in range(block2_lenght):
            for i in range(3):
                block2.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block2))
        base += '-'

        for i in range(block3_lenght):
            for i in range(3):
                block3.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block3))
        base += '-'

        for i in range(block4_lenght):
            for i in range(3):
                block4.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block4))
        base += '-'

        for i in range(block5_lenght):
            for i in range(3):
                block5.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block5))
        base += '-'

        for i in range(block6_lenght):
            for i in range(3):
                block6.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block6))
        
        for i in range(block7_lenght):
            for i in range(3):
                block7.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block7))
        
        if (base + '\n') not in used_list:
            used.write(base + '\n')
            used.close()
            used_read.close()
            return base
        else:
            i = 0


def generate_custom(count: int,
                    block1_lenght: int = 0,
                    block2_lenght: int = 0,
                    block3_lenght: int = 0,
                    block4_lenght: int = 0,
                    block5_lenght: int = 0,
                    block6_lenght: int = 0,
                    block7_lenght: int = 0):
    chars = list(open(characters_file, 'r').read())
    used_read = open(reserved_list, 'rt')
    used = open(reserved_list, 'a+')
    used_list = used_read.readlines()
    
    block1 = []
    block2 = []
    block3 = []
    block4 = []
    block5 = []
    block6 = []
    block7 = []
    
    
    for i in range(count):
        base = ''
        for i in range(block1_lenght):
            for i in range(3):
                block1.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block1))
        if block1_lenght != 0: base += '-'

        for i in range(block2_lenght):
            for i in range(3):
                block2.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block2))
        base += '-'

        for i in range(block3_lenght):
            for i in range(3):
                block3.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block3))
        base += '-'

        for i in range(block4_lenght):
            for i in range(3):
                block4.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block4))
        base += '-'

        for i in range(block5_lenght):
            for i in range(3):
                block5.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block5))
        base += '-'

        for i in range(block6_lenght):
            for i in range(3):
                block6.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block6))
        
        for i in range(block7_lenght):
            for i in range(3):
                block7.append(''.join(secrets.choice(chars)))
            base += ''.join(secrets.choice(block7))
        
        if (base + '\n') not in used_list:
            used.write(base + '\n')
            used.close()
            used_read.close()
            return base
        else:
            i = 0