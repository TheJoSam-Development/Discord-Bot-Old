def get_extension_meta(extension_path: str):
    meta_file = open(str(extension_path + 'extension.meta'), 'r')
    meta_content = list(meta_file.readlines())
    
    global extension_name
    global extension_version
    global extension_author
    global extension_description
    global extension_key
    global extension_main
    
    global extension
    
    extension_name = ''
    extension_version = ''
    extension_author = ''
    extension_description = ''
    extension_key = ''
    extension_main = ''
    
    for line in meta_content:
        if line.startswith('Name: '):    extension_name = line[6:-1]
        if line.startswith('Version: '): extension_version = line[9:-1]
        if line.startswith('Author: '):  extension_author = line[8:-1]
        if line.startswith('Description: '): extension_description = line[13:-1]
        if line.startswith('KEY_file: '):  extension_key = line[10:-1]
        if line.startswith('MAIN_file: '):  extension_main = line[11:-3]

        if extension_name is None: extension_name = 'None'
        if extension_version is None: extension_version = 'None'
        if extension_author is None: extension_author = 'None'
        if extension_description is None: extension_description= 'None'
        if extension_key is None: extension_key = 'None'
        if extension_main is None: extension_main = 'None'
            
    extension = []
    extension.append(extension_name)
    extension.append(extension_version)
    extension.append(extension_author)
    extension.append(extension_description)
    extension.append(extension_key)
    extension_main_file = str(extension_path.replace('/', '.') + extension_main)
    extension.append(extension_main_file)
    
    return extension
