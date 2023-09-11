class Operacao:
    def __init__(self, valor1, operador, valor2, resultado):
        self._valor1 = valor1
        self._operador = operador
        self._valor2 = valor2
        self._resultado = resultado

    def get_valor1(self):
        return self._valor1
    
    def set_valor1(self, novo_valor1):
        self._valor1 = novo_valor1

    def get_operador(self):
        return self._operador
    
    def set_operador(self, novo_operador):
        self._operador = novo_operador

    def get_valor2(self):
        return self._valor2
    
    def set_valor2(self, novo_valor2):
        self._valor2 = novo_valor2

    def get_resultado(self):
        return self._resultado
    
    def set_resultado(self, novo_resultado):
        self._resultado = novo_resultado


