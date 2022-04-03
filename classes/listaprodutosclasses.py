class Funcionarios( ):
      def __int__(self, nome, sobrenome, idade, endereco):
          self.  __nome = nome
          self.  __sobrenome = sobrenome
          self.  __idade = idade
          self. __endereco = endereco
      # Busca = Get 
      def get_nome(self):
            return self.__nome
      def get_sobrenome(self):
            return self.__sobrenome
      def get_idade(self):
            return self.__idade
      def get_endereco(self):
            return self.__endereco
      # Modifica = Set
      def set_endereco(self,endereco):
            self. __endereco = endereco
# Alteração (s) no dado (s)
def __str__(self):
      return f"Nome: {self.__nome} \n Sobrenome: {self.__sobrenome}\n Idade: {self.__idade}\n Endereco: {self.__endereco}"
func = Funcionarios( "Pedro",  "Souza",  30,   "casa", )
print(f"Nome: {func.get_nome()}") 
print(f"Sobrenome: {func.get_sobrenome()}")
print(f"Idade: {func.get_idade()}")
print(f"Endereco: {func.get_endereco()}")


 