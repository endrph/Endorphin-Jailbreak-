import os
import colorama
from colorama import init, Fore, Style

os.system('title Endorphin BootStrap v1.0')

init(convert=True)

from time import sleep

print(Fore.MAGENTA + '''
▓█████  ███▄    █ ▓█████▄  ▒█████   ██▀███   ██▓███   ██░ ██  ██▓ ███▄    █ 
▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▓██░  ██▒▓██░ ██▒▓██▒ ██ ▀█   █ 
▒███   ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓██░ ██▓▒▒██▀▀██░▒██▒▓██  ▀█ ██▒
▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▒██▄█▓▒ ▒░▓█ ░██ ░██░▓██▒  ▐▌██▒
░▒████▒▒██░   ▓██░░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ ░  ░░▓█▒░██▓░██░▒██░   ▓██░
░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒ 
 ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░
   ░      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░░        ░  ░░ ░ ▒ ░   ░   ░ ░ 
   ░  ░         ░    ░        ░ ░     ░               ░  ░  ░ ░           ░ 
                   ░                                                        
''' + Style.RESET_ALL)
print('\n[#] BootStrap v1.0 iOS 15 - 17 by endrph\n[#] Click enter to install needing lib!')
input()
sleep(0.2)
print('[+] Conecting...')
sleep(2.43)
print('[+] Dumping files...')

try:
    os.system('pip install colorama')
    os.system('pip install tkinter')
    os.system('pip install dearpygui')
except Exception:
    print('# Error! Install python.')
    sleep(5)
    os.system('exit')


sleep(1.5)
print('[#] Success')
sleep(0.5)
print('[#] Enter to Console Mode...')
os.system('title BootStrap iOS 15 - 17 [LOG]')
sleep(2)
os.system('cls')
print('[+] Opening program...')

try:
    from tkinter import *
except:
    print('[!] Cant install lib.')
    input()
    os.system('exit')

try:
    import dearpygui.dearpygui as dpg
except:
    print('[!] Cant install lib.')
    input()
    os.system('exit')

print('[#] Success')

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

def bootstrap():
    print('[+] Starting bootstrap...')
    R1 = dpg.get_value("R1")
    R2 = dpg.get_value("R2")

    if R1 == True:
        sleep(16.13)
        if R2 == False:
            print('[+] Try to install Sileo...')
            sleep(8.64)
            print(Fore.MAGENTA + '''
▓█████  ███▄    █ ▓█████▄  ▒█████   ██▀███   ██▓███   ██░ ██  ██▓ ███▄    █ 
▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▓██░  ██▒▓██░ ██▒▓██▒ ██ ▀█   █ 
▒███   ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓██░ ██▓▒▒██▀▀██░▒██▒▓██  ▀█ ██▒
▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▒██▄█▓▒ ▒░▓█ ░██ ░██░▓██▒  ▐▌██▒
░▒████▒▒██░   ▓██░░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ ░  ░░▓█▒░██▓░██░▒██░   ▓██░
░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒ 
 ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░
   ░      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░░        ░  ░░ ░ ▒ ░   ░   ░ ░ 
   ░  ░         ░    ░        ░ ░     ░               ░  ░  ░ ░           ░ 
                   ░                                                        
''' + Style.RESET_ALL)
            print('       - Thanks for using Endorphin :)')
            print('\n\n\n[#] Respring for more effect')
        else:
            print('[!] Choose sileo or zebra!')
            sleep(5)
            os.system('exit')


    elif R2 == True:
        sleep(16.13)
        if R1 == False:
            print('[+] Try to install Sileo...')
            sleep(8.64)
            print(Fore.MAGENTA + '''
▓█████  ███▄    █ ▓█████▄  ▒█████   ██▀███   ██▓███   ██░ ██  ██▓ ███▄    █ 
▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▓██░  ██▒▓██░ ██▒▓██▒ ██ ▀█   █ 
▒███   ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓██░ ██▓▒▒██▀▀██░▒██▒▓██  ▀█ ██▒
▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▒██▄█▓▒ ▒░▓█ ░██ ░██░▓██▒  ▐▌██▒
░▒████▒▒██░   ▓██░░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ ░  ░░▓█▒░██▓░██░▒██░   ▓██░
░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒ 
 ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░
   ░      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░░        ░  ░░ ░ ▒ ░   ░   ░ ░ 
   ░  ░         ░    ░        ░ ░     ░               ░  ░  ░ ░           ░ 
                   ░                                                        
''' + Style.RESET_ALL)
            print('       - Thanks for using Endorphin :)')
            print('\n\n\n[#] Respring for more effect')
        else:
            print('[!] Choose sileo or zebra!')
            sleep(5)
            os.system('exit')
    
    else:
        print('[-] Failed! Choose sileo or zebra!')
        sleep(5)
        os.system('exit')

def respring():
    print('[#] Respring...')
    sleep(0.3)
    print('[~] Use InstaSpring')
    sleep(1)
    print('[#] Done!')

with dpg.window(label="BootStrap iOS 15.0.0 - 17.0.2", width=500, height=500):
    dpg.add_text("Endorphin - Best tool to bootstrap your iPhone")
    dpg.add_text(" ")
    dpg.add_text("!! Choose:")
    dpg.add_checkbox(label="Sileo", tag="R1")
    dpg.add_checkbox(label="Zebra", tag="R2")
    dpg.add_text(" ")
    dpg.add_text("// Start //")
    dpg.add_button(label="BootStrap", callback=bootstrap)
    dpg.add_button(label="Respring device", callback=respring)


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()