#latihan area rentang dari angka

#mis: ++++++3-----10+++++
#maka yang diarea + akan true dan diarea - akan false

user = float(input('Masukkan angka yang bernilai\ndibawah 3 atau diatas 10: '))

#meriksa angka dibawah 3 
kurang3 = (user < 3)
#print(kurang3)

#Lebih dari 10
lebih10 = (user > 10)
#print(lebih10)
hasil = kurang3 or lebih10
print('Angkanya bernilai: ', hasil)

# contoh lain misalkan diubah jadi antara 3 dan 10 menjadi true
#-----3+++++10-----
user = float(input('Masukkan angka yang bernilai\ndiatas 3 dan dibawah 10: '))
kurang3 = (user > 3)
lebih10 = (user < 10)

hasil = kurang3 and lebih10
print('Angkanya bernilai: ', hasil)

