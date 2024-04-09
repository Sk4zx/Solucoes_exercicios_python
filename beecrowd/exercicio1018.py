valor = int(input())
if valor < 0 or valor > 1000000:
    print("Numero invalido")
notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for nota in notas:
    qtdNotas = valor // nota
    print("{} nota(s) de R$ {:.2f}".format(qtdNotas, nota).replace('.',','))
    valor = valor % nota