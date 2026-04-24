lista_precos = [1500, 1000, 800, 200]

# produtos de até 1000 pagam 10% de imposto
# produtos á cima de 1000 pagam 15% de imposto

lista_precos = [1500, 1000, 800, 200]

def calcular_imposto(lista_valores):  # você usa o def para definir a função criada que é calcular_imposto
    imposto_total = 0 
    for preco in lista_valores:
        if preco > 1000:
            taxa = 0.15
        else:
            taxa = 0.1

        imposto = preco * taxa 
        imposto_total = imposto_total + imposto 

    return imposto_total

imposto_lista1 = calcular_imposto(lista_precos)
print(imposto_lista1)

lista2_precos = [500, 4000, 3200, 2600, 1000]
imposto_lista2 = calcular_imposto(lista2_precos)
print(imposto_lista2)