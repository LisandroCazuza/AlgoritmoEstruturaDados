from Class_Aluno import Aluno
class Aluno_Graduacao():
    def __init__(self,s):
        self.__semestre = s
    def get_semestre(self):
        return self.__semestre
    def set_semestre(self,semestre):
        self.__semestre = semestre
        
        