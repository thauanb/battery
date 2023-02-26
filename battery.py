import psutil 
import time
from os import system
from plyer import notification
from colorama import Fore, Style

# Define as cores
green = Fore.GREEN
red = Fore.RED
style_reset =Style.RESET_ALL
# Simbolos
simbol_ok = f'[{green}+{style_reset}]'
simbol_fail = f'[{red}-{style_reset}]'
simbol_exclamation = f'[{red}!{style_reset}]'

def limparTela():
    system('cls')

def check():
    battery   = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    isplugged = f"{simbol_ok} Conectado" if plugged==True else f"{simbol_fail} Desconectado"
    print(f'{simbol_ok} Bateria   -> {percent}')

    if (percent == 100) and (plugged==True):
        notification.notify(title='Bateria  100%',message='A bateria está completamente carregada',timeout=100)
        input()
        return True
    return False

system('title Battery Saver')
minutes_to_wait = 5


def run(mode:bool):
    while mode==True:
        limparTela()
        print('======== Battery Saver ========\n ')
        check()
        print()
        print(f'{simbol_exclamation} Verificando a cada {minutes_to_wait}min ...')
        time.sleep(minutes_to_wait*60)
        check()

run(True)










'''
Psutil -> https://psutil.readthedocs.io/en/latest/

'''