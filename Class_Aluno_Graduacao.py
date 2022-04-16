from Class_Aluno import Aluno
class Aluno_Graduacao():
    def __init__(self,s):
        self.__semestre = s
    def get_semestre(self):
        return self.__semestre
alunagraduacao = Aluno(13, "Ana" , 2015211034 )
print(f"\n\tCódigo da aluna: {alunagraduacao.get_codigo()}" 
f"\n\tNome da aluna: {alunagraduacao.get_nome()}"
f"\n\tNº da matricula da aluna:  {alunagraduacao .get_matricula()}  ")

        
        