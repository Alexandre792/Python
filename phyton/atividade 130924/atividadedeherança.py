class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calculo_de_salario(self):
        return self.salario_base
        
class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus):
        Empregado.__init__(self, nome, salario_base)
        self.bonus = bonus

    def calculo_de_salario(self):
        return self.salario_base + self.bonus
   
    
class Vendedor(Empregado):
     def __init__(self, nome, salario_base, comissão, vendas):
         Empregado.__init__(self, nome, salario_base)
         self.comissão = comissão
         self.vendas = vendas

     def calculo_de_salario(self):
        return self.salario_base + (self.comissão * self.vendas)
     
gerente = Gerente(nome="Alexandre", salario_base=6000, bonus=500)
vendedor = Vendedor(nome="Rodrigo", salario_base=2500, comissão=0.07, vendas=1500)

print(f"salario do gerente é{gerente.nome}:{gerente.calculo_de_salario()}")
print(f"o salario do vendedor é{vendedor.nome}:{vendedor.calculo_de_salario()}")
      

