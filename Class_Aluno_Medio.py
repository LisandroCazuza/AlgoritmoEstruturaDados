from Class_Aluno import Aluno
class Aluno_Media():
    def  __init__(self, a):
        self.__ano = a
    def get_ano(self):
        return self.__ano
    def sef_ano(self, ano):
        self.__ano = ano
ano = Aluno(" cod  ", "nome ", " matri" )
print(f"{ano.get_codigo()}\n {ano.get_nome()}"
      f"\n {ano.get_matricula()}  ")
ano2 = Aluno_Media("ano")
print(f"{ano2.get_ano()}")

                
    
    