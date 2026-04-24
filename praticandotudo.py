# Exemplo 1:
# produtos = ["iphone", "ipad", "airpod"]
# novo_produto = input("digite o nome do produto: ")

#if novo_produto in produtos:
#   print("produto já existente")
#else:
#   print(f"{novo_produto}cadastrado com sucesso")
#    produtos.append(novo_produto)

#   print (produtos)

# Exemplo 2:
# bonus dos funcionários
# vendas maiores do que 15000, ele ganha 500 do bonus
# se as vendas forem entre 5000 e 15000, então ele ganha 100 de bonus
# se as vendas forem menores do que 5000 então ele não ganha bonus

#vendas = 20000
#if vendas >= 15000: 
#    bonus =500

#else:
#    if vendas >= 5000:
#       bonus = 100

#    else:
#     bonus = 0

#print(f"bonus do funcionário:{bonus}")

#if vendas >= 15000:
#   bonus = 500

#elif vendas >= 5000:
#    bonus = 100 

#else:
#   bonus = 0

# Exemplo 3
# bonus dos funcionários
# vendas maiores do que 15000, ele ganha 500 do bonus
# se as vendas forem entre 5000 e 15000, então ele ganha 100 de bonus
# se as vendas forem menores do que 5000 então ele não ganha bonus
# só ganha bonus se as vendas totais da empresa forem maiores do que 10000

vendas_empresa = 200_000  #usamos o _ underline para nos ajudar a visualizar os números, não muda em nada só ajuda na visualização
meta_empresa = 100_000
vendas_funcionario = 17000

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:   
    bonus = 100
else:
    bonus = 0
   
print (f"bonus do funcionario: {bonus}") # atenção quando for fazer o print final e ele estar dentro da operação de cima, precisa dar o enter para ele descer e poder rodar 
    