# Aluna de graduação = sub classe ou classe filha 
from Class_Aluno import Aluno
class Aluno_Graduacao(Aluno):
    def __init__(self,s):
        self.__semestre = s
    def get_semestre(self):
        return self.__semestre
alunagraduacao = Aluno(13, "Ana" ," 2015211034" )
print(f"\n\tCódigo da aluna: {alunagraduacao.get_codigo()}" 
f"\n\tNome da aluna: {alunagraduacao.get_nome()}"
f"\n\tNº da matricula da aluna:  {alunagraduacao .get_matricula()}  ")
alunagrad = Aluno_Graduacao(3)
print(f"\tA aluna {alunagraduacao.get_nome()} está: {alunagrad .get_semestre()}"
 f"º semestre  de graduação ")
        
        