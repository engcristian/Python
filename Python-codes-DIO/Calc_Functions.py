class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
        calc = Calculadora(self.valor_a, self.valor_b)

    def soma(self):
        return self.valor_a + self.valor_b
    def subtração(self):
        return self.valor_a - self.valor_b
    def multiplicação(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b
    def div_resto(self):
        return self.valor_a % self.valor_b
    def vel_med(self):
        return self.valor_a / self.valor_b
    def acel_med(self):
        return self.valor_a / self.valor_b

if  __name__ == '__main__':
    
    calc = Calculadora(10, 2)
    print(calc.soma())
    print(calc.subtração())
    print(calc.multiplicação())
    print(calc.divisao())
    print(calc.div_resto())
    print(calc.vel_med())
    print(calc.acel_med())  