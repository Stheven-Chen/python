#Digunakan untuk memendekkan operasi 

a = 5 #ini adalah assignment
print('nilai a:',a)
a += 1 #artinya a = a + 1 atau 5+1
print('nilai a di "+=" 1 akan menjadi:',a)
a -= 2
print('nilai a di "-=" 2 akan menjadi:',a)
a *= 2
print('nilai a di "*=" 2 akan menjadi:',a)
a -= 2
print('nilai a di "-=" 2 akan menjadi:',a)
a /= 2
print('nilai a di "/=" 2 akan menjadi:',a)

#Modulus dan floor division
b = 10
print('\nnilai b adalah:',b)
b %= 3 
print('nilai b di "%=" 3 akan menjadi:',b)

b = 10
print('\nnilai b adalah:',b)
b //= 3
print('nilai b di "//=" 3 akan menjadi:',b)

#Pangkat
b = 12
print('\nnilai b adalah:',b)
b **= 3 
print('nilai b di "**=" 3 akan menjadi:',b)

#OR
c = True
print('\nnilai c adalah:',c)
c |= False
print('nilai c di "|=" False akan menjadi:',c)
c = False
print('nilai c adalah:',c)
c |= False
print('nilai c di "|=" False akan menjadi:',c)

#AND
c = True
print('\nnilai c adalah:',c)
c &= False
print('nilai c di "&=" False akan menjadi:',c)
c = True
print('nilai c adalah:',c)
c &= True
print('nilai c di "&=" True akan menjadi:',c)

#XOR
c = True
print('\nnilai c adalah:',c)
c ^= False
print('nilai c di "^=" False akan menjadi:',c)
c = False
print('nilai c adalah:',c)
c ^= False
print('nilai c di "^=" False akan menjadi:',c)

