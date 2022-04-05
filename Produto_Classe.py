class Produtos():
    def __init__(self,nome, preco, quant):
        self.__produto  = nome
        self.__valor = preco
        self.__quantidade = quant
        #Buscar informação 
        def get_produto(self):
            return self.__produto
        def get_valor(self):
            return self.__valor 
        def get_quantidade(self):
            return self.__quantidade
        #Modificar informação
        #def set_produto(self, nome):
            
prod = Produtos("Massa", 5, 2)
print(f"Nome produto: {prod.get_produto()}\n{prod.get_valor()}\n{prod.get_quantidade()}")

        
