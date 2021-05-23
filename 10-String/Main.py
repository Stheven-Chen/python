data = 'ini adalah string'
print(data)
print(type(data))

#!. Cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''
data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)
#bisa juga double quote dan single quote digunakan berbarengan

#2. Menggunakan backslash \
print('hari ini hari jum\'at')
print('isn\'t it?')
print('C:\\User\\Stheven')

#Tab
print('Menggunakan\ttab') #seperti tab pada word

#backspace
print('Menggunakan \bbackslash')

#newline
print('baris pertama\nbaris kedua') #LF= Line Feed -> unix, macos, linux
print('baris pertama\rbaris kedua') #CR= Carriage Return -> acorn, commodore, lips
print('baris pertama\r\nbaris kedua') #CRLF= Line Feed Carrieage Return -> Windows

#3. String Raw atau literal
print('C:\new folder')#akan di enter
print(r'C:\new folder')#solusinya pada r di depan atau raw
#Multiline literal string
print('''
Nama: Stheven
NIM: 20184520005
''')

#Multiline and raw string
print(r'''Nama: Stheven
NIM: 20184520005
C:\newuser\tab\read
''')