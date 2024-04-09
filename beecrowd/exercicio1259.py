
def ordena_pares_impares(lista):
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0] 
    pares.sort()
    impares.sort(reverse=True)
    return pares + impares

N = int(input())

valores = []

for i in range(N):
    valor = int(input())
    valores.append(valor)

valores_ordenados = ordena_pares_impares(valores)

for valor in valores_ordenados:
    print(valor)