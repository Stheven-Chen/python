#integer data bilangan bulat
integer= 12
print(type(integer))
print(integer,"adalah data", type(integer))

#float data bilangan desimal
float= 12.0
print(type(float))
print(float,"adalah data", type(float))

#string data karakter
string="Stheven"
print(type(string))
print(string,"adalah data", type(string))

#bolean data true dan false saja
bolean=True
print(type(bolean))
print(bolean,"adalah data", type(bolean))

#complex data bilangan imaginer
compleks=complex(2,6) #2 adalah bilagan real dan 6 imaginernya
print(type(compleks))
print(compleks,"adalah data", type(compleks))

#untuk jenis data c yang lain seperti long, short dll harus di import dulu
from ctypes import c_double, c_short
long=c_double(2.0)
print(type(long))
print(long,"adalah data", type(long))