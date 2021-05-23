a=7; b=12

#Pertambahan +
hasil=a+b
print(a,"+", b, "=", hasil)

#Pengurangan -
hasil=a-b
print(a,"-", b, "=", hasil)

#Perkalian *
hasil=a*b
print(a,"x", b, "=", hasil)

#Pembagian /
hasil=a/b
print(a,"/", b, "=", hasil)

#Pangkat **
hasil=a**b
print(a,"^", b, "=", hasil)

#Sisa Pembagian (Modulus) %
hasil=b%a
print(b,"%", a, "=", hasil)

#Kebalikan Modulus (Floor Division)//
hasil=b//a
print(b,"//", a, "=", hasil)

#Prioritas Operasi (Math Rules)
"""
Urutannya 1. (), 2. **, 3. */**%//, 4. +-
"""
x=3
y=4
z=2
Hasil=x**y*z+x/y-y%z//x #akan disesuaikan dengan aturan operasi metematika
print(x,"**",y,"*",z,"+",x,"/",'y',"-",y,"%",z,"//",x,"=",Hasil)
