"""
fungsi menghitung luas segitiga
dengan rumus
luas segitiga = alas (kali) tinggi (dibagi) 2
di tulis dalam bahasa pemrograman
luas_segitiga = alas * tinggi / 2
"""

print('menghitung luas segitiga pertama #01')
alas = 20
tinggi = 7
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi {tinggi} memiliki luas {luas_segitiga} cm')

print('\nmenghitung luas segitiga kedua #02 dengan copy paste')
alas = 5
tinggi = 20
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi {tinggi} memiliki luas {luas_segitiga} cm')

# fungsi luas segitiga
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga # mengembalikan nilai hasil dari penghitungan luas segitiga

print('\nmenghitung luas segitiga dengan fungsi')
print(f'hitung luas segitiga #01 = {hitung_luas_segitiga(20,7)} cm')
print(f'hitung luas segitiga #02 = {hitung_luas_segitiga(5,20)} cm')

alas = 77
tinggi = 44
print(f'Dengan fungsi, alas = {alas} dan tinggi = {tinggi} memiliki luas segitiga = {hitung_luas_segitiga(66,4)} cm')