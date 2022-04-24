# Aluna de graduação = sub classe ou classe filha 
from Class_Aluno import Aluno
class Aluno_Graduacao(Aluno):
    def __init__(self,s):
        self.__semestre = s
    def get_semestre(self):
        return self.__semestre
alunagraduacao = Aluno(13, "Ana" ," 2015211034" )
print(f"\nCódigo da aluna: {alunagraduacao.get_codigo()}\n" 
f"\nNome da aluna: {alunagraduacao.get_nome()}\n"
f"\nNº da matricula da aluna:  {alunagraduacao .get_matricula()}\n")
alunagrad = Aluno_Graduacao(3)
print(f"\nA aluna {alunagraduacao.get_nome()} está: {alunagrad .get_semestre()}"
 f"º semestre  de graduação ")
        
        