maior = 0
maior_i = 0
for i in range(0,100):
    n = int(input(""))
    if n > maior:
        maior = n
        maior_i = i
        
print("{}\n{}".format(maior,maior_i + 1))