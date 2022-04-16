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

        