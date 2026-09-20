my_string = input("Bir kelime girin:")
i = 0

for i in range(len(my_string)):
    if(i % 2 == 0):
        print("\n",my_string[i])