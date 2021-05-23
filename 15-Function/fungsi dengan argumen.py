def siswa(nama):
    print('siswa ini bernama:',nama)

siswa('mario')
#fungsi menggunakan keyword argumen
def guru(nama,pelajaran):
    print(f'{nama} mengajar {pelajaran}')

guru(nama='titin', pelajaran='sbk')
guru(pelajaran='penjas', nama='chandra')

#fungsi menggunakan default argument
def penjagaSekolah(nama,shift='siang',sifatnya='galak'):
    print(f'{nama} jaga di shift {shift}, sifatnya {sifatnya}')
penjagaSekolah('maman',shift='malam')
penjagaSekolah('entis')
penjagaSekolah('supyadi', sifatnya='tidak galak')
penjagaSekolah('asep', sifatnya='sangat galak')