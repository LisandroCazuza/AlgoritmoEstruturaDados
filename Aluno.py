def linha():
    print(">"*60)
class Aluno():
    def __init__(self, n="Ana ", c=23, m="200511025"):
        self.nome = n
        self.codigo = c
        self.matricula = m
    def mostrar(self):
        print(f"\n\nEducação Saber do Fundamental até a Graduação\n"
        f"\n\nDados dos (as) alunos (as)\n\nNome: {self.nome}"
        f"\nCódigo: {self.codigo}\nMatrícula: {self.matricula}")
class Membros(Aluno):
    def __init__(self, *args):
        super().__init__()
        self.idade = args[0]
        self.etnia= args[1]
    def mostrar(self):
        super().mostrar()
class AlunoFund(Membros):
    def __init__(self, a,*args, c="Aluna"):
        super( ).__init__(*args)
        self.ano = a
        self.cargo = c
    def mostrar(self):
        super().mostrar()
        print(f"\nEnsino Fundamental:\n\nAno: {self.ano} \nCargo: {self.cargo}"
        f"\nIdade: {self.idade}\nEtnia: {self.etnia}")
        linha()
class AlunoMedio(Membros):

    def __init__(self, a, *args, c="Aluna"):
        super().__init__(*args)
        self.ano = a
        self.cargo = c
    def mostrar(self):
        super().mostrar()
        print(f"\nEnsino Médio:\n\nAno: {self.ano} \nCargo: {self.cargo}"
        f"\nIdade: {self.idade}\nEtnia: {self.etnia}")
        linha()

class AlunoGraduacao(Membros):

    def __init__(self, s, *args, c="Aluna"):
        super().__init__(*args)
        self.semestre = s
        self.cargo = c
    def mostrar(self):
        super().mostrar()
        print(f"\nEnsino Superior:\n\nSemestre: {self.semestre} \nCargo: {self.cargo}"
        f"\nIdade: {self.idade}\nEtnia: {self.etnia}")
        linha()
estudante1 = AlunoFund( "9º ano ","14 anos","Negra")
estudante2 = AlunoMedio("3º ano ", "17 anos", "Negra")
estudante3 = AlunoGraduacao("1º semestre ", "19 anos", "Negra")
alunos = [estudante1, estudante2, estudante3]
for membro in alunos:
    membro.mostrar()
