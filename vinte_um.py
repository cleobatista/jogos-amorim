from random import randint

def tira_carta():
    return randint(1, 10)

def vinte_um():
    participantes = {}
    participante = True
    while participante:
        participante = input('Inclua mais um participante ou vazio para concluir: ')
        if participante:
            participantes[participante] = 0
    for participante in participantes.keys():
        carta_1 = tira_carta()
        carta_2 = tira_carta()
        participantes[participante] = carta_1 + carta_2
        print(f"{participante} tirou as cartas {carta_1} e {carta_2}, totalizando {participantes[participante]}") 

    perdedores = []
    for participante in participantes.keys():
        continua = input(f"{participante} quer continuar? Qualquer letra para sim, vazio para não: ")
        if continua:
            carta = tira_carta()
            participantes[participante] += carta
            if participantes[participante] == 21:
                print(f"Parabéns {participante}, você ganhou com {participantes[participante]} pontos!")
                return 
            elif participantes[participante] > 21:
                print(f"Que pena {participante}, você tirou {carta} e estourou os pontos!")
                perdedores.append(participante)
    
    for perdedor in perdedores:
        del participantes[perdedor]

    print(participantes)
    vencedor = max(participantes, key=participantes.get)
    print(f"Parabéns {vencedor}, você ganhou com {participantes[vencedor]} pontos!")
    return
if __name__ == '__main__':
    vinte_um()