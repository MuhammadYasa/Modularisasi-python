from geometri.persegi_panjang import persegi_panjang, info as info_persegipanjang # cara import nya sama, tinggal klik tanda merah
# kalau ingin menambahkan beberapa fungsi dari 1 file, tinggal memakai comma
from geometri.segitiga import luas_segitiga, info as info_segitiga #import ter mudah
from geometri.segitiga import luas_segitiga as ls
import geometri.segitiga # import ter ribet
import geometri.segitiga as kuy # cara ribet dengan as

print(f'luas_segitiga dengan alias (as) = {ls (10, 3)}') # f = string python agar bisa menghitung nilai, cara mudah ke 2
print(f'luas_segitiga cara ter mudah = {luas_segitiga (10, 3)}') # cara ter mudah
print(f'\nluas_segitiga cara ribet 1 = {geometri.segitiga.luas_segitiga (10, 3)}') # cara ribet
print(info_segitiga())
print(f'\nluas_segitiga cara ribet 2 = {kuy.luas_segitiga (10, 3)}') #cara ribet dengan as

print(info_persegipanjang())
print(f'\nluas_persegi_panjang  = {persegi_panjang (10, 3)}') # \n = untuk new line / enter

