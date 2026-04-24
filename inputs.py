# Todo valor que vem de um INPUT é um TEXTO 

faturamento = input("Preencha com o faturamento (apenas números) ")
faturamento = int(faturamento) # para transformar o faturamento em números inteiros ou posso usar o float para colocar casas decimais 
custo = 600

lucro = faturamento - custo 
print(lucro)

vendas_dia1 = float(input("vendas_dia1 : ")) # coloco o float para transformar o input em números decimais 
vendas_dia2 = float(input("vendas_dia1 : ")) # coloco o float para transformar o input m números decimais 
print(vendas_dia1 + vendas_dia2)