lista_produtos = [ "ipad", "iphone", "airpod"]
lista_precos = [7000, 5000, 2000]

dic_produtos = {"ipad": 7000, "iphone": 5000, "airpod": 2000}

# pegar um item 
produto = "iphone"
posicao = lista_produtos.index(produto)
preco = lista_precos[posicao]
print(produto,preco)

# pegar um item usando o dicionário é mais simples
print(dic_produtos["ipad"])

dic_vendas = { "lira": [1000, 500, 1500], "joao": [500, 400, 500]}
print(dic_vendas["lira"])

# adicionar um item 
dic_produtos["macbook"] = 12000
print(dic_produtos)

# editar um item no dicionário
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.1
print(dic_produtos)

# remover um item 
dic_produtos.pop("macbook")  # usando o pop eu removi o item macbook
print(dic_produtos)

# verificar se existe um item no dicionário 
print("iphone" in dic_produtos)
print("iphone" in dic_produtos.keys()) # keys são as chaves do dicionários que são os produtos
print(2000 in dic_produtos.values())   # values são os valores do dicionário

# contagem de itens no dicionário
qtde = len(dic_produtos)
print(qtde)