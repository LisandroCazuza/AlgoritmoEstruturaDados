lst = [ ]
class Produtos():

    def __init__(self,nome , valor , quant  ):

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

    #ccad1 informação

    def set_produto(self, produto):

        self.__produto = produto

    def set_preco(self,preco):

        self.__preco = preco

    def set_quantidade(self,quantidade):

        self.__quantidade = quantidade

#print("Preço atual do produto: ")

prod = Produtos(" "," "," " )
prod2 = Produtos("Arroz ",2, 1 )
print(f"Produto em promoção:"
      f"\n\nNome do produto: {prod2.get_produto()}"
     f"\nPreço: R$ {prod2.get_preco()}"
      f"\nQuantidade de produtos:{prod2.get_quantidade()}")
print("_______________________________________________________________")
#print("Se desejar continuar - Enter - cancelar - 0 - zero")
cad1 = input("Digite o nome do   produto: ").title()
prod.set_produto(cad1)
lst.append(cad1)
cad2 = float(input("Digite o  valor do produto: R$  "))
prod.set_preco(cad2)
lst.append(cad2)
cad3 = int(input("Digite quantidade de produto: "))
prod.set_quantidade(cad3)
lst.append(cad3)

print("Lista:")
print(lst)