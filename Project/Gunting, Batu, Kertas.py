import random as r ; from os import system ; import platform

def clean():
    clean = platform.system().lower()
    if 'windows' in clean:
        system('cls')
    else :
        system ('clear')

def title():
    print(10*'='+'Selamat datang di permainan gunting batu kertas'+'='*10)

def main():
    kom = r.randint(1,3)
    hum = int()
    clean()
    title()
    input('Tekan enter untuk melanjutkan: ')
    clean()
    hum = int(input('Masukkan angka: \n1. Untuk batu\n2. Untuk Gunting\n3. Untuk Kertas\n:'))
    if kom == hum:
        print(kom)
        print('Seri')
    elif kom == 1 and hum == 2:
        print('Komputer Batu, Manusia Gunting')
        print('Kalah')
    elif kom == 2 and hum == 3:
        print('Komputer Gunting, Manusia Kertas')
        print('Kalah')
    elif kom == 3 and hum == 1:
        print('Komputer Kertas, Manusia Batu ')
        print('Kalah')
    elif kom == 3 and hum == 2:
        print('Komputer Kertas, Manusia Gunting')
        print('Menang')
    elif kom == 2 and hum == 1:
        print('Komputer Gunting, Manusia Batu')
        print('Menang')
    elif kom == 1 and hum == 3:
        print('Komputer Batu, Manusia Kertas')
        print('Menang')
    
def looping():
    while True:
        main()
        while True:
            ulang = str(input('\nMain lagi? (y/n): ')).lower()
            if ulang in ('y', 'n'):
                break
            print('???')
        if ulang =='y':
            clean()
            continue
        else :
            print ('Dadah')
            break

looping()
