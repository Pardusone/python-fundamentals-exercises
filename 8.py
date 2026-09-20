# Kullanıcıdan bir cümle ve aranacak kelimeyi alıyoruz
Cumle = input("Lütfen cümleyi giriniz: ")
Kelime = input("Lütfen aranacak kelimeyi giriniz: ")

# Cümledeki kelimenin tekrar sayısını buluyoruz
tekrar = Cumle.count(Kelime)

# Sonucu ekrana yazdırıyoruz
print(tekrar)
