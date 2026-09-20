sayi = int(input("Sayiyi giriniz: "))
ters_sayi = 0

while sayi > 0:
    # Son basamağı al
    basamak = sayi % 10
    # Ters çevrilen sayıya bu basamağı ekle
    ters_sayi = (ters_sayi * 10) + basamak
    # Son basamağı at
    sayi = sayi // 10

print("Ters çevrilmiş sayı:", ters_sayi)
