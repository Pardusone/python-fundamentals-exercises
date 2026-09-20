def palindrome(sayi):
    # Orijinal sayıyı saklıyoruz
    original_sayi = sayi

    # Sayıyı tersine çevirmek için reverse_num değişkenini başlatıyoruz
    reverse_num = 0 

    # Verilen sayıyı ters çevirmek için döngü başlatıyoruz
    while sayi > 0:
        reminder = sayi % 10  # Son basamağı al
        reverse_num = (reverse_num * 10) + reminder  # Ters çevrilen sayıyı oluştur
        sayi = sayi // 10  # Sayıyı bir basamak küçült

    # Orijinal sayı ile ters çevrilen sayıyı karşılaştırıyoruz
    if original_sayi == reverse_num:
        print("Sayı palindromdur")
    else:
        print("Sayı palindrom değildir")

# Kullanıcıdan bir sayı alıyoruz ve fonksiyonu çağırıyoruz
sayi = int(input("Lütfen bir sayı giriniz: "))
palindrome(sayi)
