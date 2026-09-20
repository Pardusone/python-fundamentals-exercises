print("Bir sayi dizisi giriniz ve cıkmak icin q tusuna basiniz")

dizi = []

while True :
    eleman = input("Bir sayi giriniz:")
    if(eleman == 'q'):
        break
    else:
        dizi.append(int(eleman))
    

for i in range(len(dizi)):
    if(dizi[i] % 5 == 0):
        print("5'e bolunen sayilar bunlardir:",dizi[i])

