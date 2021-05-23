
from os import system
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


#==================================================

clean()
while True:#to restart program "Start"
    print ('''==========Konversi Temperature==========
Contoh input: c untuk celcius r untuk reamur
''')
#for determine from ke convert input
    dari = ''
    ke = ''
    #untuk dari
    while dari != 'C' and dari != 'K' and dari != 'F' and dari != 'R':
        try:
            dari = input('dari: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Dadah')
            exit()

    #untuk ke
    while ke != 'C' and ke != 'K' and ke != 'F' and ke != 'R':
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
        print('Hasil:',(y*9/5)+32,"F")
    elif(x=="C to R"):
        print('Hasil:',4/5*y,"R")
    elif(x=="C to K"):
        print ('Hasil:',y+273,"K")
    elif (x=="F to C"):
        print('Hasil:',5/9*(y-32),"C")
    elif(x=="F to R"):
        print ('Hasil:',4/9*(y-32),"R")
    elif (x=="F to K"):
        print ('Hasil:',(5/9*(y-32))+273,"K")
    elif(x=="R to C"):
        print('Hasil:',5/4*y,"C")
    elif(x=="R to F "):
        print ('Hasil:',(9/4*y)+32,"F")
    elif(x=="R to K"):
        print('Hasil:',(5/4*y)+273,"K")
    elif(x=="K to C"):
        print('Hasil:',y-273,"C")
    elif(x=="K to R"):
        print('Hasil:',4/5*(y-273),"R")
    elif (x=="K to F"):
        print('Hasil:',((y-273)*9/5)+32,"F")
    else:
        print("Cek Kembali Input")
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

    
