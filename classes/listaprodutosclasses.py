class Produtos:
      def __int__(set, nome, preco, quantidade):
            self. __nome = nome
            self. __preco = preco
            self. __quantidade = quantidade
      # Busca = Get 
      def get_nome(self):
            return self. __nome
      def get_preco(self):
            return self.__preco
      def get_quantidade(self):
            return self.__quantidade
      # Modifica = Set 
      """
      def set_nome(self,nome):
            self.__nome = nome
      def set_preco(self,preco):
            self.__preco = preco
      def set_quantidade(self,quantidade):
            self.__quantidade = quantidade
            """
            
      def  __str__(self):
            return  f"Nome: {self.__nome}\n Preço: {self.__preco} \n Quantidade: {self.__quantidade}"
     