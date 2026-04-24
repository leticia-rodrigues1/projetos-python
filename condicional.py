# O if é usado para tomar decisões no código.
# Ele verifica uma condição e:
# se for verdadeira → executa algo 
# se não for → ignora ou faz outra coisa

faturamento = 1000
custo = 600
lucro = faturamento - custo 

#if condicao/comparacao: 
    # o que eu quero que aconteça se a condição for VERDADEIRA
#else: 
    # o que eu quero que aconteça se essa condição for FALSA, só pode ter o else com o if antes

if lucro >= 0:
    print("lucro de", lucro)
    print("deu lucro")
else:
    print("prejuizo de", lucro)
    print("deu prejuizo")
    
print("acabou")