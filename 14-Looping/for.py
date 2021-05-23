#List sebagai iterable
gorengan = ['tahu', 'ubi', 'tempe','pisang goreng']

for g in gorengan:
    print(g)
    print(len(g))

print(20*'=')
#string sebagai iterable

bakwan = 'bakwan'
for i in bakwan:
    print(i)

print(30*'=')
#for in for
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel','kentang','tomat']
daftar_belanja = [gorengan, buah, sayur]

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)

print(100*'+')
#for else range break
#range
for i in range(10,40,5):
    print(i)
print(range(10,40,5)) #bukan list

#else
print(20*'=')
number = 50
for i in range(0,40,1):
    print(i)
    if i is number:
        print('angka ditemukan',i)
        break #agar berhenti disaat 25 kalo lupa coba hapus break lalu di run lagi
else :
    print('angka tidak ditemukan')



