class Aluno():
    def  __init__(self, c, n, m):
        self.__codigo = c 
        self.__nome = n 
        self.__matricula = m
    def get_codigo(self):
            return self.__codigo
    def get_nome(self):
        return self.__nome
    def get_matricula(self):
        return self.__matricula
    def set_codigo(self,codigo):
        self.__codigo = codigo
    def set_nome(self, nome):
        self.__nome = nome 
    def set_matricula(self, matricula):
        self.__matricula = matricula
        