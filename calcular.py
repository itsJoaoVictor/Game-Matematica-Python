from random import randint

class Calcular:
    def __init__(self: object, dificuldade: int,/):
        self.__dificuldade: int = dificuldade
        self.__valor_1: int = self.__gerar_valor
        self.__valor_2: int = self.__gerar_valor
        self.__operacao: int = randint(0, 2) # 0 = soma, 1 = subtração, 2 = multiplicação
        self.__resultado: int = self.__gerar_resultado
        
    
    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade
    
    @property
    def valor_1(self: object) -> int:
        return self.__valor_1
    
    @property
    def valor_2(self: object) -> int:
        return self.__valor_2
    
    @property
    def operacao(self: object) -> int:
        return self.__operacao
    
    @property
    def resultado(self: object) -> int:
        return self.__resultado
    
    def __str__(self) -> str:
        op: str = ""
        if self.__operacao == 0:
            op = "soma"
        elif self.__operacao == 1:
            op = "subtração"
        elif self.__operacao == 2:
            op = "multiplicação"
        else:
            op = "Operação inválida"
        return f'Valor 1: {self.__valor_1}\nValor 2: {self.__valor_2}\nOperação: {op}\nResultado: {self.__resultado}'
    
    
    @property
    def __gerar_valor(self: object) -> int:
        if self.__dificuldade == 1:
            return randint(0, 10)
        elif self.__dificuldade == 2:
            return randint(0, 100)
        elif self.__dificuldade == 3:            
            return randint(0, 1000)
        elif self.__dificuldade == 4:
            return randint(0, 10000)
    
    
    @property
    def __gerar_resultado(self: object) -> int:
        if self.__operacao == 0:
            return self.__valor_1 + self.__valor_2
        elif self.__operacao == 1:
            return self.__valor_1 - self.__valor_2
        elif self.__operacao == 2:
            return self.__valor_1 * self.__valor_2
        
    @property
    def op_simbolo(self: object) -> str:
        if self.__operacao == 0:
            return "+"
        elif self.__operacao == 1:
            return "-"
        elif self.__operacao == 2:
            return "*"
        
    
    def checar_resultado(self: object, resposta: int) -> bool:
        if self.__resultado == resposta:
            print("Parabéns, você acertou!")
            certo = True
        else:
            print("Que pena, você errou!")
            certo = False
        print(f'{self.__valor_1} {self.op_simbolo} {self.__valor_2} = {resposta}')
        return certo
    
    def mostrar_operacao(self: object) -> str:
        return f'{self.__valor_1} {self.op_simbolo} {self.__valor_2} = ?'
        