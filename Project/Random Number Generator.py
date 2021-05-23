import random as ran
from os import system
import platform

def title():
    print(20*'='+'Random Number Generator V 1.0'+'='*20)

def clean ():
    clean = platform.system().lower()
    if 'windows' in clean:
        system('cls')
    else :
        system('clear')

def masuk():
    x = ''
    while x != 'y'and x !='n':
        try:
            x = str(input('Do you want a random number? (y/n) ')).lower()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()

        clean()
        title()
        if x == 'y':
            a = int(input('Number from: '))
            b = int(input('to:'))
            r = ran.randint(int (a),int (b))
            print (f'Your random number between {a} to {b} is: ',r)
        elif x == 'n':
            print ('bye')
            break

def main_program():
    while True:
        clean()
        title()
        masuk()
        while True:
            ans = str(input('\nRandom number again? (y/n): '))
            if ans in ('y', 'n'):
                break
            print("???")
        if ans == 'y':
            clean()
            continue
        else:
            print("Bye")
            break


main_program()