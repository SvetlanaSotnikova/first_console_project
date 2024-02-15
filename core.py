import datetime
from genericpath import isdir
import os
import shutil

# creat files
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
    save_info(f'creat_file {name} with text: {text}')

# creat folders
def create_folder(name):
    try:
        os.mkdir(name)
        save_info(f'create_folder {name}')
    except FileExistsError:
        save_info(f'attempt to create_folder {name}')
        print('you already have this folder')

# getting list files and folders
def GetList(folders_only=False):
    res = os.listdir()
    if folders_only:
        res= [f for f in res if os.path.isdir(f)]
    print(res)
    save_info(f'get list folders')

# deletting files and folders
def delete_file(name):
    if os.path.exists(name):
        if os.path.isdir(name):
            try:
                os.rmdir(name)
                save_info(f'deleted folder {name}')
            except OSError:
                save_info(f'deleted folder is not empty {name}')
                print('folder is not empty :/')
                print('if you want delete all directory you can use command: delete_dir :D')
        else:
            try:
                os.remove(name)
                save_info(f'deleted file {name}')
            except OSError:
                save_info(f'attempt to delete {name} wasn"t not found')
                print(f'{name} is not found :/')
    else:
        print(f'{name} is not found :/')
        save_info(f'attempt to delete {name} wasn"t not found')

# deletting directory tree
def delete_dir(name):
    if os.path.isdir(name):
        try:
            shutil.rmtree(name)
            save_info(f'delete directory {name}')
        except OSError:
            print(f'directory {name} is not empty :/')
            save_info(f'attempt to delete directory {name}')
    else:
        try:
            os.remove(name)
            save_info(f'delete file {name}')
        except OSError:
            print(f'{name} is not found')
            save_info(f'attempt to delete file {name}')

# copying files or folders
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name) 
            save_info(f'copy {name} in {new_name}')
        except FileExistsError:
            print('you already have this file')
            save_info(f'copy {name} to an existing folder {new_name}')
        except FileNotFoundError:
            print('file is not found')  
            save_info(f"attempt to copy {name} in not found {new_name} ")
    else:
        try:
            shutil.copy(name, new_name) 
            save_info(f'copy {name} in is not found {new_name}') 
        except FileNotFoundError:
            print('file is not found')   

# change of place in the project
def change_dir(name):
    try:
        os.chdir(name)
        save_info(f'change_dir {name}')
    except FileNotFoundError:
        print(f'file {name} is not found')

# saving information 
def save_info(message):
    current_time = datetime.datetime.now()
    res = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(res + '\n')

if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_f')
    GetList()
    GetList(True)
    delete_file('text.dat')
    delete_file('new_f1')
    copy_file('new_f1', 'new_f2')
    create_file('text.dat')
    copy_file('text.dat', 'text2.dat')
    save_info('hi, my dear user')