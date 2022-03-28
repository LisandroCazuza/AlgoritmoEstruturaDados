
"""Construir um algoritmo: 
Usando fuções para retirar elementos da lista. Acessar a posição usando 
parâmetros, eles serão impressos ou retirados:
1- Nome de cada produto;
2 - Preços dos produtos;
3- Quantidade de  produtos. """

lstnomeprod = [       ]

lstprecoprod = [     ]

lstquantprod = [   ]

 

while True:

            print("\n\t---------  Menu   ----------")

            print("\n\t0) Finalizar o Menu")

            print("\t1) Adicionar nome do produto")

            print("\t2) Adicionar preço do produto")

            print("\t3) Quantidade de produtos")

            print("\t4) Verificar nome do produto")

            print("\t5) Remover nome\n\t")

            opcao = int(input("\tEscolha uma opção [0-5]: "))

            if opcao == 0:

                print("Você saiu do sistema!")

                break

            elif opcao == 1:

                nomeprod1 = input("Digite o nome do produto: ")

                if nomeprod1 in lstnomeprod:

                    print(f"O produto {nomeprod1} já está na lista.")

                else:

                    lstnomeprod.append(nomeprod1)

                    print(f"O produto {nomeprod1} foi adicionado à lista.")

            elif opcao == 2:

                preco = float(input("Digite o preço do produto:R$  "))

                lstprecoprod.append(preco)

                print(f"Valor R$ {preco} adicionado à lista.")

            elif opcao == 3:

                print(f"O total de produtos são: {len(lstprecoprod)}")

            elif opcao == 4:

                nomeprod2 = input("Digite o nome do produto que deseja verificar: ")

                if nomeprod1 in lstnomeprod:

                    print(f"O produto {nomeprod1} está na lista.")

                else:

                    print(f"O produto {nomeprod2} não está na lista. !")

            elif opcao == 5 :

                print(f"Lista dos produtos cadastrados:\n\t {lstnomeprod}")

                nomeprod3 = input("Digite o nome do produto que deseja remover: ")

                if  nomeprod1 in lstnomeprod:

                    lstnomeprod.remove(nomeprod1)

                    print(f"O produto {nomeprod1} foi removido.")

                else:

                    print(f"O produto {nomeprod1} não estava na lista.")