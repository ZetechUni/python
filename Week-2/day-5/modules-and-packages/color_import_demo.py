import colorama

colorama.init()
print(colorama.Fore.RED + 'This is red')

from colorama import *

init()
print(Fore.YELLOW + 'This is yellow')

from colorama import init, Fore
print(Fore.GREEN + 'This is green')
