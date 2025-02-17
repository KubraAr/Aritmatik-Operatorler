#Görev1
sayi1 = int(input("Birinci sayıyı girin:"))
sayi2 = int(input("İkinci sayıyı girin:"))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi2 / sayi1
tam_bolme = sayi1//sayi2
mod = sayi1 % sayi2 
us = sayi1 ** sayi2

#Sonuçları ekrana yazdır
print("Toplam:", toplam)
print("Fark:", fark)
print("Çarpım:", carpim)
print("Bölüm:", bolum)
print("Tam Bölme:", tam_bolme)
print("Mod:", mod)
print("Üs:", us)

#Görev2
pi = 3.14

yaricap = float(input("Yarıçap giriniz:"))
dairenin_alani = pi * (yaricap ** 2)

#Sonucu ekrana yazdır
print("Dairenin Alanı:", dairenin_alani)
