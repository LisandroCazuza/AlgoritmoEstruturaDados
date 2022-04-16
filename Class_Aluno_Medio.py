# Aluno ensino médio  = sub classe ou classe filha 
from Class_Aluno import Aluno
class Aluno_Media():
    def  __init__(self, a):
        self.__ano = a
    def get_ano(self):
        return self.__ano

alunomedio = Aluno(23 , "Lisandro ", 200511025)
print(f"\n\tCódigo do Aluno: {alunomedio.get_codigo()}"
f"\n\tNome do aluno:  {alunomedio .get_nome()}"
f"\n\tNº da matricula do aluno:  {alunomedio .get_matricula()}  ")
alunomed = Aluno_Media(2)
print(f"\tO aluno {alunomedio .get_nome()} está : {alunomed.get_ano()}º ano do segundo grau. ")
