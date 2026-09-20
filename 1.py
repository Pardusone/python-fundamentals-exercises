def deneme(number1,number2):
    if(number1*number2 > 1000):
        print("sonuc:",number1 + number2)
    elif(number1*number2 < 1000):
        print("sonuc:",number1*number2)

number1 = int(input("Birinci sayiyi girin:"))
number2 = int(input("Ikinci sayiyi girin:"))

deneme(number1 , number2)    