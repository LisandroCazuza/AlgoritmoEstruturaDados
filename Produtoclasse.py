class Produtos():
  def __init__(self,nome, valor, quant ):
      self.__produto = nome 
      self.__preco = valor 
      self.__quantidade = quant
      #Buscar informação 
  def get_produto(self):
      return self.__produto
  def get_preco(self):
      return self.__preco
  def get_quantidade(self):
      return self.__quantidade
  #Trocar informação
print("Preço atual do produto: ")
prod = Produtos("Massa","R$ 5,00", 1)
print(f"Nome do produto: {prod.get_produto()}\nPreço: {prod.get_preco()}"
      f"\nQuantidade de produtos:{prod.get_quantidade()}")
      

        
