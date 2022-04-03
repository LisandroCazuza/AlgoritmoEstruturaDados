class Bola():
    def __init__(self, tamanho, cor, material , marca):
        self.tamanho = tamanho 
        self.cor = cor 
        self.material = material 
        self.marca = marca
    def tipoTamanho(self):
        return self.tamanho
    def tipoCor(self):
        return self.cor
    def tipoMaterial(self):
        return self.material
    def tipoMarca(self):
        return self.marca
    def trocarTamanho(self, tamanho):
        self.tamanho = tamanho
caracteristica = Bola(20, 'vermelha', 'couro', 'Adidas')
print("caracteristic da bola: "
 "\nTamaho: ",caracteristica.tipoTamanho(),
 "\nCor:  ",caracteristica.tipoCor(), 
 "\nMaterial:",caracteristica.tipoMaterial(),
 "\nMarca: ",caracteristica.tipoMarca())
caracteristica.trocarTamanho(10)
print("A minha bola tem o tamanho novo: ",caracteristica.tipoTamanho())
class Jogador():
    def __init__(self, nome):
        self.nome = nome         
    def cadastroNome(self):
        return self.nome
n = Jogador(input("Digite o nome do jogador: "))
print("O nome do jogador é: ",n.cadastroNome().title())
class IdadeJogador():  
    def __init__(self, idade):
        self.idade = idade     
    def cadastroIdade(self):
        return self.idade
i = IdadeJogador(input("Digite a idade do jogador: "))
print(f"A idade do jogador é:  {i.cadastroIdade()} anos" )
class AlturaJogador():
    def __init__(self, altura):
        self.altura = altura
    def cadastroAltura(self):
        return self.altura
a = AlturaJogador(float(input("Digite a altura do jogador: ")))
print(f"A altura do jogador é:  {a.cadastroAltura()}")

    



 


