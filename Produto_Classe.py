class Produtos():
  def __init__(self,nome, valor, quant ):
      self.__produto = nome 
      self.__preco = valor 
      self.__quantidade = quant
  def get_produto(self):
      return self.__produto
  def get_preco(self):
      return self.__preco
  def get_quantidade(self):
      return self.__quantidade
      

        
