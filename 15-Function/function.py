#misalakan fungsi penambahan

#mendefinisikan fungsi
def suara_ayam():
    print('kukukuk')

def harga_ayam():
    suara_ayam()
    print('harga ayam Rp.60000/kg ')

#fungsi dengan input
def harga_total_ayam(kg):
    suara_ayam()
    harga = 60000
    hargaTotal = kg*harga
    print(f'Harga {kg}kg ayam adalah Rp.{hargaTotal}')

harga_total_ayam(12)

