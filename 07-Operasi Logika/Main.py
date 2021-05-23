# ada operasi logika not, or, and, xor

# Not 
print('===========Not')
a = True 
c = not a
print('data a: ',a)
print('jika di not')
print('data c: ',c)

# OR (Jika ada truenya maka akan menjadi true)
print('===========OR')
a = True
b = False  
c = a or b
print(a, ' OR', b, '=', c)
print('===========OR')
a = True
b = True  
c = a or b
print(a, ' OR', b, '=', c)
print('===========OR')
a = False
b = False  
c = a or b
print(a, 'OR', b, '=', c)
print('===========OR')
a = False
b = True  
c = a or b
print(a, 'OR', b, '=', c)

# AND (Jika ada 2 nilai true baru akan menjadi true)
print('===========and')
a = True
b = False  
c = a and b
print(a, ' and', b, '=', c)
print('===========and')
a = True
b = True  
c = a and b
print(a, ' and', b, '=', c)
print('===========and')
a = False
b = False  
c = a and b
print(a, 'and', b, '=', c)
print('===========and')
a = False
b = True  
c = a and b
print(a, 'and', b, '=', c)

# XOR (Akan tre jika hanya 1 sisi yang ada true)
print('===========xOR')
a = True
b = False  
c = a ^ b
print(a, ' xOR', b, '=', c)
print('===========xOR')
a = True
b = True  
c = a ^ b
print(a, ' xOR', b, '=', c)
print('===========xOR')
a = False
b = False  
c = a ^ b
print(a, 'xOR', b, '=', c)
print('===========xOR')
a = False
b = True  
c = a ^ b
print(a, 'xOR', b, '=', c)