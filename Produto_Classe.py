class Produtos():
    def __init__(self,nome, preco, quantidade):
        self.nome  = nome
        self.preco = preco
        self.quantidade = quantidade
# Busca
    def get_nome(self):
        return self.nome
    def get_preco(self):
        return self.preco
    def get_quantidade(self):
        return self.quantidade
# Modifica
def set_nome(self):
    self.nome = nome
prod = Produtos("Ana ", 10, 2)
print(f"O nome para ser trocado: {prod.get_nome()}")
print( prod.get_preco())
print(prod.get_quantidade())
novo = input("Digite um novo nome: ")
prod.set_nome(novo)
print(f"O novo nome é: {prod.get_nome()}")
