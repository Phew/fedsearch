import requests, os
from colorama import *

def main():
    os.system('cls; clear')
    print('Welcome to HellSec Database API!\n')
    s = input(f'{Fore.YELLOW}> ')
    r = requests.post(
        url='https://fedsearch.xyz/API/test.php', 
        data={"search": s, "submit": "", "key": ""}, 
    )
    print(f'{Fore.WHITE}' + r.text)
    print('\n')
    lmao = input('Type clear to clear the screen! ')
    if lmao == 'clear':
        main()

main()
