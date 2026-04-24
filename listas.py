lista_vendas = [100, 50, 1000, 800, 35]
print(lista_vendas[0]) # Pegar um item da lista, aqui pegou o caracter 0 que é o primeiro item o número 100, os itens estão separados pela vírgula

# Para pegar o tamanho da lista eu uso o len que é o tamanho    
qtde_vendas = len(lista_vendas)
print(qtde_vendas)

# somar todos os itens
total_vendas =  sum(lista_vendas)
print(total_vendas)

# MAX, MIN, MEDIA
print(max(lista_vendas))
print(min(lista_vendas))
print(total_vendas / qtde_vendas)

# encontrar um elemento na lista ( a posição do elemento na lista )
print(100 in lista_vendas)  # usei o IN (em) para saber se existe o 1000 na lista_vendas

# encontrar um elemento da lista_produtos
lista_produtos = ["iphone", "ipad", "apple watch", "airpod","macbook"]
print("airpod" in lista_produtos)  # quero saber se tem "airpod" na lista_produtos, para encontrar se tem ou não

# posição 
posicao = lista_produtos.index("airpod")
print(posicao)

# como editar o valor de um item 
lista_precos = [5000, 7000, 3000, 1000, 10000]
novo_preco= lista_precos [0] *1.1
lista_precos [0] = novo_preco
print(lista_precos)

# para remover um item da lista temos o remove e o pop
# remove ( )
# pop    ( )

# lista_produtos.remove("macbook") # remove você passa o valor do item que quer remover 
lista_produtos.pop(4)                # pop você passa a posição do item que quer remover 
print(lista_produtos)

# append é para adicionar um item na lista, sempre adiciona no final da lista
lista_produtos.append("macbook")

# extend ele extende uma lista para outra lista, junta todos os itens das duas listas
lista2_produtos = ["PC", "air tag", "caixa de som"]
lista_produtos.extend(lista2_produtos)
print(lista_produtos)

# inserir um item em uma posição específica eu uso o insert
lista_produtos.insert(1, "airpod max")
print(lista_produtos)

# contar quantas vezes o item aparece na lista usando o count 
print(lista_produtos.count("airpod"))

# ordernar uma lista usamos sort coloca em ordem usando uma tabela de programação 
lista_produtos.sort()
print(lista_produtos)

lista_precos.sort()
print(lista_precos)
