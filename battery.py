import psutil 
import time
from os import system
from plyer import notification

def limparTela():
    system('cls')

def check():
    battery   = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    isplugged = "[+] Conectado" if plugged==True else "[-] Desconectado"

    print(f'[+] Bateria   -> {percent}')
    print(f'{isplugged}')


    if (percent == 100) and (plugged==True):
        notification.notify(title='Bateria  100%',message='A bateria está completamente carregada',timeout=10)
        return True
    return False

system('title Battery Saver')
minutes_to_wait = 1


while check() == False:
    limparTela()
    print('======== Battery Saver ========\n ')
    check()
    print()
    print(f'[.] Verificando a cada {minutes_to_wait}min ...')
    time.sleep(minutes_to_wait*60)
input('[!]..')







'''
Psutil -> https://psutil.readthedocs.io/en/latest/

'''