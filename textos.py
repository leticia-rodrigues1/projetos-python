faturamento = 1000
custo = 600

lucro = faturamento - custo 

# str transforma qualquer valor em texto 
texto = "O lucro foi de " + str ( lucro ) + " e o faturamento  foi de " + str ( faturamento ) # tem essa forma de concatenar 

# f para formatar o texto 
texto = f" O lucro foi de R${lucro} e o faturamento foi de R${faturamento} "      # tem essa outra forma de concatenar 
 
print (texto)

email = "EMAIL_FALSO@gmail.com"

# lower coloca tudo em letra minúscula 
email = email.lower()

# strip ajusta todos os espaços 
email = email.strip()

print (email)

# para tamanho do texto eu uso o len 
print(len(email))

# posição eu uso o find que mostra a posição de um elemento
posicao = email.find("@")
print(posicao)

# pegar pedaços do texto eu uso o [ ] colchetes 
servidor = email[posicao]
print(servidor)

#email_falso@gmail.com

# trocar um pedaço do texto eu uso replace () ele troca um texto para outro texto
novo_email = email.replace("gmail.com", "yahoo.com.br")
print(novo_email)

# capitalize coloca apenas a primeira letra da primeira palavra em  maiúscula 
nome = "leticia rodrigues"
nome = nome.capitalize()
print(nome)

# title coloca a primeira letra de cada palavra do texto em maiúcula 
nome = nome.title()
print(nome)

# upper coloca todas as letras em maiúcula
nome = nome.upper()
print(nome)

# formatação numérica podemos usar o _ para visualizar as separações númericas melhor, não muda em nada só te ajuda a enxer melhor os números
faturamento = 1_000_000
custo = 600
texto = f" O lucro foi de R${lucro} e o faturamento foi de R${faturamento} " 


# só conseguimos concatenar texto com texto 
# a função str transforma qualquer valor em texto 
# f na frente significa que você vai formatar aquela frase 
# strip () ajustar os espaços vazios 
# lower () colocar em letra minúscula 
# find () mostra a posição de um elemento dentro do texto 
 
 # EXERCÍCIO

nome = "leticia rodrigues"
email = "leticia_rodrigues2026@hotmail.com" 

# descubra o servidor do email
posicao= email.find("@")
servidor = email[posicao + 1 :]
print(servidor)
                        
# descubra o primeiro nome do usuário
posicao_espaco = nome.find(" ")
primeiro_nome = nome [:posicao_espaco]
primeiro_nome = primeiro_nome.capitalize()
print(primeiro_nome)

# criar uma mensagem personalizada dizendo "Usuario tal foi cadastrado com sucesso no email tal"
mensagem = f"Usuário {primeiro_nome} foi cadastrado com sucesso no email {email}"
print(mensagem)