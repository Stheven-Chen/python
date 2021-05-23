
angka = 0
while angka <=5:
    print('nilai angka adalah ',angka)
    angka += 1

print(20*'=')
print('ini diluar while')

print(20*'=')
start = True
angka = 0
while start: #while boolean
    print('ini di dalam while')
    if angka is 100:
        start = False
        print('angka 100 ditemukan')
    angka +=1
    