def calcularPontos(ordem, sistemaPontuacao):
    pontos = [0] * len(ordem)
    for idx, posicao in enumerate(ordem):
        if posicao <= sistemaPontuacao['ultimaPosicao']:
            pontos[idx] = sistemaPontuacao['pontos'][posicao - 1]
    return pontos

def main():
    while True:
        numeroCorridas, numeroPilotos = map(int, input().split())
        if numeroCorridas == 0 and numeroPilotos == 0:
            break
        
        resultadosCorrida = []
        for n in range(numeroCorridas):
            resultadosCorrida.append(list(map(int, input().split())))
        
        numeroSistemasPontuacao = int(input())
        for n in range(numeroSistemasPontuacao):
            sistemaPontuacao = {}
            ultimaPosicao, *pontos = map(int, input().split())
            sistemaPontuacao['ultimaPosicao'] = ultimaPosicao
            sistemaPontuacao['pontos'] = pontos
            
            pontosPilotos = [0] * numeroPilotos
            for resultadoCorrida in resultadosCorrida:
                pontosCorrida = calcularPontos(resultadoCorrida, sistemaPontuacao)
                for idx in range(numeroPilotos):
                    pontosPilotos[idx] += pontosCorrida[idx]
            
            maxPontos = max(pontosPilotos)
            campeoes = [str(idx + 1) for idx, pontos in enumerate(pontosPilotos) if pontos == maxPontos]
            print(' '.join(campeoes))

if __name__ == "__main__":
    main()