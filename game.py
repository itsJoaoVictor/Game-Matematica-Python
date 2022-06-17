from calcular import Calcular

def main():
    pontos = 0
    jogar (pontos)
    
def jogar(pontos: int) -> None:
    difculdade: int = int(input("Digite a dificuldade desejada [1, 2, 3 ou 4]: "))
    calc: Calcular = Calcular(difculdade)
    
    print('Qual é o resultado da operação:')
    print(calc.mostrar_operacao())
    
    resultado = int(input("Digite o resultado: "))
    
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Parabéns, você acertou! Você tem {pontos} ponto(s)')
        
    continuar = input("Deseja continuar? [S/N] ")
    
    if continuar.upper() == "S":
        jogar(pontos)
    else:
        print(f'Você fechou o jogo com {pontos} ponto(s)')
        print("Obrigado por jogar!")
    
    

if __name__ == "__main__":
    main()