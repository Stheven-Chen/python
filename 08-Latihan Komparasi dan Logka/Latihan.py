#-----0+++++5------8++++++11------
# dan kebalikannya 
print('No 1 Skemanya -----0+++++5------8++++++11------')
user = float(input('angka dibawah 0 false dibawah 5 true\ndibawah 8 false dibawah 11 true: '))

num0 = (user > 0)
#print ('num0:',num0)
num5 = (user < 5)
#print('num5: ',num5)
num8 = (user > 8)
#print('num8: ',num8)
num11 = (user < 11)
#print('num11: ',num11)

hasil = num0 and num5 or num8 and num11
print('Angka yang dimasukkan: ', hasil)

#+++++0-----5+++++8-----11+++++
print('=========')
print('No 2 Skemanya +++++0-----5+++++8-----11+++++')
user = float(input('Angka dibawah 0 true, dibawah 5 false\ndibawah 8 true, dibawah 11 false: '))
num0 = (user < 0)
#print ('num0:',num0)
num5 = (user > 5)
#print('num5: ',num5)
num8 = (user < 8)
#print('num8: ',num8)
num11 = (user > 11)
#print('num11: ',num11)

hasil = num0 or num5 and num8 or num11
print('Angka yang dimasukkan: ', hasil)