gorengan = ['pisang goreng','tempe','tahu isi','tahu bulat','ubi']
saya_mau = str(input('Saya mau: '))

if saya_mau in gorengan:
    print(f'ada {saya_mau}nya')
if saya_mau not in gorengan:
    print(f'saya gak jual {saya_mau}')
