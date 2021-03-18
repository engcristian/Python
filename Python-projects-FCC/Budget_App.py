class Categoria:
  def __init__(self, nome):
    self.nome = nome
    self.registro = []

  def saque(self, quantidade, descrição = ""):
    if self.check_fundos(quantidade):
      self.registro.append({"quantidade": -quantidade, "descrição": descrição})
      return True
    else:
      return False

  def deposito(self, quantidade, descrição = ""):
    self.registro.append({"quantidade": quantidade, "descrição": descrição})

  def obter_balanço(self):
    total = 0
    for item in self.registro:
      total += item['quantidade']
    return total

  def transferência(self, quantidade, orçamento_categoria):
    if self.check_fundos(quantidade):
      self.saque(quantidade, f"Transferência para {orçamento_categoria.nome}")
      orçamento_categoria.deposito(quantidade, f"Transferência de {self.nome}")
      return True
    else:
      return False

  def check_fundos(self, quantidade):
    if quantidade <= self.obter_balanço():
      return True
    else:
      return False

  def __str__(self):
    saida = self.nome.center(30, "*") + "\n"
    for item in self.registro:
      saida += f"{item['descrição'][:23].ljust(23)}{format(item['quantidade'], '.2f').rjust(7)}\n"
    saida += f"Total: {format(self.obter_balanço(), '.2f')}"
    return saida

def gráfico_de_registros(categorias):
  categoria_nomes = []
  gastos = []
  porcento_gasto = []

  for categoria in categorias:
    total = 0
    for item in categoria.registro:
      if item['quantidade'] < 0:
        total -= item['quantidade']
    gastos.append(round(total, 2))
    categoria_nomes.append(categoria.nome)

  for quantidade in gastos:
    porcento_gasto.append(round(quantidade / sum(gastos), 2)*100)

  gráfico = "Porcentagem gasta por categoria:\n"

  labels = range(100, -10, -10)

  for label in labels:
    gráfico += str(label).rjust(3) + "| "
    for porcento in porcento_gasto:
      if porcento >= label:
        gráfico += "o  "
      else:
        gráfico += "   "
    gráfico += "\n"

  gráfico += "    ----" + ("---" * (len(categoria_nomes) - 1))
  gráfico += "\n     "

  len_maior_nome = 0

  for nome in categoria_nomes:
    if len_maior_nome < len(nome):
      len_maior_nome = len(nome)

  for i in range(len_maior_nome):
    for nome in categoria_nomes:
      if len(nome) > i:
        gráfico += nome[i] + "  "
      else:
        gráfico += "   "
    if i < len_maior_nome-1:
      gráfico += "\n     "
  
  return(gráfico)

if __name__ == '__main__':

  comida = Categoria("Comida")
  comida.deposito(1000, "Deposito inicial")
  comida.saque(10, "Mercearia")
  comida.saque(15, "Restaurantet")
  
  
  roupas = Categoria("Roupas")  
  comida.transferência(50, roupas) 
  roupas.saque(25, 'T-shirt')
  

  carro = Categoria("Carro") 
  carro.deposito(1000, "Deposito inicial")
  carro.saque(50,'Combustível')
  carro.saque(150, 'Motor')

  print(comida)
  print(roupas)
  print(carro)

  print('Balanço Geral')
  print(comida.obter_balanço())
  print(roupas.obter_balanço())
  
  print(carro.obter_balanço())

  print(gráfico_de_registros([comida, roupas, carro]))

