for num in range(1, 101):
    # Her yeni satırda bir önceki satırın sonuna num yazdırılır
    print(num, end=" ")
    # Eğer num 10'un katı ise yeni satıra geç
    if num % 10 == 0:
        print()  # Yeni satıra geç
