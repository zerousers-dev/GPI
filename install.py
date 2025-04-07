import os
import time

os.system('clear')
print('[---GPI---]')
print('Welcome to GPI (GitHub Program Installer)')
print()
print('A program installer for Linux Mint.')
print('----------')
input()
os.system('clear')
print('Please select an option.')
print()
print('1. Install GPI')
print('2. Exit')
print()
choice = input('> ')
if choice == '1':
    os.system('clear')
    print('Installing GPI')
    
    # Escribir el script GPI en el archivo
    gpi_script = '''
import time
import os
import requests

os.system('clear')
print('[---GPI---]')
print('1. Install Program')
print('2. Exit')
print()
cmd = input('> ')
if cmd == '1':
    os.system('clear')
    programname = input('Program Name > ')
    response = requests.get(f'https://raw.githubusercontent.com/AaronVerdep/GPI/main/pgs/{programname}')
    if response.status_code == 200:
        os.system('clear')
        with open(f'/home/{os.getlogin()}/Desktop/{programname}', 'wb') as program:
            program.write(response.content)
        print('Program Installed on Desktop successfully!')
    else:
        os.system('clear')
        print('Cannot find the program.')
        input()
        exit()
else:
    os.system('clear')
    exit()
    '''
    
    # Guardar el script GPI en el directorio del usuario
    with open(f'/home/{os.getlogin()}/gpi.py', 'w') as gpi:
        gpi.write(gpi_script)
    
    # Añadir el alias en .bashrc sin sobrescribir
    with open(f'/home/{os.getlogin()}/.bashrc', 'a') as bashrc:
        bashrc.write(f'\nalias gpi="python3 /home/{os.getlogin()}/gpi.py"\n')

    print("GPI installed successfully and alias added to .bashrc!, Execute 'gpi' on terminal!")
else:
    os.system('clear')
    exit()
