def desen_ciz(satir_sayisi):
    for i in range(satir_sayisi, 0, -1):
        print('* ' * i)

# Kullanıcıdan satır sayısını al
satir_sayisi = int(input("Desen için satır sayısını giriniz: "))
desen_ciz(satir_sayisi)
