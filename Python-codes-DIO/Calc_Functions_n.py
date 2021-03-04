class Calculadora:
    
    def soma(self, valor_a,  valor_b):
        return valor_a + valor_b
    def subtração(self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicação(self,valor_a , valor_b):
        return valor_a * valor_b
    def divisao(self,valor_a , valor_b):
        return valor_a / valor_b
    def div_resto(self,valor_a , valor_b):
        return valor_a % valor_b
    def vel_med(self,valor_a , valor_b):
        return valor_a / valor_b
    def acel_med(self,valor_a , valor_b):
        return valor_a / valor_b
    
if __name__ =='__main__':

    print(calc.soma(10,20))
    print(calc.subtração(33, 15))
    print(calc.multiplicação(11, 5))
    print(calc.divisao(38,4))
    print(calc.div_resto(66,5))
    print(calc.vel_med(150,36))
    print(calc.acel_med(169,9))