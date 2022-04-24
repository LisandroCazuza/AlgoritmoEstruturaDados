# Aluno ensino médio  = sub classe ou classe filha 
from Class_Aluno import Aluno
class Aluno_Media(Aluno):
    def  __init__(self, a):
        self.__ano = a
    def get_ano(self):
        return self.__ano

alunomedio = Aluno(23 , "Lisandro "," 200511025")
print(f"\nCódigo do Aluno: {alunomedio.get_codigo()}\n"
f"\nNome do aluno:  {alunomedio .get_nome()}\n"
f"\nNº da matricula do aluno:  {alunomedio .get_matricula()}\n  ")
alunomed = Aluno_Media(2)
print(f"\nO aluno {alunomedio .get_nome()} está : {alunomed.get_ano()}º ano do segundo grau. ")
