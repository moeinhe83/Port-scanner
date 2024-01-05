# port scanner

# Library
from os import system as sys
from pyfiglet import figlet_format
from termcolor import colored

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format('Port Scanner'), color='cyan'))
print(colored('=======================================================', color='blue'))

# Install Nmap On Linux
nmap = input('Do You Want Install Nmap [y/n] ===> ')

# IF For install Nmap
if nmap == 'y' or nmap == 'Y':
    sys('sudo apt install nmap')

elif nmap == 'n' or nmap == 'N':
    pass

print(colored('=======================================================', color='yellow'))

# Input
user_op = input(colored('''
===================================
Scan all parts or a specific port
[1] ===> Normal Scan
[2] ===> Scan specific port 
===================================
Please Enter Option ====> ''', color='red'))

# IF For Option
if user_op == '1':
    print(colored('===================================', color='blue'))
    # Value Input
    name_site = input('Enter Name Site Or Ip ===> ')
    # Scan
    sys(f'nmap {name_site}')
    print(colored('===================================', color='blue'))
    print(colored(figlet_format('Done'), color='green'))

elif user_op == '2':
    print(colored('===================================', color='blue'))
    # Value Input
    name = input('Enter Name Site Or Ip ===> ')
    port = int(input('Which port to scan ===> '))

    # Scan
    print('=======================================================')
    sys(f'nmap -p {port} {name}')
    print(colored('===================================', color='blue'))
    print(colored(figlet_format('Done'), color='green'))

else:
    print(colored('===================================', color='blue'))
    print(colored('Error ===> Please enter the correct values! Run the program once more.', color='red'))


# Create By Moein Heshmati
# Finish
