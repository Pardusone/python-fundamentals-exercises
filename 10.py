print("Bir sayı dizisi giriniz ve çıkmak için 'q' tuşuna basınız")

dizi_cift = []
dizi_tek = []
dizi_yeni = []

# Çift sayıları kullanıcıdan al
while True:
    eleman1 = input("Bir çift sayı giriniz (çıkmak için 'q' tuşuna basınız): ")
    if eleman1 == 'q':
        break
    else:
        dizi_cift.append(int(eleman1))  # Sayıyı int tipine dönüştür

# Tek sayıları kullanıcıdan al
while True:
    eleman2 = input("Bir tek sayı giriniz (çıkmak için 'q' tuşuna basınız): ")
    if eleman2 == 'q':
        break
    else:
        dizi_tek.append(int(eleman2))  # Sayıyı int tipine dönüştür

# Yeni diziyi oluştur
for num in dizi_cift:
    if num % 2 == 0:  # Sayı çiftse
        dizi_yeni.append(num)

for num in dizi_tek:
    if num % 2 != 0:  # Sayı tekse
        dizi_yeni.append(num)

print("Yeni diziniz:", dizi_yeni)
