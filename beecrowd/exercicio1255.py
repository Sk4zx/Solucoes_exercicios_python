def contar_frequencia_letras(texto):
    frequenciaLetras = {}
    
    for ch in texto:
        if ch.isalpha():
            if ch in frequenciaLetras:
                frequenciaLetras[ch] += 1
            else:
                frequenciaLetras[ch] = 1
    
    Frequencia = max(frequenciaLetras.values())
    letrasMaxFrequencia = []
    
    for letra, frequencia in frequenciaLetras.items():
        if frequencia == Frequencia:
            letrasMaxFrequencia.append(letra)
    
    letrasMaxFrequencia.sort()
    
    return ''.join(letrasMaxFrequencia)

N = int(input())

for i in range(N):
    texto = input().lower()
    resultado = contar_frequencia_letras(texto)
    print(resultado)