
import os
from collections import defaultdict

TARGET_DIR = 'joplin-monitor/' # target directory to copy files into
DEBUG = True

VALID_MENU_CHOICES = {
     1:'Split files into chunks',
     2:'Read from list',
     3:'Read from dict',
}

files_complex = defaultdict(list)
files_simple = []

# must be relative to current directory

def change_directory(target_dir=TARGET_DIR):
    """Changes directory to the provided path
    Returns full path of new directory"""
    os.chdir(target_dir)
    cwd = os.getcwd()
    if DEBUG:
        print(f'Successfully changed directory: {cwd}')
    return cwd

def create_file(fname, content=None):
    """Creates an actual file in the filesystem"""
    if not content:
        # no content has to be written to file
        # so only create file
        with open(fname,'w') as f:
            pass
    else:
        # create file and write content to it
        with open(fname,'w') as f:
                f.write('\n'.join(content))
    if DEBUG:
            print(f'Successfully created file: {fname}')
    return

def create_files(files:dict | list):
    """Creates files from a list of filenames or
    a dict of filenames with content as value

    Example valid list of filenames:
    ['hello.txt','yo.txt']

    Example valid dict of files with content:
    {
        'somefile.txt':['first line','second line','etc...',],
        'poem.txt':['poem first line','you are so brave bla bla poem'],
        'emptyfile.txt':[],
    }
    """
    if isinstance(files, list):
        for f in files:
             print(f'About to create file: {f}')
             if DEBUG:
                  input('Continue?')
             create_file(f)
        return
    elif isinstance(files, dict):
        print(f'Preparing to create files from dict')
        for fname, content in files.items():
             print(f'About to create file: {fname} with content: {content}')
             input('Continue?')
             create_file(fname, content)
        return
    else:
        raise SystemExit("Only creating files from list has been implementet, sorry!")



def is_valid_choice(choice:int):
    """Attempts to clean nasty stuff from the users
    mennu choice"""
    
    cleaned_choice = 0
    try:
        cleaned_choice = int(choice)
    except Exception as e:
         print(e)
         return 0
    if DEBUG:
        print(f'Checking if cleaned_choice in VALID_CHOICES:')
    if cleaned_choice in VALID_MENU_CHOICES.keys():
        return cleaned_choice
    return 0

def print_menu():
    print(f'Welcome to blabla')
    choices = VALID_MENU_CHOICES.items()
    
    for choice, description in choices:
        print(f'{choice}: {description}')
    
    userchoice = ''
    while not is_valid_choice(userchoice:= input(f'What would you like to do?')):
         print(f'Please select a number corresponding to a menu item')
    
    print(f'Choice is valid!')
    raise NotImplementedError('Sorry not finished!')
    



def main():
    print_menu()

if __name__ == '__main__':
     main()