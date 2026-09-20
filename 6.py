
dizi = []
n = 0
print("Diziye eklemek için sayilari girin ve bittiginde q tusuna basin")

while True :
    eleman = input("Bir sayi girin:")
    if eleman == 'q' :
        break
    else:
        dizi.append(int(eleman))
    n+1 
print("Olusturdugunuz dizi:",dizi)
if(dizi[0]==dizi[n-1]):
    print("Sonuc dogru")
else:
    print("Sonuc yanlis")