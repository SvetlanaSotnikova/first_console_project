import sys
from core import create_file, create_folder, GetList, delete_dir, delete_file, copy_file, save_info, change_dir
from game import Game

try:
    command = sys.argv[1]
except IndexError:
    print('command must be entered. help')
else:
    if command == 'list':
        GetList()

    elif command == 'create_file':
        try: 
            text = sys.argv[3]
        except IndexError:
            print('text none')
            text=None
        try:
            name = sys.argv[2]
        except IndexError:
            print('? create_file <file_name> ?')
        else:
            create_file(name, text)

    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('? create_folder <folder_name> ?')
        else:
            create_folder(name)

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('? delete <file_name_or_folder_name> ?')
        else:
            delete_file(name)

    elif command == 'delete_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('? delete_dir <directory_name> ?')
        else:
            delete_dir(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('? create_file <file_name> <new_file_name> ?')
        copy_file(name, new_name)

    elif command == 'game':
        Game()
        save_info('game')

    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('? ch <folder_name> ?')
        else:
            change_dir(name)

    elif command == 'help':
        print('command: list -- shows a list of your files')
        print('command: create_file -- creates a file in your project')
        print('command: create_folder -- creates a folder in your project')
        print('command: delete -- deletes a folder or file in your project')
        print('command: delete_dir -- deletes a directory tree in your project')
        print('command: copy -- copies a folder or file in your project')
        print('command: game -- game "guess the number" with the computer')


