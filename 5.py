word = input('enter word')
print("Original string", word)

size = len(word)



print("Printing only even index chars")

for i in range(0, size - 1,2):
    print("index[",i,"]",word[i])
