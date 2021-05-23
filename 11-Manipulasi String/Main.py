#Gabung beberapa string

nama = 'Stheven'
NIM = '20184520005'
data = nama + ' '+ NIM
print(data)

#Menghitung panjang string
panjang = len(data)
print('Panjanng string dari',data + ' ' + 'adalah:',  panjang)

#mengecek apakah ada char di dalam string
s = '\ns'
status = s in data
print (s + ' ada di ' + data + ' = ' + str(status))

s = 'S'
status = s in data
print (s + ' ada di ' + data + ' = ' + str(status))

s = 'even'
status = s in data
print (s + ' ada di ' + data + ' = ' + str(status))

s = 's'
status = s not in data
print (s + ' tidak ada di ' + data + ' = ' + str(status))

s = 'S'
status = s not in data
print (s + ' tidak ada di ' + data + ' = ' + str(status))

#Mengulang String
print(10*'=')
print('='*20)

#indexing
print('index ke-0 adalah: '+data[0])
print('index ke-5 adalah: '+data[5])
print('index ke-(-1) adalah: '+data[-1])
print('index 0 sampai 7: '+ data [0:7])
print('index ke 0,2,4,6,8,10: '+data [0:10:2])

#item paling kecil
print('item paling kecil:'+min(data)) #hasilnya adalah spasi
print('item paling besar:'+max(data))

#operator dalam method 
coba = 'aloha everybody im here'
jumlah = coba.count('e')
print('jumlah dari huruf "e": ', jumlah)

#case
#ubah semua ke uppercase
data = 'stheven'
print(data.upper())

#pengecekan dengan isx method 
#apakah string lower semua
cek = data.islower()
print(cek)
cek = data.isupper()
print(cek)

#isalpha() apakah semuanya huruf
#isalnum() huruf dan angka
#isdecimal() angka saja
#isspace() string kosong 
#istitle() semua  kata dimulai dengan uppercase

judul = 'It Is Ok Not To Be Orkay'
cek = judul.istitle()
print(cek)
#cek komponen startwith() dan endwith()
cek_start =  'Sangjangnim Oppa'.startswith('Sangjangnim')
print('Start: ' + str(cek_start))
cek_start =  'Sangjangnim Oppa'.startswith('sangjangnim')
print('Start: ' + str(cek_start))
cek_end =  'Sangjangnim Oppa'.endswith('Oppa')
print('end: ' + str(cek_end))
cek_end =  'Sangjangnim Oppa'.endswith('oppa')
print('end: ' + str(cek_end))

#Komponen join() split()
pisah = ['me', 'i', 'you']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = ' '.join(pisah)
print(gabungan)
gabungan = ' yey '.join(pisah)
print(gabungan)

gabungan = 'ilalamelalayou'
print(gabungan.split('lala'))

#alokasi karakter
print(5*'=' + 'data' + '='*5)
#bisa menggunakan rjust() dan ljust() center()
kanan = 'kanan'.rjust(10)
print("'" + kanan + "'")
kiri = 'kiri'.ljust(10)
print("'" + kiri + "'")
center = 'center'.center(10)
print("'" + center + "'")
center = 'center'.center(20,'=')
print("'" + center + "'")

#kebalikan (strip)

center = center.strip('=')
print("'" + center + "'")
