import random
from os import system
import platform




def clean():
    x = platform.system().lower()
    if 'windows'in x:
        system('cls')
    else:
        system ('clear') 

def tebak(x):
    clean()
    no_acak = random.randint(1, x)
    tebak = 0
    while tebak != no_acak:
        tebak = int(input (f'Tebak angka antara 1 sampai {x}: '))   
        if tebak < no_acak:
            print ('Terlalu Kecil')
        elif tebak > no_acak:
            print('Terlalu Besar')
    print(f'Benar jawabannya {no_acak}')    


tebak(100)

