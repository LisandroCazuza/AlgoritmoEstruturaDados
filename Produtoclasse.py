lst = [ ]
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

  def set_produto(self, produto):

      self.__produto = produto

  def set_preco(self,preco):

      self.__preco = preco

  def set_quantidade(self,quantidade):

      self.__quantidade = quantidade  

print("Preço atual do produto: ")

prod = Produtos("Massa","R$ 5,00", 1)

print(f"Nome do produto: {prod.get_produto()}\nPreço: {prod.get_preco()}"

      f"\nQuantidade de produtos:{prod.get_quantidade()}")
trocar1 = input("Digite o nome do novo  produto: ").title()
prod.set_produto(trocar1)
lst.append(trocar1)
trocar2 = float(input("Digite o novo valor do produto: "))
prod.set_preco(trocar2)
lst.append(trocar2)
trocar3 =int(input("Digite outra quantidade de produto: "))
prod.set_quantidade(trocar3)
lst.append(trocar3)
print("Lista:")
print(lst)



      

        

