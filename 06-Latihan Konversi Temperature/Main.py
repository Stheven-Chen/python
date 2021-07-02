
from os import pipe, system
import platform

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def welcome():
    print ('''==========Konversi Temperature==========
Contoh input: c untuk celcius r untuk reamur
''')

#==================================================

clean()
welcome()
while True:#to restart program "Start"
#for determine from ke convert input
    dari = ''
    ke = ''
    inputUser = ('C', 'R', 'K', 'F')
    #untuk dari
    while dari not in inputUser:
        try:
            dari = input('dari: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Dadah')
            exit()

    #untuk ke
    while ke not in inputUser:
        try:
            ke = input('ke: ').upper()
        except(EOFError,KeyboardInterrupt):
            print('Bye')
            exit()
            
    x=str((f"{dari} to {ke}"))

#for temperature input
    if dari == 'C':
        y=float(input("Temperature (Celcius): "))
    elif dari == 'F':
        y=float(input("Temperature (Farenheit): "))
    elif dari == 'R':
        y=float(input("Temperature (Reamur): "))
    elif dari == 'K':
        y=float(input("Temperature (Kelvin): "))
        
#Main Converter Program
    if(x=="C to F"):
        hasil=(y*9/5)+32
    elif(x=="C to R"):
        hasil=4/5*y
    elif(x=="C to K"):
        hasil=y+273.15
    elif (x=="F to C"):
        hasil=5/9*(y-32)
    elif(x=="F to R"):
        hasil=4/9*(y-32)
    elif (x=="F to K"):
        hasil=(5/9*(y-32))+273.15
    elif(x=="R to C"):
        hasil=5/4*y
    elif(x=="R to F "):
        hasil=(9/4*y)+32
    elif(x=="R to K"):
        hasil=(5/4*y)+273.15
    elif(x=="K to C"):
        hasil=y-273.15
    elif(x=="K to R"):
        hasil=4/5*(y-273.15)
    elif (x=="K to F"):
        hasil=((y-273.15)*9/5)+32
    else:
        print("Cek Kembali Input")
    pembulatan = round(hasil,2)
    print(y,dari,'dikonversi ke',ke,"sama dengan",pembulatan,ke)
    while True:#to restart program "end"
        answer = str(input('\nLagi? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Cek Kembali Input")
    if answer == 'y':
        clean()
        continue
    else:
        print("Dadah")
        break

    
