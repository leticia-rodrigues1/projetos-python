faturamento = 1100 #numero inteiro
custo = 600

print("faturamento", faturamento)
novas_vendas = 1000

faturamento = faturamento + novas_vendas

imposto = 0.15 * faturamento  # float 
print(imposto)
lucro = faturamento - custo - imposto

print("faturamento", faturamento)
print("Custo", custo)
print("Lucro", "lucro")

mensagem = "O faturamento da loja foi de 2100" # string

teve_lucro = True  #boolean

margem_lucro = lucro/faturamento
print ("Margem", margem_lucro)


# int = numeros inteiros
# float = numeros casa decimal
# strings = textos
# boolean = booleanos (True False)

# mod -> %
# É o resto da divisão de um número pelo outro
# 10 % 3 
print(10 % 3)

# floor division -> // 
# É a parte inteira da divisão

# round é para arredondar 