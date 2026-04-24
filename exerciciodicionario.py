dic_produtos = {"ipad": 7000, "iphone": 5000, "airpod": 2000, "macbook": 12000}

produto_buscado = input ("Digite o nome do produto:")
produto_buscado = produto_buscado.strip() # strip remove os espaços vazios
produto_buscado = produto_buscado.lower() # lower coloca tudo em letra minúscula

if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado]
    print("produto encontrado")
    print(f"produto: {produto_buscado}, preco: R${preco}")
else:
    print("produto não encontrado")

