import os


def clear_console():
    """Cross-platform console clear (Windows/macOS/Linux)"""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def val_error():
    '''Prints ValueError message'''
    print('Invalid input.')
    input('Press enter to continue...')
