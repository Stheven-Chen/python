from os import system
import platform

def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

clean()
print('''
Ini program buat ngecek nim anak fismed 18 Universitas Matana.
cuma ada akhiran nim dari 1-13.
''')
while True:
    nim = int(input("Masukkan Akhiran NIM : "))
    if(nim==5):
          print("Stheven")
    elif (nim==1):
        print("Agripa")
    elif (nim==2):
        print("Yohana")
    elif (nim==3):
        print("Juli")
    elif (nim==4):
        print("Leo")
    elif (nim==6):
        print("Ino")
    elif (nim==11):
        print("Adel")
    elif (nim==13):
        print("Panji")
    else:
        print("Gak Ada Orangnya Udah Keluar Kali")
    while True:
        answer = str(input('Cari lagi? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Cek lagi.")
    if answer == 'y':
        clean()
        continue
    else:
        print("Dadah")
        break
