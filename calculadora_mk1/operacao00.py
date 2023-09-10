class Operacao:
    def __init__(self, valor1, operador, valor2, resultado,):
        self._valor1 = valor1
        self._operador = operador
        self._valor2 = valor2
        self._resultado = resultado
    
    def get_valor1(self):
        return self._valor1
    
    def get_operador(self):
        return self._operador
    
    def get_valor2(self):
        return self._valor2
    
    def get_resultado(self):
        return self._resultado