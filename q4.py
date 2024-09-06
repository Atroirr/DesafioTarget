cidadeValor = [['São Paulo', 67836.43],['Rio de Janeiro', 36678.66],['Minas Gerais', 29229.88], ['Espirito Santo', 27165.48], ['Outros', 19849.53]]

total = 0
for i in cidadeValor:
    total += i[1]

print(total)
def percentual(i):
    return ((100 * i) / total)

for i in cidadeValor:
    cidade = i[0]
    valor = i[1]

    print(f"O percentual da cidade de {cidade}, no valor de {round(valor,2)}, é de {round(percentual(valor),2)}%. \n")